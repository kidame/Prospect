# Résumé du run — 2026-05-31

- **Couple (secteur, zone) de ce run** : Menuiserie / Neuchâtel et agglomération (rotation depuis le run précédent : Paysagiste / La Chaux-de-Fonds).
- **Requête coeur** : « menuisier Neuchâtel » 70/mois (pic 210) ; voisin majeur « menuisier/menuiserie La Chaux-de-Fonds » 170/mois. Un prospect retenu (HALOMEN) est en réalité sur la zone Yverdon (« menuisier Yverdon » 140/mois, pic 390).
- **Collecte** : Apify `enckay/google-maps-places-extractor`, keyword=menuisier, location=Neuchâtel, 21 établissements (minReviews 4, fermés exclus).
- **Contact** : Apify `vdrmota/contact-info-scraper` sur 16 sites → 11 emails publics trouvés.
- **Analyse** : DataForSEO serp_organic_live_advanced (Neuchâtel + Yverdon, mobile), on_page_instant_pages, ranked_keywords, kw search volume.

## RETENUS — canal EMAIL (4)

| Prospect | Ville | Avis | Email | Offre | Score | Accroche mesurée |
|---|---|---|---|---|---|---|
| **HALOMEN Sàrl** | Chavornay (VD) | 49 (5,0) | info@halomen.ch | Diagnostic → Refonte | 78 | Site piraté (spam machines à sous injecté dans le HTML) + 0 mot-clé positionné ; absent pack ET organique sur « menuisier Yverdon » (140/mois) |
| **Évasion Bois Sàrl** | Saint-Blaise (NE) | 57 (5,0) | info@evasionbois.ch | Diagnostic → Suivi | 72 | Mieux noté du panel mais ~11e organique + absent pack sur « menuisier Neuchâtel » (70/mois) ; rang 69 sur La Chaux-de-Fonds (170/mois) ; accueil sans H1, ~84 mots |
| **Tschäppät & Moret SA** | Cornaux (NE) | 46 (5,0) | info@tschappat-moret.ch | Diagnostic / Suivi | 64 | Bon site, #1 sur sa marque et #8 « ossature bois », mais page 2 (rang 17-18) sur « menuiserie/menuisier Neuchâtel » + absent pack. Angle croissance |
| **Atelier Insolite SARL** | Neuchâtel | 26 (5,0) | info@atelierinsolite.ch | Diagnostic / Création | 58 | 1 seul mot-clé positionné (rang 77) ; Wix sans H1, page 1,18 Mo. Niche mobilier d'art |

Emails finalisés : voir chaque dossier. Brouillons Gmail créés (à revue manuelle par Thomas avant tout envoi).

## À APPELER — canal BONUS, pas d'email public (3)

| Prospect | Ville | Avis | Tel | Angle pour l'appel |
|---|---|---|---|---|
| **Menuiserie Ritz SA** | Neuchâtel | 35 (4,1) | +41 32 730 55 30 | #2 en organique sur « menuisier Neuchâtel » mais absent du pack local Google → levier fiche Google Business |
| **Opus Lignum** | Neuchâtel | 37 (5,0) | +41 79 855 80 91 | 37 avis 5,0 mais absent du pack ET de l'organique page 1 sur « menuisier Neuchâtel » |
| **Menuiserie Nussbaumer L.** | Les Vieux-Prés / Val-de-Ruz | 29 (5,0) | +41 32 853 87 60 | 29 avis 5,0, site sans email, invisible sur le coeur Neuchâtel |

## REJETÉS (raisons)
- **Menuiserie Walzer SA** (CdF/Yverdon) — déjà #1 du pack local sur « menuisier Yverdon » (62 avis 5,0) : besoin faible.
- **Menuiserie Joel Gonçalves** (Neuchâtel) — déjà pack local #1 + organique #10 sur « menuisier Neuchâtel » : déjà visible (note : site sur template `digitalone.site`, potentiel Refonte à requalifier plus tard).
- **Menuiserie Vauthier SA** (Boudry) — #3 en organique sur « menuisier Neuchâtel » (présent), note 3,9 : besoin plus faible.
- **Artéo sàrl** (Neuchâtel) — 4 avis seulement, fiche marquée « Fermé » : activité/budget incertains.
- **iwood SA** (Neuchâtel) — note 2,3/5 : réputation problématique.
- **En réserve (emails publics, non analysés en profondeur ce run, plafond budget)** : Entreprise Bastide (Neuchâtel, 11 avis), Bois et Design (Cernier, 32 avis), menuiserie S.Barfuss (Geneveys-sur-Coffrane, 20 avis), JD Menuiserie (Fétigny/FR, 35 avis), Ebéniste La Chignole (Coffrane, 9 avis). À requalifier au prochain run menuiserie.
- **Autres vus, hors priorité** : La fabrique du bois (Valangin, 7), Xylos (Corcelles, 5), Menuiserie Entre-deux-Lacs (Marin, 8), FRED (Boudry, 12).

## Coût estimé du run
- Apify Google Maps (21 places + contacts) : ~0,12 USD
- Apify contact scraper (16 sites) : ~0,07 USD
- DataForSEO : 3 SERP live + 4 OnPage + 4 ranked_keywords + 2 volumes + 2 locations ≈ 0,25 USD
- **Total ≈ 0,45 USD (~0,40 CHF)** — bien sous le plafond de 10 CHF.

## Erreurs / notes
- 1er appel SERP : `location_name` invalide (« Neuchâtel,Canton of… ») corrigé via serp_locations → « Neuchatel,Neuchatel,Switzerland ».
- HALOMEN : adresse absente de Google Maps, récupérée sur le site (Chavornay VD). Deux numéros publiés (site vs fiche Google).
- Gmail : pas d'outil d'envoi disponible, uniquement création de brouillons (conforme « drafts only, aucun envoi »).

## Prochain run
Éviter Menuiserie + Neuchâtel et Paysagiste + La Chaux-de-Fonds. Pistes : thérapeutes (ostéo/physio) ou fiduciaires à Fribourg ou Lausanne ; ou artisans (électricien/sanitaire) à Yverdon.
