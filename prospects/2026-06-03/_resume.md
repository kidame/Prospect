# Run 2026-06-03 — cuisiniste × Genève

**Couple (métier, zone) :** cuisiniste × Genève (pilier BÂTIMENT / agencement, zone forte demande).
**Rotation :** runs récents = menuiserie/ébénisterie, paysagiste, fiduciaire (Neuchâtel/Fribourg). Ici on change de métier ET de zone (Genève).

## Marché mesuré (canton GE, fr)
- "cuisiniste geneve" = **260/mois** (pic 390 en mars) -> demande réelle confirmée (> 150).
- "cuisiniste" (head) = 720/mois. "cuisines geneve" = 480/mois.
- Prestations fines minces : "cuisine sur mesure geneve", "agencement cuisine geneve", "amenagement cuisine geneve" = ~10/mois chacune (CPC élevés : agencement 29,86 / cuisine 14,32).
- SERP cœur "cuisiniste geneve" (mobile) :
  - Pack local top 3 = Cuisines Concept (4,9) · eba Genève (5,0) · TEK Cuisines (4,1).
  - Organique p.1 = cuisine-geneve.ch (Schmidt Carouge) · Cuisines Concept · TEK · Cuisine Art et Bois (#4) · Schmidt · architectes.ch · Style Cuisine (#7) · houzz · atelier-cuisines · local.ch.

## Collecte
- Apify enckay/google-maps-places-extractor : keyword=cuisiniste, location=Genève, minReviews=15 -> 17 fiches.
- Pré-filtre -> 8 finalistes avec domaine propre + 2 sans site (tel). Mesure DataForSEO sur les finalistes.

## RETENUS — canal EMAIL (2)
1. **Cuisine Art et Bois Sàrl** — cuisineartetbois.ch — info@cuisineartetbois.ch — 022 342 56 40 — Petit-Lancy 1213.
   39 avis 5,0. Organique p.1 (#4) sur la requête cœur MAIS absent du pack local (top 3 = Cuisines Concept/eba/TEK). OnPage 95. Offre : **Diagnostic 1200** (levier pack local). Score 78. Draft prêt.
2. **Style Cuisine SA** — stylecuisine.ch — devis@stylecuisine.ch — 022 344 97 40 — Carouge 1227.
   50 avis 4,7. Sur "cuisiniste geneve", dépassé par une page Schmidt (cuisine-geneve.ch) + annuaires alors qu'en p.1 (#7) ; absent pack local ; accueil mince (238 mots). Offre : **Diagnostic 1200**. Score 70. Draft prêt.

## À APPELER — bonus (3)
3. **Kitchen Prestige** — kitchenprestige.ch — **076 267 53 40** — Genève 1207.
   86 avis 5,0 mais invisible Google (organique page 4+, abs 38-57 ; absent pack). Site = page funnel GoHighLevel/LeadConnector, pas de structure SEO. Email présent mais protégé Cloudflare (non récupérable). Offre : **Refonte/Création + Diagnostic**. Angle : superbe réputation, introuvable sur Google.
4. **Cuisiniste-pro** — **079 533 67 73** — Genève. 49 avis 5,0, AUCUN site. Offre : **Création**.
5. **TIPS Cuisines Sàrl** — **022 810 40 00** — Genève. 28 avis 4,8, aucun site. Offre : **Création**.

## REJETÉS
Mesurés/loggés en Notion (péremption 120j) :
- Cuisines Concept — déjà dominant (pack #1 + organique #2, 399 avis).
- eba Genève — déjà dans le pack local #2 ; profil marque/groupe.
- IG Kitchen Design — site 100% anglais obsolète (2023) + note 3,5 (réputation).
- Arcadia Meubles — ICP faible (magasin de meubles / archi d'intérieur, cuisine = revente Boffi), pas d'email.
- Dimatech Cuisines Professionnelles — cuisines pro/dépannage B2B (resto), hors ICP résidentiel.

Exclusions dures au pré-filtre (non loggées) :
- SCHMIDT Cuisine & Rangement (franchise nationale, home-design.schmidt).
- Molteni Cuisine Genève (armanidada.com) + Molteni&C Flagship (molteni.it) + VIPP Cuisine (vipp.com) — marques internationales.
- L'atelier De Laure — cours de cuisine / traiteur (food, exclusion dure).
- Pollinger AG — Valais (hors zone GE) + note 3,3.

## Dedup
Aucun chevauchement avec la base : runs récents = Neuchâtel/Fribourg (menuiserie, paysagiste, fiduciaire). Nouveau métier + nouvelle zone.

## Erreurs / limites
- **Zefix indisponible** (HTTP 401) : pas de confirmation registre (date de fondation, dirigeant). Salutations email -> neutre "Bonjour," (aucun dirigeant confirmé pour les 2 retenus). Budget estimé via avis/forme juridique/secteur.
- Email Kitchen Prestige non récupérable (Cloudflare) malgré scrape (vdrmota/contact-info-scraper) + 2 pages testées -> bascule en "à appeler".

## Coût estimé
~1 à 2 CHF (Apify : 2 runs ~0,03 CU ; DataForSEO : ~13 appels — volumes, 1 SERP live, 5 OnPage, 3 ranked_keywords, 2 domain_rank_overview, serp_locations). Sous le plafond 10 CHF.
