# Formats d'entree / sortie

## entities_raw.json (entree du scoring) - une observation par canal
[
  {"channel": "directory", "source": "ufe-phuket", "name": "ASIA Global Yachting",
   "website": "https://asiaglobalyachting.com", "phone": "+66801434380",
   "email": "nico@asiaglobalyachting.com", "contact": "Nicolas Monges",
   "city": "Phuket", "vertical": "nautisme_charter", "site_lang": "en_only"},
  {"channel": "serp", "keyword": "agence immobiliere koh samui", "loc": "FR",
   "name": "Samui Immobilier", "website": "https://www.samuiimmobilier.com/",
   "position": 1, "serp_type": "organic", "city": "Koh Samui",
   "vertical": "immobilier", "site_lang": "fr_only"},
  {"channel": "maps", "name": "Dream Properties Samui", "website": null,
   "phone": "+66 82 974 3415", "city": "Koh Samui", "vertical": "immobilier",
   "pct_fr_reviews": 100, "owner_responds_fr": false, "category_fr": false,
   "reviews_count": 46, "total_score": 5.0}
]
Champs site_lang: "fr_only" | "fr" | "en_only" | null (inconnu).
Note bug GBP/Facebook: si une fiche maps a website=facebook.com MAIS qu'un
autre canal (serp, directory) donne un vrai domaine pour la meme entite,
le script detecte gbp_issue=true et garde le vrai site (pas gbp_only).

## seo_profiles.json (etape 4)
{ "samuiimmobilier.com": {"pos_1_10": 12, "pos_11_20": 7, "total": 40, "etv": 350.0} }
(pos_1_10 = pos_1 + pos_2_3 + pos_4_10 du domain_rank_overview)

## prospects scores (sortie du script)
Liste triee T1 -> EXCLU. Champs cles par prospect:
- tier, francite + francite_detail, seo_profile, niveau_confiance
- flag_opportunite_langue, gbp_issue, volume_fr_valide
- gbp{reviews, score, pct_fr, repond, gbp_issue}
- serp_positions, channels
- offre_recommandee (descriptive), prix_conseille (vide), prix_audacieux (vide)
- a_verifier_avant_contact (liste de faits a checker avant tout email)
Tiers possibles: T1, T1_VOLUME_A_VALIDER, T2, A_QUALIFIER, T3,
T3_A_VERIFIER, CONCURRENT_LOCAL, CONCURRENT_REF, EXCLU.

## Fiche argumentaire (build_fiche.py)
Sections: identite + confiance, FAITS PROUVES (data), demande FR validee
(volumes), HYPOTHESES (clairement separees), angle de vente, OFFRE Kumo
(prix en [A FIXER]), A VERIFIER avant contact.
REGLE: la fiche nourrit le cold email, elle ne L'EST pas. Le prix n'est
jamais auto-genere. Toujours reformuler et verifier les faits sur le site
du prospect avant envoi (meme discipline que les corrections Kumo).
