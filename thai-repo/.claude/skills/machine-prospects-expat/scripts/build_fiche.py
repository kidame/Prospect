#!/usr/bin/env python3
"""
build_fiche.py - genere la fiche argumentaire MD d'un prospect.
Usage: python3 build_fiche.py scored.json <slug-ou-domaine> [money_keywords.json] > fiche.md

La fiche separe explicitement FAITS PROUVES, HYPOTHESES, et FAITS A VERIFIER
avant contact. Elle propose une offre Kumo et laisse le PRIX a remplir.
"""
import json, sys, re

def main():
    data = json.load(open(sys.argv[1]))
    key = sys.argv[2].lower()
    # Charger les money keywords: 3e argument si fourni, sinon le fichier par
    # defaut du skill (evite le faux "aucun money keyword" quand on suit le SKILL.md).
    if len(sys.argv) > 3:
        mk = json.load(open(sys.argv[3]))
    else:
        default_mk = __file__.rsplit("/scripts/", 1)[0] + "/data/money_keywords_thailand.json"
        try:
            mk = json.load(open(default_mk))
        except Exception:
            mk = {}
    p = next((x for x in data if (x.get("domain") or "").startswith(key)
              or re.sub(r"[^a-z0-9]", "", (x.get("name") or "").lower()).startswith(
                  re.sub(r"[^a-z0-9]", "", key))), None)
    if not p:
        sys.exit(f"Prospect introuvable: {key}")
    L = []
    L.append(f"# Fiche prospect: {p['name']}")
    L.append("")
    L.append(f"- Domaine: {p['domain'] or 'AUCUN SITE (prospect GBP-only)'}")
    L.append(f"- Ville / verticale: {p.get('city') or '?'} / {p.get('vertical')}")
    L.append(f"- Tier: {p['tier']} | Niveau de confiance: {p.get('niveau_confiance','?')}")
    L.append(f"- Francite: {p['francite']} ({', '.join(p['francite_detail'])})")

    # --- FAITS PROUVES ---
    L.append("")
    L.append("## Faits prouves (data)")
    L.append(f"- Profil SEO: {p['seo_profile']}" +
             (f" | {p['seo_data']}" if p.get('seo_data') else ""))
    if p.get("gbp"):
        g = p["gbp"]
        line = (f"- Google Business: {g.get('reviews')} avis, note {g.get('score')}, "
                f"{g.get('pct_fr')}% avis FR, repond en FR: {g.get('repond')}")
        if g.get("gbp_issue"):
            line += " | fiche Google pointe vers Facebook au lieu du domaine"
        L.append(line)
    if p.get("serp_positions"):
        for s in p["serp_positions"]:
            L.append(f"- Position {s['pos']} sur '{s['kw']}' ({s.get('loc')})")
    vert = p.get("vertical")
    if vert and vert in mk:
        L.append("")
        L.append("## Demande FR validee sur la verticale (volumes DataForSEO)")
        for k in mk[vert]:
            vol = k.get("vol")
            extra = f", CPC {k['cpc']} EUR" if k.get("cpc") else ""
            L.append(f"- {k['kw']} [{k['loc']}]: {vol if vol is not None else 'n/d'}/mois{extra}")
    elif vert:
        L.append("")
        L.append("## Demande FR sur la verticale")
        L.append("- ATTENTION: aucun money keyword valide pour cette verticale.")
        L.append("  Valider les volumes via DataForSEO AVANT de chiffrer un deal.")

    # --- HYPOTHESES (clairement separees des faits) ---
    hyp = []
    if p.get("flag_opportunite_langue"):
        hyp.append("Gerant francophone avec site non-FR: il laisse probablement une part "
                   "importante du trafic francophone sur la table (a nuancer: un site EN "
                   "capte encore du trafic marque et les requetes a mots anglais comme "
                   "yacht, catamaran, villa).")
    if p["seo_profile"] == "non_qualifie":
        hyp.append("Besoin SEO PAS encore confirme par DataForSEO: ne pas affirmer de "
                   "diagnostic chiffre avant qualification.")
    if hyp:
        L.append("")
        L.append("## Hypotheses (a confirmer, ne pas asserter en l'etat)")
        for h in hyp:
            L.append(f"- {h}")

    # --- ANGLE DE VENTE ---
    L.append("")
    L.append("## Angle de vente (a adapter, jamais envoyer brut)")
    cls = p["seo_profile"]
    if cls == "gbp_only":
        L.append("- Pas de vrai site: offre d'entree = fiche Google optimisee + site une page FR.")
    if cls == "sous_performant":
        L.append("- Pages bloquees en page 2: 'vous avez deja paye ce contenu, je le fais")
        L.append("  passer en page 1 sans rien recreer'.")
    if cls == "invisible":
        L.append("- Invisible sur Google FR malgre la demande: chiffrer le trafic rate")
        L.append("  et la valeur d'un seul client gagne.")
    if cls == "emergent":
        L.append("- Bonnes bases mais densite insuffisante: structurer pour accelerer.")
    if p.get("flag_opportunite_langue"):
        L.append("- Argument langue (defendable): pas de vraie porte d'entree SEO pour")
        L.append("  les recherches francophones, alors que la demande FR existe.")
    if p.get("gbp_issue"):
        L.append("- Quick win: la fiche Google pointe vers Facebook au lieu du site.")
        L.append("  Correction immediate = trafic recupere sans rien produire.")
    g = p.get("gbp")
    if g:
        if not g.get("repond"):
            L.append("- Ne repond pas aux avis Google: quick win e-reputation.")
        if (g.get("reviews") or 99) < 20:
            L.append("- Tres peu d'avis Google: collecte d'avis = quick win local pack.")

    # --- OFFRE + PRIX (prix a remplir) ---
    L.append("")
    L.append("## Offre Kumo")
    L.append(f"- Offre recommandee: {p.get('offre_recommandee','?')}")
    L.append(f"- Prix conseille (securise): {p.get('prix_conseille') or '[A FIXER]'}")
    L.append(f"- Prix audacieux: {p.get('prix_audacieux') or '[A FIXER]'}")
    L.append("- Raison du prix: [chiffrer la valeur d'un client type de cette verticale]")

    # --- A VERIFIER AVANT CONTACT ---
    L.append("")
    L.append("## A verifier avant contact (discipline anti-erreur)")
    for v in p.get("a_verifier_avant_contact", []):
        L.append(f"- {v}")

    print("\n".join(L))

if __name__ == "__main__":
    main()
