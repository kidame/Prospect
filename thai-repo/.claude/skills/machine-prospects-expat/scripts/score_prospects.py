#!/usr/bin/env python3
"""
score_prospects.py - fusion multi-canaux + scoring francite + tiers.

Usage:
  python3 score_prospects.py entities_raw.json [seo_profiles.json] > scored.json

entities_raw.json: liste d'observations (une par canal par business), schema
dans references/format-sortie.md. seo_profiles.json (optionnel, etape 4):
{ "domaine": {"pos_1_10": n, "pos_11_20": n, "total": n, "etv": f}, ... }

Tous les seuils sont des PARAMETRES ci-dessous (calibres sur echantillon
Koh Samui 06/2026, a re-calibrer si une nouvelle zone donne des resultats etranges).
"""
import json, re, sys, unicodedata

# ---------- PARAMETRES ----------
W = {
    "directory": 4,          # present dans un annuaire francophone
    "serp_multi": 3,         # rank sur >= 2 money keywords FR
    "serp_single": 2,        # rank sur 1 money keyword FR
    "pct_fr_high": 3,        # >= PCT_HIGH % d'avis FR
    "pct_fr_mid": 1,         # PCT_MID a PCT_HIGH-1 %
    "owner_fr": 2,           # le gerant repond aux avis en francais
    "name_fr": 2,            # nom du business a motif francais
    "cat_fr": 2,             # categorie Google explicitement francaise
    "site_fr": 2,            # site avec version/contenu FR
    "tld_fr": 1,             # domaine .fr ou mot FR dans le domaine
    "phone_fr": 1,           # numero +33 affiche
    "fr_mention": 2,         # mention explicite "francophone"/"equipe francaise" (titre SERP, site)
}
PCT_HIGH, PCT_MID = 60, 30
SEUIL_PROSPECT, SEUIL_VERIF = 5, 3
# Offre Kumo par PROFIL SEO (pour les vrais prospects T1/T2 seulement).
# DESCRIPTIVE, sans prix: le prix se fixe au cas par cas.
OFFRE_PAR_PROFIL = {
    "sous_performant": "Sprint SEO FR 90 jours: pousser les pages deja en page 2 vers la page 1",
    "invisible":       "Fondation SEO FR: creation du socle de pages + cluster money keywords",
    "emergent":        "Acceleration SEO FR: structurer et densifier le contenu existant",
    "gbp_only":        "Site one-page FR + optimisation fiche Google Business",
}
# Offre par TIER quand le tier prime sur le profil (concurrents, a qualifier, etc.)
OFFRE_PAR_TIER = {
    "A_QUALIFIER":          "Diagnostic DataForSEO avant toute proposition chiffree",
    "T1_VOLUME_A_VALIDER":  "Diagnostic volume FR + angle GBP/local (volume de recherche a confirmer)",
    "T3_A_VERIFIER":        "Verifier la francite avant tout demarchage",
    "CONCURRENT_LOCAL":     "NE PAS PROSPECTER. Analyser comme concurrent local (change l'angle de vente)",
    "CONCURRENT_REF":       "NE PAS PROSPECTER. Garder comme reference/benchmark concurrentiel",
    "EXCLU":                "Aucune action",
}
# Profils SEO (qualification etape 4)
ETV_GAGNANT = 8000           # trafic estime -> concurrent reference, ecarte
P1_GAGNANT = 150             # nb keywords en page 1 -> idem
P2_SOUSPERF = 10             # nb keywords en page 2 -> sous_performant
FR_NAME_PAT = re.compile(
    r"\b(chez|le|la|les|petit|petite|gourmand|bistro|bistrot|cote|boeuf|"
    r"paris|france|francais|francaise|french|immobilier|evasion|plaisir|"
    r"maison|villa(ge)?s? fran)\b", re.I)
FR_WORD_DOMAIN = re.compile(r"(francais|france|paris|immobilier|evasion|bonsplans|pourfrancais)", re.I)
# --------------------------------

