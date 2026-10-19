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
import html as _htmllib
import json
import os
import re
import sys
import urllib.error
import urllib.request

# Reutilise le chargeur .env et le parseur de "fiche" du module IMAP voisin.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from infomaniak_draft import load_env_file, parse_fiche  # noqa: E402

DEFAULT_MAIL_API = "https://mail.infomaniak.com"
DEFAULT_ADDRESS = "thomas.puglisi@kumo-seo.ch"


class InfomaniakError(Exception):
    """Erreur metier/reseau cote API Infomaniak (levee, jamais sys.exit : reutilisable par le serveur MCP)."""


def _token() -> str:
    tok = os.environ.get("INFOMANIAK_API_TOKEN")
    if not tok:
        raise InfomaniakError(
            "INFOMANIAK_API_TOKEN manquant. Cree un jeton API (scope 'mail') sur "
            "manager.infomaniak.com (Developpeur / Jetons API) et expose-le en variable d'environnement."
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
        raise InfomaniakError(f"{method} {url} -> HTTP {e.code} : {detail[:500]}")
    except urllib.error.URLError as e:
        raise InfomaniakError(f"reseau vers {url} : {e}")
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        raise InfomaniakError(f"reponse non-JSON de {url} : {raw[:500]}")


def list_mailboxes() -> list[dict]:
    """GET /api/mailbox -> liste des boites accessibles (avec leur uuid et email)."""
    res = _request("GET", f"{_api_base()}/api/mailbox?with=aliases,unseen")
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
    raise InfomaniakError(
        f"boite '{address}' introuvable parmi : {dispo}. "
        "Verifie INFOMANIAK_MAIL_ADDRESS, ou force INFOMANIAK_MAILBOX_UUID."
    )


def list_folders(uuid: str) -> list[dict]:
    """GET /api/mail/{uuid}/folder -> dossiers (INBOX, Drafts, Sent, ...)."""
    res = _request("GET", f"{_api_base()}/api/mail/{uuid}/folder?with=ik-static")
    data = res.get("data", res)
    return data if isinstance(data, list) else []


def get_messages(uuid: str, folder_id: str, offset: int = 0) -> dict:
    """GET la liste des messages d'un dossier (entetes : expediteur, objet, date, uid)."""
    url = (
        f"{_api_base()}/api/mail/{uuid}/folder/{folder_id}/message"
        f"?thread=off&offset={offset}"
    )
    res = _request("GET", url)
    return res.get("data", res)


def get_message(uuid: str, folder_id: str, short_uid: str) -> dict:
    """GET le contenu complet d'un message (le short_uid est la partie avant '@' dans l'uid)."""
    short = str(short_uid).split("@", 1)[0]
    res = _request("GET", f"{_api_base()}/api/mail/{uuid}/folder/{folder_id}/message/{short}")
    return res.get("data", res)


def load_signature() -> str:
    """Lit la signature HTML (tools/signature.html) si presente, sinon chaine vide.

    Pourquoi : un brouillon cree par l'API ne declenche PAS l'insertion auto de la signature
    du webmail. On l'embarque donc nous-memes dans le corps HTML.
    """
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "signature.html")
    try:
        with open(path, encoding="utf-8") as f:
            return f.read().strip()
    except OSError:
        return ""


def _text_to_paragraphs(corps: str) -> str:
    """Transforme un corps texte (accents OK) en paragraphes HTML.

    Le webmail/app Infomaniak avale les sauts de ligne d'un corps text/plain (tout arrive en
    un bloc). On envoie donc du HTML : un <p> par paragraphe. Separateur de paragraphe = ligne
    vide ; a defaut (corps a simples retours a la ligne), chaque ligne non vide devient un <p>.
    Le texte est echappe (anti-injection HTML) ; les retours simples internes -> <br>.
    """
    text = corps.strip()
    blocks = [b.strip() for b in re.split(r"\n[ \t]*\n", text) if b.strip()]
    if len(blocks) <= 1:
        blocks = [ln.strip() for ln in text.split("\n") if ln.strip()]
    out = []
    for b in blocks:
        safe = _htmllib.escape(b).replace("\n", "<br>")
        out.append(f'<p style="margin:0 0 14px 0;">{safe}</p>')
    return "".join(out)


def _is_signoff_line(line: str) -> bool:
    """Vrai si la ligne est un pied de signature texte (a retirer avant la signature HTML)."""
    s = line.strip()
    if not s:
        return True
    t = s.lower().rstrip(".,").strip()
    if t in {
        "thomas", "thomas puglisi", "thomas, kumo", "thomas / kumo",
        "bien a vous", "bien à vous", "cordialement", "a bientot", "à bientôt",
        "a votre disposition", "à votre disposition",
    }:
        return True
    if "kumo" in t and len(s) <= 70:  # "KUMO - kumo-seo.ch", "kumo-seo.ch", ...
        return True
    if re.fullmatch(r"\+?[\d][\d\s().\-]{6,}", s):  # ligne de telephone
        return True
    return False


def _strip_trailing_signoff(text: str) -> str:
    """Enleve le pied de signature texte en fin de corps (Thomas / KUMO / tel / 'Bien a vous').

    Pourquoi : les mails rediges (Notion) finissent par 'Thomas / KUMO - kumo-seo.ch'. Comme on
    ajoute ensuite la signature HTML riche, on eviterait sinon une signature EN DOUBLE. On ne
    retire que les lignes finales qui matchent un pied connu : le corps reel n'est jamais touche.
    """
    lines = text.rstrip("\n").split("\n")
    while lines and _is_signoff_line(lines[-1]):
        lines.pop()
    return "\n".join(lines).rstrip()


