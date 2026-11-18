#!/usr/bin/env python3
"""Etat de la boite Infomaniak de Thomas, en JSON compact sur la sortie standard.

Pourquoi ce script existe
-------------------------
La routine relance (BOITE.md) et la routine de recherche ("la boite fait foi") doivent savoir
ce qui est parti, ce qui est revenu et ce qui attend en brouillon. L'outil MCP `lister_messages`
ne montre pas toujours les destinataires : ce script lit l'API mail une fois et rend tout.

LECTURE SEULE : il ne cree, ne modifie et ne supprime rien. Rien n'est ecrit sur le disque :
ne redirige JAMAIS la sortie vers un fichier du depot (donnees prospect).

Usage
-----
  python3 tools/boite_etat.py                 # envoyes 120 jours, recus 30 jours, brouillons
  python3 tools/boite_etat.py --tout          # tous les envoyes (controle complet)
  python3 tools/boite_etat.py --jours-envoyes 60 --jours-recus 14
  python3 tools/boite_etat.py --historique    # toute la boite : {adresse: n envois, premier,
                                              # dernier} + tous les expediteurs deja recus

Sortie : un objet JSON
  envoyes    : [{to:[...], date, objet}]
  adresses_envoyees : toutes les adresses deja destinataires (sur la periode lue)
  domaines_envoyes  : leurs domaines, hors domaines generiques (gmail, bluewin...)
  brouillons : [{to:[...], date, objet, uuid}]   uuid = celui a passer a supprimer_brouillon
  recus      : [{from, date, objet, apercu, dossier, retour}]  retour=true = avis de non-distribution
Config : INFOMANIAK_API_TOKEN (variable d'environnement ou .env), INFOMANIAK_MAIL_ADDRESS.
"""
import argparse
import datetime
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from infomaniak_draft import load_env_file  # noqa: E402
from infomaniak_draft_api import (  # noqa: E402
    DEFAULT_ADDRESS, resolve_mailbox_uuid, list_folders, get_messages)

GENERIQUES = {
    "gmail.com", "googlemail.com", "hotmail.com", "hotmail.ch", "hotmail.fr", "outlook.com",
    "outlook.fr", "live.com", "live.fr", "windowslive.com", "msn.com", "bluewin.ch", "sunrise.ch",
    "hispeed.ch", "net2000.ch", "vtxnet.ch", "vtx.ch", "yahoo.com", "yahoo.fr", "icloud.com",
    "me.com", "gmx.ch", "gmx.net", "gmx.com", "protonmail.com", "proton.me", "romandie.com",
}
RETOUR_EXP = ("mailer-daemon", "postmaster", "mail delivery")
RETOUR_OBJ = ("undeliver", "delivery status", "non remis", "delivery failed", "failure notice",
              "returned mail", "non distribu", "could not be delivered")


def adresses(liste):
    return [(x.get("email") or "").lower().strip() for x in (liste or []) if x.get("email")]


def lire(uuid, dossier, depuis):
    """Tous les messages d'un dossier, du plus recent au plus ancien, jusqu'a la date `depuis`."""
    out, off = [], 0
    while True:
        d = get_messages(uuid, dossier["id"], off)
        fils = d.get("threads") or []
        if not fils:
            break
        stop = False
        for t in fils:
            for m in (t.get("messages") or [t]):
                date = (m.get("date") or "")[:10]
                if depuis and date and date < depuis:
                    stop = True
                    continue
                out.append(m)
        off += len(fils)
        if stop or off >= (d.get("total_messages_count") or 0):
            break
        time.sleep(0.2)
    return out


