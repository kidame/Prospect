# Run prospection KUMO - 2026-05-31

## Couple (secteur, zone) du run
- **Secteur** : Paysagiste / Jardinier (mappe en "Artisan" dans Notion, faute d'option dediee)
- **Zone** : Fribourg (ville coeur) + agglo (Marly, Granges-Paccot, Matran, Givisiez, Villars-sur-Glane)
- **Rotation** : le(s) run(s) precedent(s) portaient sur Menuiserie / Ebenisterie dans la region Neuchatel. Changement de secteur ET de zone respecte.

## Marche mesure (DataForSEO, Google Ads, canton de Fribourg, fr)
- paysagiste Fribourg : 210/mois (requete coeur)
- jardinier Fribourg : 140/mois (2e marche)
- paysagiste Bulle : 110/mois
- amenagement exterieur Fribourg : 70/mois
- entretien jardin Fribourg : 50/mois
- amenagement jardin Fribourg : 40/mois
- paysagiste Marly : 40/mois
- creation jardin Fribourg : 30/mois

## SERP reel "paysagiste Fribourg" (mobile)
- Pack local (top 3) : Brodard Jardins SA, Boschung Paysages SA, Sciboz Jardins Sarl
- Organique : 1. Brodard, 2. local.ch, 3. Sciboz, 4. search.ch, 5. Boschung, 6. Tornare,
  7. Multipaysages, 8. annuaire.ch, 9. Demierre, 10. Page Paysages

## Collecte
- Apify enckay/google-maps-places-extractor : keyword "paysagiste", location "Fribourg",
  maxResults 50, minReviews 15, fermes exclues, extractContactDetails=true. 18 etablissements.
- Emails recuperes directement a la collecte Maps (pas besoin du contact-scraper pour les retenus).

## RETENUS - canal EMAIL (4) -> fiches Notion avec Diagnostic + Email (Draft pret coche)
1. **Multipaysages Sarl** (Fribourg) - info@multipaysages.ch - Score 74 - Offre Diagnostic
   Site faible (OnPage 58,5, pas de H1, ~3,4s), absent pack, organique #7, 2 mots-cles.
2. **Tornare Jardins Sarl** (Fribourg) - info@tornare-jardins.ch - Score 70 - Offre Diagnostic
   Absent pack, organique #6, etroit (3 kw), rate jardinier Fribourg (140). OnPage 71 (pas de desc).
3. **Corpataux Jardins Sarl** (Marly) - info@corpataux-jardins.ch - Score 72 - Offre Diagnostic
   #2 sur "paysagiste Marly" (40) mais #13 sur "paysagiste Fribourg" (210, ~5x) + #18 jardinier. Site sain (91,5), 4,8/37 avis.
4. **Demierre Jardins** (Fribourg) - info@demierre-jardins.ch - Score 66 - Offre Diagnostic
   Absent pack, organique #9, capte des prestations mais rate jardinier Fribourg (140). Site sain (88).

## A APPELER - canal BONUS (3) -> fiches Notion (Diagnostic, pas de mail)
1. **Page Paysages SA** (Fribourg) - +41 26 481 99 22 - organique #10, absent pack ; aucun email public trouve.
2. **Rim Jardins Sarl** (Villars-sur-Glane) - +41 79 322 55 66 - 4,9/23 avis mais AUCUN site web. Angle creation.
3. **Jardinerie du Gibloux** (Vuisternens) - +41 26 411 22 33 - 4,1/17, aucun site. Priorite basse.

## REJETES (4 analyses) -> fiches Notion en statut "Ancien"
1. **Brodard Jardins SA** - #1 pack + #1 organique : deja dominant, pas d'ecart.
2. **Boschung Paysages SA** - #2 pack + #5 organique : bien present (et pas d'email).
3. **Sciboz Jardins Sarl** - #3 pack + #3 organique : bien present.
4. **Aebischer Paysagisme Sarl** - hors cible : Dudingen (zone germanophone, Singine).

## Autres collectes non retenues (pool, hors coeur Fribourg ou bien places)
Jardins Sottas SA (Bulle), Gobet Espaces Verts (Bulle), Clement Paysages Sarl (Bulle),
Vial Paysages SA (Romont, pas d'email), Niclasse Paysagistes Sarl (Estavayer-le-Lac),
Espaces Verts Macheret (Givisiez, pas d'email). Non analyses en profondeur (autres villes,
hors requete coeur Fribourg) - a traiter dans un run dedie Bulle/Broye si rotation l'amene.

## Dedup
- Base Notion "Contacts" interrogee : tous les Place ID existants concernaient la Menuiserie
  (region Neuchatel). Aucun chevauchement avec les paysagistes de Fribourg. Aucun doublon.

## Cout estime du run
- Apify Maps : 2 runs ~0,024 CU (~0,05 CHF).
- Apify contact-scraper : plusieurs runs, dont des echecs sur premiere passe (~0,3 CU, ~0,3 CHF) -
  finalement inutiles, les emails venaient de la collecte Maps. A eviter au prochain run.
- DataForSEO : 1 SERP live + 1 volume + 4 OnPage + 4 ranked_keywords (~0,03 CHF).
- Total estime : ~0,5 CHF. Tres en dessous du plafond 10 CHF.

## Erreurs / notes pour la prochaine fois
- Format de localisation DataForSEO pour Fribourg : utiliser "Fribourg,Switzerland" (canton),
  PAS "Canton of Fribourg,Switzerland" ni "Fribourg,Canton of Fribourg,Switzerland" (rejetes).
- Notion : parent = data_source_id "de8f19f7-9e6a-416e-b484-4d1f184a47e2" (collection),
  PAS l'ID de database "a42395e8..." (404). Secteur n'a pas d'option "Paysagiste" -> "Artisan".
  Offre KUMO = "Diagnostic" (pas "Diagnostic 1200"). Confiance budget = Faible/Moyenne/Elevee.
- Les emails de la collecte Maps suffisent souvent : lancer le contact-scraper seulement si
  email absent ET site present.