NO_SITE_HOSTS = ("facebook.com", "instagram.com", "linktr.ee", "carrd.co",
                 "bit.ly", "wa.me", "m.me", "linkin.bio", "taplink.cc")

def norm_domain(u):
    if not u: return None
    d = re.sub(r"^https?://", "", u.strip().lower())
    d = d.split("/")[0].split("?")[0]
    d = re.sub(r"^www\.", "", d)
    if any(h in d for h in NO_SITE_HOSTS): return None  # page-lien, pas un site
    return d or None

def slug(name):
    s = unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())

def merge(observations):
    """Fusionne par domaine racine, fallback slug(nom) avec containment."""
    entities = []
    def find(dom, sl):
        for e in entities:
            if dom and e["domain"] == dom: return e
            if sl and len(sl) >= 8:
                ed = (e["domain"] or "").replace("-", "").replace(".", "")
                if e["slug"] == sl or (ed and (sl in ed or ed.startswith(sl[:12]))):
                    return e
        return None
    for o in observations:
        dom = norm_domain(o.get("website"))
        sl = slug(o.get("name"))
        e = find(dom, sl)
        if not e:
            e = {"name": o.get("name"), "domain": dom, "slug": sl, "city": o.get("city"),
                 "vertical": o.get("vertical"), "obs": [], "phones": set(),
                 "gbp_points_social": False}
            entities.append(e)
        if dom and not e["domain"]: e["domain"] = dom
        if o.get("vertical") and not e["vertical"]: e["vertical"] = o["vertical"]
        if o.get("phone"): e["phones"].add(o["phone"])
        # GBP/annuaire qui pointe vers une page sociale (Facebook, linktr.ee...)
        if o.get("website") and any(h in o["website"] for h in NO_SITE_HOSTS):
            e["gbp_points_social"] = True
        e["obs"].append(o)
    # Apres fusion: un vrai domaine a-t-il ete trouve par un AUTRE canal ?
    # Si oui, l'entite a un vrai site et la page sociale n'est qu'un mauvais lien GBP.
    for e in entities:
        e["has_real_site"] = bool(e["domain"])
        e["gbp_issue"] = e["gbp_points_social"] and e["has_real_site"]
        # gbp_only seulement si AUCUN vrai site nulle part
        e["truly_no_site"] = e["gbp_points_social"] and not e["has_real_site"]
    return entities

def score_francite(e):
    s, why = 0, []
    chans = {o["channel"] for o in e["obs"]}
    serp_kws = {o.get("keyword") for o in e["obs"] if o["channel"] == "serp" and o.get("keyword")}
    if "directory" in chans: s += W["directory"]; why.append("annuaire FR")
    if len(serp_kws) >= 2: s += W["serp_multi"]; why.append(f"rank sur {len(serp_kws)} money kw FR")
    elif len(serp_kws) == 1: s += W["serp_single"]; why.append("rank sur 1 money kw FR")
    maps = [o for o in e["obs"] if o["channel"] == "maps"]
    if maps:
        # agregation: on prend le MEILLEUR signal sur toutes les fiches Maps,
        # pas seulement la premiere observation (un business peut sortir sur
        # plusieurs requetes avec un signal faible en premier).
        pcts = [o.get("pct_fr_reviews") for o in maps if o.get("pct_fr_reviews") is not None]
        p = max(pcts) if pcts else None
        if p is not None:
            if p >= PCT_HIGH: s += W["pct_fr_high"]; why.append(f"{p}% avis FR")
            elif p >= PCT_MID: s += W["pct_fr_mid"]; why.append(f"{p}% avis FR (zone grise)")
        if any(o.get("owner_responds_fr") for o in maps):
            s += W["owner_fr"]; why.append("gerant repond en FR")
        if any(o.get("category_fr") for o in maps):
            s += W["cat_fr"]; why.append("categorie Google francaise")
    if FR_NAME_PAT.search(e["name"] or ""): s += W["name_fr"]; why.append("nom a motif FR")
    sl = any(o.get("site_lang") in ("fr", "fr_only") for o in e["obs"])
    if sl: s += W["site_fr"]; why.append("site en FR")
    if e["domain"] and (e["domain"].endswith(".fr") or FR_WORD_DOMAIN.search(e["domain"])):
        s += W["tld_fr"]; why.append("domaine FR")
    if any(p.startswith("+33") for p in e["phones"]): s += W["phone_fr"]; why.append("tel +33")
    if any(o.get("fr_mention") for o in e["obs"]):
        s += W["fr_mention"]; why.append("mention explicite francophone")
    # flag opportunite langue: francite forte mais site non-FR
    en_only = any(o.get("site_lang") == "en_only" for o in e["obs"])
    return s, why, (en_only and s >= SEUIL_PROSPECT)

