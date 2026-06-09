#!/usr/bin/env python3
"""Serveur MCP "infomaniak-mail" : brouillons + lecture, via l'API mail HTTPS Infomaniak (kMail).

Pourquoi pur Python (zero dependance)
-------------------------------------
Ce serveur tourne A L'INTERIEUR de l'environnement cloud de Claude Code (declare dans
.mcp.json a la racine du repo), y compris dans la routine nocturne. Pour qu'il soit
increvable (pas de `pip install` qui casse un run), il implemente le protocole MCP
(JSON-RPC 2.0 sur stdio, messages delimites par des sauts de ligne) avec la stdlib seule.

Il parle a Infomaniak en HTTPS (port 443, autorise depuis le cloud ; l'IMAP 993 ne l'est pas).

Auth : variable d'environnement INFOMANIAK_API_TOKEN (jeton API scope "mail").
Boite : INFOMANIAK_MAIL_ADDRESS (defaut thomas.puglisi@kumo-seo.ch).

Outils exposes :
  - lister_boites      : les boites accessibles (email + uuid)
  - lister_dossiers    : les dossiers de la boite (INBOX, Brouillons, Envoyes, ...)
  - creer_brouillon    : cree un brouillon pret a envoyer (action "save", aucun envoi)
  - lister_messages    : entetes des messages d'un dossier (expediteur, objet, date, uid)
  - lire_message       : contenu complet d'un message

Le protocole stdio : stdout = canal JSON-RPC UNIQUEMENT. Tous les logs vont sur stderr.
"""

from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from infomaniak_draft import load_env_file  # noqa: E402
from infomaniak_draft_api import (  # noqa: E402
    DEFAULT_ADDRESS,
    InfomaniakError,
    build_draft_body,
    build_html_email,
    create_draft,
    get_message,
    get_messages,
    list_folders,
    list_mailboxes,
    resolve_mailbox_uuid,
)

SERVER_NAME = "infomaniak-mail"
SERVER_VERSION = "0.1.0"
DEFAULT_PROTOCOL = "2025-06-18"

_uuid_cache: str | None = None


def log(*a: object) -> None:
    print(f"[{SERVER_NAME}]", *a, file=sys.stderr, flush=True)


def _address() -> str:
    return os.environ.get("INFOMANIAK_MAIL_ADDRESS") or DEFAULT_ADDRESS


def _uuid() -> str:
    global _uuid_cache
    if _uuid_cache is None:
        _uuid_cache = resolve_mailbox_uuid(_address())
    return _uuid_cache


def _resolve_folder(arg: str | None) -> dict:
    """Trouve un dossier par role ('inbox','draft',...), par nom, ou par id. Defaut : INBOX."""
    folders = list_folders(_uuid())
    want = (arg or "inbox").strip().lower()
    aliases = {
        "inbox": "inbox", "reception": "inbox", "réception": "inbox", "boite": "inbox",
        "brouillons": "draft", "brouillon": "draft", "drafts": "draft", "draft": "draft",
        "envoyes": "sent", "envoyés": "sent", "sent": "sent",
    }
    want_role = aliases.get(want, want)
    # 1) par role
    for f in folders:
        if str(f.get("role") or "").lower() == want_role:
            return f
    # 2) par id exact
    for f in folders:
        if str(f.get("id") or "") == (arg or ""):
            return f
    # 3) par nom (insensible a la casse)
    for f in folders:
        if str(f.get("name") or "").lower() == want:
            return f
    dispo = ", ".join(f"{f.get('name')}({f.get('role')})" for f in folders)
    raise InfomaniakError(f"dossier '{arg}' introuvable. Disponibles : {dispo}")


# ---------------------------------------------------------------------------
# Implementation des outils -> renvoient une chaine (texte affiche a Claude).
# ---------------------------------------------------------------------------

def tool_lister_boites(_args: dict) -> str:
    boxes = list_mailboxes()
    lignes = [f"- {b.get('email','?')}  (uuid {b.get('uuid') or b.get('mailbox_uuid','?')})" for b in boxes]
    return "Boites accessibles :\n" + ("\n".join(lignes) if lignes else "(aucune)")


