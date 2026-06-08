#!/usr/bin/env python3
"""Depose un brouillon pret a envoyer dans le dossier Brouillons d'une boite Infomaniak (IMAP).

Pourquoi ce script existe
-------------------------
La routine nocturne KUMO ecrit le mail finalise dans la fiche Notion (source unique).
Ce script prend ce mail et le pose en BROUILLON directement dans la boite Infomaniak,
pour que Thomas n'ait plus qu'a ouvrir son client mail et cliquer "Envoyer".

Il fait un IMAP APPEND avec le flag \\Draft dans le dossier Brouillons.
Aucun envoi : c'est un brouillon, la revue manuelle reste intacte.

IMPORTANT (reseau)
------------------
L'environnement cloud de Claude Code (ou tourne la routine nocturne) ne laisse sortir
que le HTTP/HTTPS (443) via un proxy. Le port IMAP 993 y est bloque. Ce script doit donc
tourner la ou le 993 est ouvert : le VPS Infomaniak (cron) ou une machine perso.
En --dry-run il n'ouvre aucune connexion : il imprime juste le message genere (testable partout).

Config par variables d'environnement
------------------------------------
  INFOMANIAK_IMAP_USER      login = adresse mail complete (ex. thomas@kumo-seo.ch)   [REQUIS]
  INFOMANIAK_IMAP_PASSWORD  mot de passe de l'application / de la boite               [REQUIS]
  INFOMANIAK_IMAP_HOST      defaut: mail.infomaniak.com
  INFOMANIAK_IMAP_PORT      defaut: 993
  INFOMANIAK_FROM           From affiche, ex. "Thomas Puglisi <thomas@kumo-seo.ch>"
                            (defaut: l'adresse INFOMANIAK_IMAP_USER)
  INFOMANIAK_DRAFTS_FOLDER  force le nom du dossier (sinon auto-detecte \\Drafts)

Exemples
--------
  # depuis un fichier "fiche" (1re ligne "Objet : ...", le reste = corps)
  python3 tools/infomaniak_draft.py --to prospect@exemple.ch --from-file mail.txt

  # arguments directs
  python3 tools/infomaniak_draft.py --to prospect@exemple.ch \
      --subject "Votre visibilite a Neuchatel" --body-stdin < corps.txt

  # voir le mail genere sans rien envoyer ni se connecter
  python3 tools/infomaniak_draft.py --to x@y.ch --subject Test --body "Bonjour," --dry-run

  # lister les dossiers de la boite (diagnostic du nom du dossier Brouillons)
  python3 tools/infomaniak_draft.py --list-folders
"""

from __future__ import annotations

import argparse
import imaplib
import os
import re
import sys
import time
from email.message import EmailMessage
from email.utils import formatdate, make_msgid


DEFAULT_HOST = "mail.infomaniak.com"
DEFAULT_PORT = 993
# Noms de dossier "Brouillons" frequents, par ordre de preference si la
# detection par flag \Drafts echoue.
DRAFT_FOLDER_FALLBACKS = ["Drafts", "Brouillons", "INBOX.Drafts", "INBOX.Brouillons"]


def _need(name: str) -> str:
    val = os.environ.get(name)
    if not val:
        sys.exit(f"[erreur] variable d'environnement manquante : {name}")
    return val


def build_message(to_addr: str, subject: str, body: str, from_addr: str) -> EmailMessage:
    """Construit un mail RFC 5322 en UTF-8 (accents conserves)."""
    msg = EmailMessage()
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    # Domaine du message-id derive de l'adresse d'envoi quand c'est possible.
    domain = from_addr.split("@")[-1].strip(" >") if "@" in from_addr else None
    msg["Message-ID"] = make_msgid(domain=domain) if domain else make_msgid()
    msg.set_content(body, subtype="plain", charset="utf-8")
    return msg


def parse_fiche(text: str) -> tuple[str, str]:
    """Decoupe un bloc 'fiche' : 1re ligne non vide 'Objet : X' -> sujet, le reste -> corps.

    Tolere 'Objet :', 'Objet:', 'Subject:'. Si aucune ligne objet, tout devient le corps
    et le sujet est vide (l'appelant devra fournir --subject).
    """
    lines = text.splitlines()
    # saute les lignes vides du debut
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    subject = ""
    if i < len(lines):
        m = re.match(r"^\s*(?:objet|subject)\s*:\s*(.*)$", lines[i], re.IGNORECASE)
        if m:
            subject = m.group(1).strip()
            i += 1
            # saute une ligne vide separatrice eventuelle
            if i < len(lines) and not lines[i].strip():
                i += 1
    body = "\n".join(lines[i:]).strip("\n")
    return subject, body


def _decode_folder_line(raw: bytes) -> tuple[str, str]:
    """Retourne (flags, nom_dossier) pour une ligne de reponse LIST."""
    line = raw.decode("utf-8", errors="replace")
    # format type : (\HasNoChildren \Drafts) "/" "Brouillons"
    m = re.match(r'^\((?P<flags>[^)]*)\)\s+(?:"[^"]*"|\S+)\s+(?P<name>.*)$', line)
    if not m:
        return "", line.strip()
    name = m.group("name").strip()
    if name.startswith('"') and name.endswith('"'):
        name = name[1:-1]
    return m.group("flags"), name