def build_html_email(corps: str, with_signature: bool = True) -> str:
    """Corps HTML complet : paragraphes propres + (optionnel) la signature KUMO.

    Robuste : si le corps inclut deja un pied de signature texte (Thomas / KUMO / tel), il est
    retire avant d'ajouter la signature HTML -> jamais de double signature.
    """
    text = _strip_trailing_signoff(corps) if with_signature else corps
    inner = _text_to_paragraphs(text)
    if with_signature:
        sig = load_signature()
        if sig:
            inner += sig
    return (
        "<div style=\"font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;"
        'font-size:14px;color:#1a1423;line-height:1.5;">' + inner + "</div>"
    )


def build_draft_body(to_addr: str, subject: str, body: str, mime_type: str,
                     action: str = "save") -> dict:
    # NB : l'API refuse cc/bcc vides ("must have at least 1 items") -> on les OMET quand vides.
    return {
        "to": [{"email": to_addr, "name": ""}],
        "subject": subject,
        "body": body,
        "mime_type": mime_type,
        "action": action,  # "save" = brouillon ; "send" = ENVOI REEL (meme route kMail)
    }


def create_draft(address: str, draft_body: dict) -> dict:
    uuid = resolve_mailbox_uuid(address)
    url = f"{_api_base()}/api/mail/{uuid}/draft"
    res = _request("POST", url, draft_body)
    return res


def list_signatures(uuid: str) -> list[dict]:
    """GET /api/mail/{uuid}/signatures -> identites d'envoi de la boite (kMail).

    Pourquoi : l'action "send" exige (selon les versions de l'API) un identity_id ;
    chez Infomaniak les signatures FONT office d'identites (champ id + is_default).
    """
    res = _request("GET", f"{_api_base()}/api/mail/{uuid}/signatures")
    data = res.get("data", res)
    if isinstance(data, dict):
        data = data.get("signatures") or data.get("data") or []
    return data if isinstance(data, list) else []


def default_identity_id(uuid: str) -> int | None:
    sigs = list_signatures(uuid)
    for s in sigs:
        if s.get("is_default") or s.get("default"):
            return s.get("id")
    return sigs[0].get("id") if sigs else None


def send_email(address: str, draft_body: dict) -> dict:
    """ENVOI REEL d'un email via la route draft kMail (action="send").

    Meme endpoint que le brouillon ; seul "action" change. Si l'API exige une identite
    (erreur mentionnant identity), on resout l'identite par defaut de la boite (= sa
    signature par defaut) et on retente UNE fois. Leve InfomaniakError sinon : l'appelant
    (la routine) doit alors retomber sur creer_brouillon, jamais perdre le mail.
    """
    uuid = resolve_mailbox_uuid(address)
    url = f"{_api_base()}/api/mail/{uuid}/draft"
    body = dict(draft_body)
    body["action"] = "send"
    try:
        return _request("POST", url, body)
    except InfomaniakError as e:
        if "identity" not in str(e).lower():
            raise
        ident = default_identity_id(uuid)
        if ident is None:
            raise InfomaniakError(f"envoi refuse (identite requise) et aucune signature/identite trouvee : {e}")
        body["identity_id"] = ident
        return _request("POST", url, body)


def delete_draft(address: str, draft_uuid: str) -> dict:
    """Supprime un brouillon par son UUID de ressource (celui renvoye par create_draft).

    Cible la ressource 'draft' precise -> aucun risque de toucher un autre message/dossier.
    """
    uuid = resolve_mailbox_uuid(address)
    url = f"{_api_base()}/api/mail/{uuid}/draft/{draft_uuid}"
    return _request("DELETE", url)


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(description="Cree un brouillon Infomaniak via l'API mail HTTPS.")
    p.add_argument("--to", help="adresse du destinataire (le prospect)")
    p.add_argument("--subject", help="objet (sinon lu depuis --from-file)")
    p.add_argument("--body", help="corps (texte direct)")
    p.add_argument("--body-stdin", action="store_true", help="lit le corps depuis stdin")
    p.add_argument("--from-file", help="fichier 'fiche' : 1re ligne 'Objet : ...', le reste = corps")
    p.add_argument("--address", help="boite source (defaut: INFOMANIAK_MAIL_ADDRESS ou le defaut KUMO)")
    p.add_argument("--html", action="store_true", help="envoie le corps en text/html (defaut: text/plain)")
    p.add_argument("--send", action="store_true",
                   help="ENVOI REEL (action=send) au lieu d'un brouillon. A n'utiliser qu'en connaissance de cause.")
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
        print(f"(boite source a resoudre : {address} ; action : {'send' if args.send else 'save'})")
        print(json.dumps(draft_body, ensure_ascii=False, indent=2))
        return

    if args.send:
        send_email(address, draft_body)
        print(f"[ok] EMAIL ENVOYE depuis '{address}' -> {args.to}")
        return

    res = create_draft(address, draft_body)
    data = res.get("data", res)
    uuid = data.get("uuid") if isinstance(data, dict) else None
    print(f"[ok] brouillon cree dans '{address}' -> {args.to}" + (f" (uuid {uuid})" if uuid else ""))


if __name__ == "__main__":
    try:
        main()
    except InfomaniakError as e:
        sys.exit(f"[erreur] {e}")