def tool_lister_dossiers(_args: dict) -> str:
    folders = list_folders(_uuid())
    lignes = [f"- {f.get('name','?')}  [role={f.get('role') or '-'}, id={f.get('id','?')}]" for f in folders]
    return f"Dossiers de {_address()} :\n" + ("\n".join(lignes) if lignes else "(aucun)")


def tool_creer_brouillon(args: dict) -> str:
    to = (args.get("to") or "").strip()
    objet = (args.get("objet") or args.get("subject") or "").strip()
    corps = args.get("corps") or args.get("body") or ""
    if not to or not objet or not corps.strip():
        raise InfomaniakError("'to', 'objet' et 'corps' sont obligatoires.")
    # Defaut = HTML : le webmail/app Infomaniak avale les sauts de ligne d'un text/plain
    # (le corps arrive en un bloc, sans mise en page). En HTML, paragraphes + signature OK.
    # Pour forcer le texte brut (sans signature), passer html=false.
    plain = args.get("html") is False
    signature = args.get("signature", True)
    if plain:
        mime, body_text = "text/plain", corps
    else:
        mime, body_text = "text/html", build_html_email(corps, bool(signature))
    body = build_draft_body(to, objet, body_text, mime)
    cc = args.get("cc") or []
    if isinstance(cc, list) and cc:
        body["cc"] = [{"email": str(a), "name": ""} for a in cc]
    res = create_draft(_address(), body)
    data = res.get("data", res) if isinstance(res, dict) else {}
    uuid = data.get("uuid") if isinstance(data, dict) else None
    return f"Brouillon cree dans {_address()} pour {to}." + (f" (uuid {uuid})" if uuid else "")


def _expediteur(item: dict) -> str:
    frm = item.get("from") or item.get("sender") or []
    if isinstance(frm, list) and frm:
        return frm[0].get("email") or frm[0].get("name") or "?"
    return "?"


def tool_lister_messages(args: dict) -> str:
    folder = _resolve_folder(args.get("dossier"))
    offset = int(args.get("offset") or 0)
    data = get_messages(_uuid(), folder.get("id"), offset)
    # L'API renvoie data.threads[] ; chaque thread porte les entetes + messages[].
    threads = data.get("threads") if isinstance(data, dict) else None
    if threads is None and isinstance(data, dict):
        threads = data.get("messages")  # repli si structure differente
    if not threads:
        return f"Aucun message dans {folder.get('name')} (offset {offset})."
    lignes = []
    for t in threads[:25]:
        msgs = t.get("messages") if isinstance(t, dict) else None
        uid = (msgs[0].get("uid") if msgs else None) or t.get("uid", "?")
        lignes.append(
            f"- [uid {uid}] {t.get('date','')} | {_expediteur(t)} | {t.get('subject') or '(sans objet)'}"
        )
    return f"Messages de {folder.get('name')} :\n" + "\n".join(lignes)


def tool_lire_message(args: dict) -> str:
    folder = _resolve_folder(args.get("dossier"))
    uid = (args.get("uid") or "").strip()
    if not uid:
        raise InfomaniakError("'uid' est obligatoire (voir lister_messages).")
    m = get_message(_uuid(), folder.get("id"), uid)
    frm = m.get("from") or []
    if isinstance(frm, list) and frm:
        frm = frm[0].get("email") or frm[0].get("name") or "?"
    body = m.get("body") or {}
    texte = body.get("value") if isinstance(body, dict) else str(body)
    return (
        f"De : {frm}\nObjet : {m.get('subject','')}\nDate : {m.get('date','')}\n\n{texte or '(corps vide)'}"
    )


