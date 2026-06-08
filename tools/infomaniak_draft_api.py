#!/usr/bin/env python3
"""Cree un brouillon dans une boite Infomaniak via l'API mail HTTPS (kMail).

Pourquoi ce script (vs infomaniak_draft.py en IMAP)
---------------------------------------------------
L'environnement cloud de Claude Code (ou tourne la routine nocturne) ne laisse sortir que
le HTTPS (443) : l'IMAP 993 est bloque. CE script passe en HTTPS pur, donc il fonctionne
DEPUIS LE WEB / la routine nocturne, sans VPS ni pont. C'est la voie a privilegier.

  POST https://mail.infomaniak.com/api/mail/{mailboxUuid}/draft
  Authorization: Bearer <INFOMANIAK_API_TOKEN>
  Body JSON: {to, cc, bcc, subject, body, mime_type, action:"save"}

Cette route est celle des apps officielles kMail (open source, GPL). Elle n'est PAS dans le
portail developpeur public d'Infomaniak (qui ne gere que l'admin des boites). Elle est stable
en pratique (la prod Infomaniak en depend) mais non garantie cote support : si un jour elle
change, le repli est l'IMAP (infomaniak_draft.py) sur le VPS.

Config (variables d'environnement)
----------------------------------
  INFOMANIAK_API_TOKEN     jeton API Infomaniak avec scope "mail" (REQUIS)
                           -> a creer sur manager.infomaniak.com (Developpeur / Jetons API).
  INFOMANIAK_MAIL_ADDRESS  adresse de la boite (defaut: thomas.puglisi@kumo-seo.ch).
                           Sert a retrouver le mailboxUuid automatiquement.
  INFOMANIAK_MAILBOX_UUID  court-circuite la resolution auto si tu connais deja l'uuid.
  INFOMANIAK_MAIL_API      defaut: https://mail.infomaniak.com

Exemples
--------
  # voir la requete (URL + JSON) sans token ni reseau
  python3 tools/infomaniak_draft_api.py --to x@y.ch --subject Test --body "Bonjour," --dry-run

  # lister les boites accessibles + leur uuid (verifie le token)
  python3 tools/infomaniak_draft_api.py --list-mailboxes

  # depuis le bloc Notion (1re ligne "Objet : ...", puis le corps)
  python3 tools/infomaniak_draft_api.py --to prospect@exemple.ch --from-file mail.txt
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

# Reutilise le chargeur .env et le parseur de "fiche" du module IMAP voisin.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from infomaniak_draft import load_env_file, parse_fiche  # noqa: E402

DEFAULT_MAIL_API = "https://mail.infomaniak.com"
DEFAULT_ADDRESS = "thomas.puglisi@kumo-seo.ch"


def _token() -> str:
    tok = os.environ.get("INFOMANIAK_API_TOKEN")
    if not tok:
        sys.exit(
            "[erreur] INFOMANIAK_API_TOKEN manquant.\n"
            "  Cree un jeton API (scope 'mail') sur manager.infomaniak.com (Developpeur / Jetons API)\n"
            "  puis ajoute-le comme variable d'environnement INFOMANIAK_API_TOKEN."
        )
    return tok


def _api_base() -> str:
    return os.environ.get("INFOMANIAK_MAIL_API", DEFAULT_MAIL_API).rstrip("/")


def _request(method: str, url: str, body: dict | None = None) -> dict:
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {_token()}")
    req.add_header("Accept", "application/json")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        sys.exit(f"[erreur] {method} {url} -> HTTP {e.code}\n{detail}")
    except urllib.error.URLError as e:
        sys.exit(f"[erreur] reseau vers {url} : {e}")
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        sys.exit(f"[erreur] reponse non-JSON de {url} :\n{raw[:500]}")


def list_mailboxes() -> list[dict]:
    """GET /api/mail -> liste des boites (avec leur uuid et email)."""
    res = _request("GET", f"{_api_base()}/api/mail")
    data = res.get("data", res)
    return data if isinstance(data, list) else []


def resolve_mailbox_uuid(address: str) -> str:
    forced = os.environ.get("INFOMANIAK_MAILBOX_UUID")
    if forced:
        return forced
    boxes = list_mailboxes()
    for b in boxes:
        email = (b.get("email") or b.get("email_address") or "").lower()
        if email == address.lower():
            uuid = b.get("uuid") or b.get("mailbox_uuid")
            if uuid:
                return uuid
    dispo = ", ".join((b.get("email") or "?") for b in boxes) or "(aucune)"
    sys.exit(
        f"[erreur] boite '{address}' introuvable parmi : {dispo}\n"
        "  Verifie INFOMANIAK_MAIL_ADDRESS, ou force INFOMANIAK_MAILBOX_UUID."
    )


def build_draft_body(to_addr: str, subject: str, body: str, mime_type: str) -> dict:
    return {
        "to": [{"email": to_addr, "name": ""}],
        "cc": [],
        "bcc": [],
        "subject": subject,
        "body": body,
        "mime_type": mime_type,
        "action": "save",  # "save" = brouillon (pas d'envoi)
    }


def create_draft(address: str, draft_body: dict) -> dict:
    uuid = resolve_mailbox_uuid(address)
    url = f"{_api_base()}/api/mail/{uuid}/draft"
    res = _request("POST", url, draft_body)
    return res


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(description="Cree un brouillon Infomaniak via l'API mail HTTPS.")
    p.add_argument("--to", help="adresse du destinataire (le prospect)")
    p.add_argument("--subject", help="objet (sinon lu depuis --from-file)")
    p.add_argument("--body", help="corps (texte direct)")
    p.add_argument("--body-stdin", action="store_true", help="lit le corps depuis stdin")
    p.add_argument("--from-file", help="fichier 'fiche' : 1re ligne 'Objet : ...', le reste = corps")
    p.add_argument("--address", help="boite source (defaut: INFOMANIAK_MAIL_ADDRESS ou le defaut KUMO)")
    p.add_argument("--html", action="store_true", help="envoie le corps en text/html (defaut: text/plain)")
    p.add_argument("--dry-run", action="store_true", help="imprime la requete, aucun reseau ni token")
    p.add_argument("--list-mailboxes", action="store_true", help="liste les boites + uuid puis sort")
    args = p.parse_args(argv)
    load_env_file()

    if args.list_mailboxes:
        for b in list_mailboxes():
            print(f"{b.get('email','?'):40} uuid={b.get('uuid') or b.get('mailbox_uuid','?')}")
        return

    subject = args.subject or ""
    body = ""
    if args.from_file:
        with open(args.from_file, encoding="utf-8") as f:
            fsubject, body = parse_fiche(f.read())
        subject = subject or fsubject
    elif args.body_stdin:
        body = sys.stdin.read()
    elif args.body is not None:
        body = args.body
    else:
        p.error("fournir le corps via --from-file, --body ou --body-stdin")

    if not args.to:
        p.error("--to est requis")
    if not subject:
        p.error("objet manquant : --subject ou une ligne 'Objet : ...' dans le fichier")
    if not body.strip():
        p.error("corps vide")

    mime_type = "text/html" if args.html else "text/plain"
    if args.html:
        # conversion minimale des sauts de ligne pour un rendu correct en HTML
        body = body.replace("\n", "<br>\n")

    address = args.address or os.environ.get("INFOMANIAK_MAIL_ADDRESS") or DEFAULT_ADDRESS
    draft_body = build_draft_body(args.to, subject, body, mime_type)

    if args.dry_run:
        print("----- DRY-RUN : aucune connexion, aucun token requis -----")
        print(f"POST {_api_base()}/api/mail/<mailboxUuid>/draft")
        print(f"(boite source a resoudre : {address})")
        print(json.dumps(draft_body, ensure_ascii=False, indent=2))
        return

    res = create_draft(address, draft_body)
    data = res.get("data", res)
    uuid = data.get("uuid") if isinstance(data, dict) else None
    print(f"[ok] brouillon cree dans '{address}' -> {args.to}" + (f" (uuid {uuid})" if uuid else ""))


if __name__ == "__main__":
    main()