def main():
    p = argparse.ArgumentParser(description="Etat de la boite (lecture seule), JSON sur stdout.")
    p.add_argument("--jours-envoyes", type=int, default=120)
    p.add_argument("--jours-recus", type=int, default=30)
    p.add_argument("--tout", action="store_true", help="tous les envoyes, sans limite de date")
    p.add_argument("--historique", action="store_true",
                   help="resume de TOUTE la boite : envois par adresse et expediteurs deja recus")
    a = p.parse_args()
    try:
        load_env_file(".env")
    except Exception:
        pass
    adresse = os.environ.get("INFOMANIAK_MAIL_ADDRESS") or DEFAULT_ADDRESS
    uuid = resolve_mailbox_uuid(adresse)
    if a.historique:
        envois, exp, ignores = {}, set(), []
        for f in list_folders(uuid):
            role = (f.get("role") or "").upper()
            if role == "DRAFT":
                continue
            try:
                messages = lire(uuid, f, None)
            except Exception:
                ignores.append(f.get("name") or f.get("path") or "?")  # dossier virtuel ou illisible
                continue
            for m in messages:
                d = (m.get("date") or "")[:10]
                if role == "SENT":
                    for e in adresses(m.get("to")) + adresses(m.get("cc")):
                        x = envois.setdefault(e, {"n": 0, "premier": d, "dernier": d})
                        x["n"] += 1
                        if d and (not x["premier"] or d < x["premier"]):
                            x["premier"] = d
                        if d and d > x["dernier"]:
                            x["dernier"] = d
                else:
                    exp.update(adresses(m.get("from")))
        json.dump({"boite": adresse, "lu_le": datetime.date.today().isoformat(),
                   "envois_par_adresse": envois,
                   "expediteurs": sorted(exp), "dossiers_ignores": ignores,
                   "domaines_expediteurs": sorted({e.split("@")[-1] for e in exp} - GENERIQUES)},
                  sys.stdout, ensure_ascii=False)
        sys.stdout.write("\n")
        return
    auj = datetime.date.today()
    depuis_env = None if a.tout else (auj - datetime.timedelta(days=a.jours_envoyes)).isoformat()
    depuis_rec = (auj - datetime.timedelta(days=a.jours_recus)).isoformat()

    res = {"boite": adresse, "lu_le": auj.isoformat(), "envoyes_depuis": depuis_env or "debut",
           "recus_depuis": depuis_rec, "envoyes": [], "brouillons": [], "recus": []}
    for f in list_folders(uuid):
        role = (f.get("role") or "").upper()
        if role == "SENT":
            for m in lire(uuid, f, depuis_env):
                res["envoyes"].append({"to": adresses(m.get("to")) + adresses(m.get("cc")),
                                       "date": (m.get("date") or "")[:10],
                                       "objet": (m.get("subject") or "")[:90]})
        elif role == "DRAFT":
            for m in lire(uuid, f, None):
                ressource = (m.get("draft_resource") or "").rstrip("/")
                res["brouillons"].append({"to": adresses(m.get("to")),
                                          "date": (m.get("date") or "")[:10],
                                          "objet": (m.get("subject") or "")[:90],
                                          "uuid": ressource.split("/")[-1] if ressource else None})
        elif role in ("INBOX", "SPAM"):
            for m in lire(uuid, f, depuis_rec):
                exp = (adresses(m.get("from")) or [""])[0]
                objet = m.get("subject") or ""
                retour = any(k in exp for k in RETOUR_EXP) or any(k in objet.lower() for k in RETOUR_OBJ)
                res["recus"].append({"from": exp, "date": (m.get("date") or "")[:10],
                                     "objet": objet[:90], "apercu": (m.get("preview") or "")[:240],
                                     "dossier": "reception" if role == "INBOX" else "indesirables",
                                     "retour": retour})
    toutes = sorted({e for m in res["envoyes"] for e in m["to"]})
    res["adresses_envoyees"] = toutes
    res["domaines_envoyes"] = sorted({e.split("@")[-1] for e in toutes} - GENERIQUES)
    res["compte"] = {"envoyes": len(res["envoyes"]), "brouillons": len(res["brouillons"]),
                     "recus": len(res["recus"]), "retours": sum(1 for r in res["recus"] if r["retour"])}
    json.dump(res, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
