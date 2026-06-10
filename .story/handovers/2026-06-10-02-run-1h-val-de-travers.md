# Run 1h 2026-06-10 (sur demande) — segment batiment/bois x Val-de-Travers

**TL;DR** — Demande explicite de l'utilisateur : 10 prospects qualifies au Val-de-Travers (pas 3-5). Objectif atteint : 13 fiches creees dans Notion Contacts (10 retenus EMAIL avec drafts prets + 3 a-appeler bonus). Segment = batiment/bois (menuisier, ebeniste, charpente, electricien) x Val-de-Travers (Fleurier, Couvet, Motiers, Buttes, La Cote-aux-Fees, Mont-de-Buttes, Noiraigue, Les Verrieres). Aucun doublon avec les runs recents (carreleur x Geneve, peintre x Lausanne). ~3-4 CHF, sous plafond.

## Rotation
- Couvert : **batiment/bois + electricien x Val-de-Travers** (zone rurale neuve, jamais traitee).
- Vs 3 derniers handovers (carreleur x Geneve, peintre x Lausanne, instauration handover) : aucun doublon.
- 1 prospect ecarte car deja dans Notion (contacte le 2026-06-09, meme segment electricien). SEVT + Groupe E ecartes (utilites/nationales).
- **Prochain segment suggere** : transition energetique (installateur PAC/solaire) x Vaud ou Neuchatel (encore peu couvert), ou demenageur x Lausanne (ratissage avant echeances de bail). Eviter de re-piocher Val-de-Travers tout de suite (vallee quasi epuisee cote artisans joignables : ~24 fiches valley au total dont 13 retenues).

## Compteurs
- Maps : 2 runs (220 + 140 items) centres Fleurier puis Couvet. Apres filtre commune VdT : ~24 entreprises locales, tres majoritairement bois (economie forestiere du Jura).
- Retenus EMAIL (10) : 7 menuisier/ebeniste/charpente + 2 electricien + 1 charpente-couverture. Tous email de domaine sauf 1 (gmail perso, flag a-confirmer).
- A appeler (3) : 1 electricien sans site (pack #3), 1 menuisier sans email, 1 charpentier sans site.
- Emails resolus via vdrmota contact-scraper sur 9 domaines : 4 nouveaux emails de domaine recuperes.

## Cout
- Apify : Maps 0,086 CU (2 runs) + contact-scraper 0,047 CU.
- DataForSEO : 1 search_volume, 2 serp_locations, 2 serp_organic_live (mutualisees : 1 "menuiserie neuchatel" pour tout le bois, 1 "electricien val-de-travers" pour les electriciens). 0 on_page.
- Total estime ~3-4 CHF. Sous plafond.

## Observations systeme
- **Marche hyperlocal ~0, tete de canton = le vrai marche.** "menuisier/menuiserie fleurier|val-de-travers" = pas de volume ; "menuisier neuchatel" 90 + "menuiserie neuchatel" 90 = ~180/mois. Pour une vallee rurale, l'angle n'est PAS le pack local par village mais la visibilite tete-de-canton + la creation/refonte web. Pack + organique "menuiserie neuchatel" verrouilles par des maisons de Neuchatel-ville/Boudry (Ritz SA, Vauthier, Colette, Evasion Bois) ; AUCUN artisan VdT n'y figure -> besoin reel et homogene sur tout le segment.
- **SERP mutualisee payante confirmee** : 2 requetes coeur ont couvert 13 fiches. A garder.
- **Sourcing Maps en zone sparse** : la run multi-keywords a sur-indexe sur les 1ers mots-cles (menuisier/ebeniste) qui ont sature le cap de resultats et fait deborder les autres secteurs hors vallee (Yverdon, Pontarlier, Neuchatel-ville). Voir issue ouverte.

## Issue ouverte ce run
- 1 issue (sourcing Maps zone rurale : starvation de mots-cles). Cf. storybloq issue list.