def seo_class(profile, has_real_site, truly_no_site):
    # vraiment aucun site (Facebook/linktr seulement, et aucun vrai domaine ailleurs)
    if truly_no_site or not has_real_site:
        return "gbp_only", 3
    if profile is None: return "non_qualifie", 2
    if profile.get("etv", 0) >= ETV_GAGNANT or \
       (profile.get("pos_1_10", 0) >= P1_GAGNANT and
        profile.get("pos_11_20", 0) < profile.get("pos_1_10", 0)):
        return "deja_gagnant", 0
    if profile.get("total", 0) == 0: return "invisible", 3
    if profile.get("pos_11_20", 0) >= P2_SOUSPERF or \
       profile.get("pos_11_20", 0) >= max(1, profile.get("pos_1_10", 0)):
        return "sous_performant", 3
    return "emergent", 2

def tier(val, besoin, fr_score, seo_cls, has_money_kw=True, channels=None):
    # Concurrent local (agence web/SEO, val negative) = sortie dediee, PAS EXCLU.
    # Un concurrent change l'angle de vente, il ne doit pas etre cache.
    if val is not None and val < 0:
        return "CONCURRENT_LOCAL"
    if seo_cls == "deja_gagnant": return "CONCURRENT_REF"
    if val is None: val = 2
    if val == 0 or fr_score < SEUIL_VERIF: return "EXCLU"
    if fr_score < SEUIL_PROSPECT: return "T3_A_VERIFIER"
    # Bug 2: sans qualification SEO confirmee, jamais de T1/T2 final.
    if seo_cls == "non_qualifie":
        return "A_QUALIFIER"
    # Point 5: verticale prioritaire sans volume FR valide -> volume a valider.
    if not has_money_kw and val >= 4:
        return "T1_VOLUME_A_VALIDER"
    # Doctrine "aucun signal seul ne decide": un business connu UNIQUEMENT par
    # Google Maps ne monte en T1 que s'il est gbp_only (Maps est alors la seule
    # source possible). Sinon il plafonne a T2 tant qu'un 2e canal ne confirme pas.
    maps_only = channels is not None and set(channels) == {"maps"}
    if maps_only and seo_cls != "gbp_only":
        return "T2" if (val >= 3 and besoin >= 2) else "T3"
    if val >= 4 and besoin >= 3: return "T1"
    if (val == 3 and besoin >= 2) or (val >= 4 and besoin == 2): return "T2"
    return "T3"

def offre(tier_label, seo_cls):
    """L'offre depend du TIER d'abord (concurrents, a-qualifier), du profil ensuite."""
    if tier_label in OFFRE_PAR_TIER:
        return OFFRE_PAR_TIER[tier_label]
    return OFFRE_PAR_PROFIL.get(seo_cls, "diagnostic d'opportunite")

def confidence(fr_score, seo_cls):
    """Niveau de confiance pour le passage a l'action commerciale."""
    proven_seo = seo_cls in ("sous_performant", "invisible", "emergent", "gbp_only")
    if fr_score >= 7 and seo_cls in ("sous_performant", "invisible", "gbp_only"):
        return "fort"
    if fr_score >= 5 and proven_seo:
        return "moyen"
    return "faible"