def detect_drafts_folder(imap: imaplib.IMAP4_SSL) -> str:
    """Trouve le dossier Brouillons : d'abord par flag special \\Drafts, sinon par nom connu."""
    forced = os.environ.get("INFOMANIAK_DRAFTS_FOLDER")
    if forced:
        return forced
    typ, data = imap.list()
    folders = []
    if typ == "OK":
        for raw in data:
            if not raw:
                continue
            flags, name = _decode_folder_line(raw)
            folders.append(name)
            if re.search(r"\\Drafts", flags, re.IGNORECASE):
                return name
    for cand in DRAFT_FOLDER_FALLBACKS:
        if cand in folders:
            return cand
    # dernier recours : le nom standard, l'APPEND echouera proprement si absent
    return "Drafts"


def list_folders() -> None:
    host = os.environ.get("INFOMANIAK_IMAP_HOST", DEFAULT_HOST)
    port = int(os.environ.get("INFOMANIAK_IMAP_PORT", DEFAULT_PORT))
    user = _need("INFOMANIAK_IMAP_USER")
    pwd = _need("INFOMANIAK_IMAP_PASSWORD")
    with imaplib.IMAP4_SSL(host, port) as imap:
        imap.login(user, pwd)
        typ, data = imap.list()
        if typ != "OK":
            sys.exit("[erreur] LIST a echoue")
        for raw in data:
            if raw:
                flags, name = _decode_folder_line(raw)
                marker = "  <- BROUILLONS" if re.search(r"\\Drafts", flags, re.IGNORECASE) else ""
                print(f"{name}    [{flags}]{marker}")


def append_draft(msg: EmailMessage, retries: int = 3) -> None:
    host = os.environ.get("INFOMANIAK_IMAP_HOST", DEFAULT_HOST)
    port = int(os.environ.get("INFOMANIAK_IMAP_PORT", DEFAULT_PORT))
    user = _need("INFOMANIAK_IMAP_USER")
    pwd = _need("INFOMANIAK_IMAP_PASSWORD")

    raw = msg.as_bytes()
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            with imaplib.IMAP4_SSL(host, port) as imap:
                imap.login(user, pwd)
                folder = detect_drafts_folder(imap)
                typ, resp = imap.append(
                    folder,
                    "(\\Draft)",
                    imaplib.Time2Internaldate(time.time()),
                    raw,
                )
                if typ != "OK":
                    raise RuntimeError(f"APPEND a echoue : {typ} {resp!r}")
                print(f"[ok] brouillon depose dans '{folder}' ({len(raw)} octets) -> {msg['To']}")
                return
        except Exception as e:  # noqa: BLE001 - on veut retenter sur erreurs reseau/serveur
            last_err = e
            wait = 2 ** (attempt + 1)
            print(f"[essai {attempt + 1}/{retries}] echec : {e} ; nouvelle tentative dans {wait}s", file=sys.stderr)
            time.sleep(wait)
    sys.exit(f"[erreur] depot du brouillon impossible apres {retries} essais : {last_err}")


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(description="Depose un brouillon dans une boite Infomaniak (IMAP APPEND).")
    p.add_argument("--to", help="adresse du destinataire (le prospect)")
    p.add_argument("--subject", help="objet du mail (sinon lu depuis --from-file)")
    p.add_argument("--body", help="corps du mail (texte direct)")
    p.add_argument("--body-stdin", action="store_true", help="lit le corps depuis stdin")
    p.add_argument("--from-file", help="fichier 'fiche' : 1re ligne 'Objet : ...', le reste = corps")
    p.add_argument("--from", dest="from_addr", help="From affiche (defaut: INFOMANIAK_FROM ou INFOMANIAK_IMAP_USER)")
    p.add_argument("--dry-run", action="store_true", help="imprime le mail genere, n'ouvre aucune connexion")
    p.add_argument("--list-folders", action="store_true", help="liste les dossiers IMAP et sort")
    args = p.parse_args(argv)

    if args.list_folders:
        list_folders()
        return

    # Resolution sujet + corps selon la source
    subject = args.subject or ""
    body = ""
    if args.from_file:
        with open(args.from_file, encoding="utf-8") as f:
            text = f.read()
        fsubject, body = parse_fiche(text)
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
        p.error("objet manquant : fournir --subject ou un fichier avec une ligne 'Objet : ...'")
    if not body.strip():
        p.error("corps vide")

    from_addr = (
        args.from_addr
        or os.environ.get("INFOMANIAK_FROM")
        or os.environ.get("INFOMANIAK_IMAP_USER")
        or "moi@exemple.ch"  # placeholder visible uniquement en --dry-run sans config
    )

    msg = build_message(args.to, subject, body, from_addr)

    if args.dry_run:
        print("----- DRY-RUN : message genere (rien n'est envoye ni connecte) -----")
        print(msg.as_string())
        return

    append_draft(msg)


if __name__ == "__main__":
    main()
