#!/usr/bin/env python3
"""Nouvelles inscriptions au registre du commerce (FOSC / SHAB, rubrique HR01), zone KUMO.

Source : API publique du portail des feuilles officielles (amtsblattportal.ch), sans cle.
Stdlib seule. Sortie : une ligne JSON par entreprise, triee par rang de proximite.
Le script ne juge PAS la cible (sauf associations, fondations, succursales, holdings) :
c'est la routine qui applique les exclusions de CLAUDE.md en lisant `but` et `fin_du_texte`
(le nom du titulaire ou des gerants s'y trouve).

Usage : python3 tools/fosc_nouvelles.py [--jours 30] [--max 60]
Rang 1 = Val-de-Travers et communes voisines ; rang 2 = reste du canton de Neuchatel ;
rang 3 = Nord vaudois (district Jura-Nord vaudois).
"""
from __future__ import annotations
import argparse, datetime as dt, json, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

API = "https://amtsblattportal.ch/api/v1/publications"
VDT_NPA = {2103, 2105, 2108, 2112, 2113, 2114, 2115, 2116, 2117, 2123, 2124, 2126, 2127, 2149}
VDT_COMMUNES = ("val-de-travers", "la côte-aux-fées", "les verrières")
NORD_VD = ("yverdon-les-bains", "grandson", "sainte-croix", "orbe", "vallorbe", "chavornay", "yvonand",
           "baulmes", "champagne", "concise", "bonvillars", "montagny-près-yverdon", "pomy", "mathod",
           "bullet", "vuiteboeuf", "onnens", "ependes", "essertines-sur-yverdon", "treycovagnes",
           "chamblon", "suchy", "belmont-sur-yverdon", "orges", "giez", "fiez", "provence", "tévenon",
           "rances", "arnex-sur-orbe", "agiez", "montcherand", "ballaigues", "lignerolle", "valeyres-sous-montagny",
           "cheseaux-noréaz", "romainmôtier-envy", "croy", "vaulion", "le chenit", "l'abbaye", "le lieu",
           "donneloye", "cronay", "cuarny", "villars-epeney", "champvent", "valeyres-sous-rances")

def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "kumo-prospect/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def liste(canton: str, debut: str, fin: str) -> list[dict]:
    out, page = [], 0
    while True:
        q = urllib.parse.urlencode({"publicationStates": "PUBLISHED", "cantons": canton, "subRubrics": "HR01",
                                    "publicationDate.start": debut, "publicationDate.end": fin,
                                    "pageRequest.page": page, "pageRequest.size": 100, "includeContent": "false"})
        d = json.loads(get(f"{API}?{q}"))
        c = d.get("content") or []
        out += c
        if len(out) >= (d.get("total") or 0) or not c:
            return out
        page += 1
        time.sleep(0.3)


def detail(pid: str) -> str:
    root = ET.fromstring(get(f"{API}/{pid}/xml"))
    el = root.find(".//publicationText")
    return (el.text or "") if el is not None else ""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--jours", type=int, default=30)
    ap.add_argument("--max", type=int, default=400)
    a = ap.parse_args()
    fin = dt.date.today()
    debut = fin - dt.timedelta(days=a.jours)
    rows = []
    for canton in ("NE", "VD"):
        for p in liste(canton, debut.isoformat(), fin.isoformat()):
            m = p["meta"]
            titre = (m.get("title") or {}).get("fr") or ""
            titre = re.sub(r"^Nouvelles entrées\s+", "", titre)
            commune = titre.rsplit(",", 1)[-1].strip().lower() if "," in titre else ""
            if canton == "VD" and commune not in NORD_VD:
                continue
            rows.append((canton, m["id"], (m.get("publicationDate") or "")[:10], titre, commune))
    res = []
    for canton, pid, date, titre, commune in rows:
        try:
            txt = detail(pid)
        except Exception as e:  # une fiche illisible ne casse pas le lot
            print(f"# detail illisible {titre}: {e}", file=sys.stderr)
            continue
        time.sleep(0.2)
        npa = re.search(r"\b(\d{4})\s+[A-ZÉÈÀÂÎÔÛa-zé]", txt)
        npa_i = int(npa.group(1)) if npa else None
        rang = 3 if canton == "VD" else (1 if (npa_i in VDT_NPA or commune in VDT_COMMUNES) else 2)
        uid = re.search(r"CHE-\d{3}\.\d{3}\.\d{3}", txt)
        but = re.search(r"But\s*:\s*(.+)", txt, re.S)
        forme = re.search(r"Nouvelle? (société à responsabilité limitée|société anonyme|entreprise individuelle|société en nom collectif|société coopérative|association|fondation|succursale)", txt)
        nom = titre.rsplit(",", 1)[0].strip()
        f = (forme.group(1) if forme else "")
        ecart = f in ("association", "fondation", "succursale") or "succursale" in nom.lower() or "holding" in nom.lower()
        adr = txt.split(uid.group(0))[0] if uid else txt[:200]
        res.append({"rang": rang, "date": date, "nom": nom, "commune": commune, "npa": npa_i,
                    "uid": uid.group(0) if uid else None, "forme": f or None,
                    "adresse": adr.strip(" ,.")[:160],
                    "but": (re.sub(r"\s+", " ", but.group(1)).strip()[:260] if but else None),
                    "fin_du_texte": re.sub(r"\s+", " ", txt).strip()[-700:],
                    "ecarte_d_office": ecart})
    res = [r for r in res if not r["ecarte_d_office"]]
    res.sort(key=lambda r: (r["rang"], r["date"]))
    for r in res[: a.max]:
        print(json.dumps(r, ensure_ascii=False))
    print(f"# total zone : {len(res)} inscriptions sur {a.jours} jours (rang1={sum(r['rang']==1 for r in res)}, "
          f"rang2={sum(r['rang']==2 for r in res)}, rang3={sum(r['rang']==3 for r in res)}) ; "
          f"associations, fondations, succursales et holdings deja retirees", file=sys.stderr)


if __name__ == "__main__":
    main()
