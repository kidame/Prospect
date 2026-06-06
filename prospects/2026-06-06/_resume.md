# Run prospection KUMO - 2026-06-06

## Couple du run
- **Metier x Zone : cuisiniste x Lausanne** (pilier batiment/agencement #1, zone #1 demande)
- Rotation : runs precedents = electricien/menuiserie/paysagiste/fiduciaire/energie surtout sur Fribourg + Val-de-Travers/Neuchatel. Lausanne + cuisiniste = couple frais.

## Marche (DataForSEO, location Lausanne/Vaud/Switzerland, fr)
- "cuisiniste Lausanne" : **320 rech./mois** (KD 10, CPC 8.75) -> requete coeur, demande_reelle OK (>150).
- "cuisiniste Vaud" : 170/mois (CPC 13.29). "cuisine sur mesure" 170/mois. "renovation cuisine" cluster 480/mois.
- SERP coeur (mobile) : Pack local top 3 = Kouah Cuisines, Bulthaup, Cuisiniste Lausanne (EMD). Organique #1 = BeHome Interiors (blog listicle).

## Collecte
- Apify enckay/google-maps-places-extractor : keyword=cuisiniste, location=Lausanne, minReviews 15 -> 15 fiches.
- Apify vdrmota/contact-info-scraper sur 5 finalistes -> emails recuperes (4/5).

## RETENUS - canal EMAIL (4) [Draft pret coche dans Notion]
1. **A-TEC Cuisines Vaud SA** (cuisiniste.ch) - contact@cuisiniste.ch - Score 78 - Offre Creation.
   Absent pack+organique p.1 sur "cuisiniste Lausanne"; site = 1 page quasi vide (63 mots) malgre domaine premium + 57 avis 4.9. Signaux: concurrent_double, demande_reelle, receptivite.
2. **RENOVE-CUISINES Sarl** (renovcuisines.ch) - info@renovcuisines.ch - Score 68 - Offre Refonte.
   #1 sur "renovation cuisine" (marque/Kitlifting) mais page 2 sur "cuisiniste Lausanne/Vaud" (cuisine neuve); site Drupal 7 obsolete. Signaux: concurrent_double, demande_reelle, receptivite.
3. **JJH Cuisines Diffusion SA** (jjhcuisines.ch, Crissier) - info@jjhcuisines.ch - Score 64 - Offre Diagnostic.
   Page 2 (#9) sur "cuisiniste Lausanne"; absent pack local; fort sur niche acier Forster. Signaux: concurrent_double, demande_reelle.
4. **Cote Cuisines Sarl** (cotecuisines.ch, Prilly) - info@cotecuisines.ch - Score 58 - Offre Diagnostic.
   Present bas de page (#10-12) sur "cuisiniste Vaud/Lausanne" mais absent des 3 fiches du pack local. Signaux: concurrent_double, demande_reelle, receptivite.

## A APPELER - canal BONUS (1, pas d'email)
- **Zourdani Agencements Sarl** (zourdaniagencements.ch) - Tel +41 76 511 97 03.
  Site racine en **erreur 404** (signal page_cassee); absent pack+organique; 21 avis 5.0. Angle appel: votre site renvoie une erreur, vous etes injoignable via Google.

## REJETES (mesures, loggues pour dedup)
- **BeHome Interiors** : besoin faible, deja #1 organique sur la requete coeur + 115 avis.
- **Passion Cuisine Sarl** : present organique #7, coeur geographique = Morges/Lutry (a reprendre sur couple "cuisiniste x Morges").
- **Cuisines & Max Sarl** : hors zone (St-Aubin), 181 avis 5.0, a reprendre sur son bassin NE/FR.

## REJETES (exclusions dures / hors cible, non loggues en CRM)
- Bulthaup, APF Crissier (Cuisines Schmidt), Sanitas Troesch : franchises / enseignes nationales.
- Carota (cours de cuisine), Spoon Spoon (vaisselle retail), SWISSFRIGO (cuisines pro B2B), Atelier Art Home (generaliste tous corps d'etat) : hors cible cuisiniste residentiel.

## Cout estime
- Apify : Maps 0.015 CU + contacts 0.031 CU.
- DataForSEO : 1 serp_locations, 1 kw volume, 1 SERP live mobile, 5 OnPage instant, 4 ranked_keywords.
- Total estime : ~1 a 2 CHF (sous le plafond 10 CHF/nuit).

## Erreurs / notes
- Volume "cuisiniste Lausanne" : 110/mois au niveau ville-code, 320/mois au niveau Suisse (retenu 320 comme reference marche).
- Salutations : "Bonjour," neutre partout (aucun dirigeant actuel confirme).
- Emails tous domain-matched (info@/contact@ = domaine du site) -> confiance confirmee, pas d'alerte "a confirmer".