TOOLS = {
    "lister_boites": {
        "fn": tool_lister_boites,
        "description": "Liste les boites mail Infomaniak accessibles (email + uuid).",
        "inputSchema": {"type": "object", "properties": {}},
    },
    "lister_dossiers": {
        "fn": tool_lister_dossiers,
        "description": "Liste les dossiers de la boite (INBOX, Brouillons, Envoyes, etc.) avec leur id et role.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    "creer_brouillon": {
        "fn": tool_creer_brouillon,
        "description": (
            "Cree un BROUILLON pret a envoyer dans la boite Infomaniak (aucun envoi). "
            "Utilise pour deposer le mail d'un prospect, pret a relire et envoyer. "
            "Par defaut : corps en HTML (paragraphes propres + signature KUMO), car le webmail "
            "Infomaniak avale les sauts de ligne d'un texte brut."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "to": {"type": "string", "description": "adresse du destinataire"},
                "objet": {"type": "string", "description": "objet du mail"},
                "corps": {"type": "string", "description": "corps du mail (texte avec accents ; un paragraphe par ligne vide). NE PAS inclure la signature : elle est ajoutee automatiquement."},
                "cc": {"type": "array", "items": {"type": "string"}, "description": "copies (optionnel)"},
                "html": {"type": "boolean", "description": "true/omis = HTML formate (defaut). false = texte brut sans signature."},
                "signature": {"type": "boolean", "description": "ajouter la signature KUMO en HTML (defaut: true ; ignore si html=false)"},
            },
            "required": ["to", "objet", "corps"],
        },
    },
    "lister_messages": {
        "fn": tool_lister_messages,
        "description": "Liste les entetes des messages d'un dossier (expediteur, objet, date, uid).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "dossier": {"type": "string", "description": "role/nom/id du dossier (defaut: inbox)"},
                "offset": {"type": "integer", "description": "pagination (defaut 0)"},
            },
        },
    },
    "lire_message": {
        "fn": tool_lire_message,
        "description": "Lit le contenu complet d'un message (par son uid, via lister_messages).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "dossier": {"type": "string", "description": "role/nom/id du dossier (defaut: inbox)"},
                "uid": {"type": "string", "description": "uid du message (voir lister_messages)"},
            },
            "required": ["uid"],
        },
    },
}


# ---------------------------------------------------------------------------
# Boucle JSON-RPC / MCP (stdio, messages delimites par '\n')
# ---------------------------------------------------------------------------

def _send(obj: dict) -> None:
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def _result(req_id: object, result: dict) -> None:
    _send({"jsonrpc": "2.0", "id": req_id, "result": result})


def _error(req_id: object, code: int, message: str) -> None:
    _send({"jsonrpc": "2.0", "id": req_id, "error": {"code": code, "message": message}})


def handle(msg: dict) -> None:
    method = msg.get("method")
    req_id = msg.get("id")
    is_request = "id" in msg

    if method == "initialize":
        client_proto = (msg.get("params") or {}).get("protocolVersion")
        _result(req_id, {
            "protocolVersion": client_proto or DEFAULT_PROTOCOL,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        })
        return

    if method in ("notifications/initialized", "initialized", "notifications/cancelled"):
        return  # notifications : pas de reponse

    if method == "ping":
        if is_request:
            _result(req_id, {})
        return

    if method == "tools/list":
        tools = [
            {"name": name, "description": t["description"], "inputSchema": t["inputSchema"]}
            for name, t in TOOLS.items()
        ]
        _result(req_id, {"tools": tools})
        return

    if method == "tools/call":
        params = msg.get("params") or {}
        name = params.get("name")
        args = params.get("arguments") or {}
        tool = TOOLS.get(name)
        if not tool:
            _result(req_id, {"content": [{"type": "text", "text": f"Outil inconnu : {name}"}], "isError": True})
            return
        try:
            load_env_file()
            text = tool["fn"](args)
            _result(req_id, {"content": [{"type": "text", "text": text}], "isError": False})
        except InfomaniakError as e:
            _result(req_id, {"content": [{"type": "text", "text": f"Erreur Infomaniak : {e}"}], "isError": True})
        except Exception as e:  # noqa: BLE001 - tout renvoyer comme erreur d'outil, ne jamais crasher le serveur
            log("exception outil", name, repr(e))
            _result(req_id, {"content": [{"type": "text", "text": f"Erreur interne : {e}"}], "isError": True})
        return

    if is_request:
        _error(req_id, -32601, f"Methode inconnue : {method}")


def main() -> None:
    load_env_file()
    log("demarre")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            _error(None, -32700, "JSON invalide")
            continue
        try:
            handle(msg)
        except Exception as e:  # noqa: BLE001 - jamais laisser tomber la boucle
            log("exception handle", repr(e))
            if "id" in msg:
                _error(msg.get("id"), -32603, f"Erreur interne : {e}")
    log("arret (EOF)")


if __name__ == "__main__":
    main()