def to_verify(e_has_gbp, seo_cls, opp, gbp_issue):
    """Faits a verifier sur le site AVANT tout contact (discipline anti-erreur)."""
    v = ["page services / offre reelle du prospect", "langue effective du site (visiter, pas deduire)"]
    if e_has_gbp: v.append("dernier avis Google et reactivite du gerant")
    if opp: v.append("confirmer que le site n'a aucune version FR (sinon l'angle tombe)")
    if gbp_issue: v.append("confirmer que la fiche Google pointe vers Facebook et pas le domaine")
    if seo_cls == "non_qualifie": v.append("LANCER DataForSEO domain_rank_overview avant de chiffrer quoi que ce soit")
    return v

def main():
    obs = json.load(open(sys.argv[1]))
    profiles = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}
    base = __file__.rsplit("/scripts/", 1)[0]
    verticales = json.load(open(base + "/data/verticales.json"))
    # verticales reellement couvertes par des money keywords (pour le gating point 5)
    try:
        mk = json.load(open(base + "/data/money_keywords_thailand.json"))
        covered = {k for k, v in mk.items() if not k.startswith("_") and v}
    except Exception:
        covered = set()
    out = []
    for e in merge(obs):
        fr, why, opp = score_francite(e)
        prof = profiles.get(e["domain"]) if e["domain"] else None
        cls, besoin = seo_class(prof, e["has_real_site"], e["truly_no_site"])
        val = verticales.get(e["vertical"] or "", None)
        has_kw = (e["vertical"] in covered) if e["vertical"] else True
        chans = sorted({o["channel"] for o in e["obs"]})
        t = tier(val, besoin, fr, cls, has_kw, chans)
        gbp_obs = [o for o in e["obs"] if o["channel"] == "maps"]
        gbp_block = None
        if gbp_obs:
            # agregation coherente avec le score: meilleur signal sur toutes les fiches
            pcts = [o.get("pct_fr_reviews") for o in gbp_obs if o.get("pct_fr_reviews") is not None]
            revs = [o.get("reviews_count") for o in gbp_obs if o.get("reviews_count") is not None]
            scores = [o.get("total_score") for o in gbp_obs if o.get("total_score") is not None]
            gbp_block = {
                "reviews": max(revs) if revs else None,
                "score": max(scores) if scores else None,
                "pct_fr": max(pcts) if pcts else None,
                "repond": any(o.get("owner_responds_fr") for o in gbp_obs),
                "gbp_issue": e["gbp_issue"],
            }
        out.append({
            "name": e["name"], "domain": e["domain"], "city": e["city"],
            "vertical": e["vertical"], "valeur_verticale": val,
            "francite": fr, "francite_detail": why,
            "flag_opportunite_langue": opp,
            "seo_profile": cls, "seo_data": prof, "besoin": besoin,
            "gbp_issue": e["gbp_issue"],
            "volume_fr_valide": has_kw,
            "channels": chans,
            "serp_positions": [{"kw": o.get("keyword"), "pos": o.get("position"), "loc": o.get("loc")}
                               for o in e["obs"] if o["channel"] == "serp"],
            "gbp": gbp_block,
            # --- bloc business (offre + confiance + a verifier, SANS prix) ---
            "offre_recommandee": offre(t, cls),
            "prix_conseille": "",   # a remplir par Kidame selon positionnement/marge
            "prix_audacieux": "",   # idem
            "niveau_confiance": confidence(fr, cls),
            "a_verifier_avant_contact": to_verify(bool(gbp_obs), cls, opp, e["gbp_issue"]),
            "tier": t,
        })
    order = {"T1": 0, "T1_VOLUME_A_VALIDER": 1, "T2": 2, "A_QUALIFIER": 3, "T3": 4,
             "T3_A_VERIFIER": 5, "CONCURRENT_LOCAL": 6, "CONCURRENT_REF": 7, "EXCLU": 8}
    out.sort(key=lambda x: (order.get(x["tier"], 9), -x["francite"]))
    json.dump(out, sys.stdout, indent=2, ensure_ascii=True)

if __name__ == "__main__":
    main()
