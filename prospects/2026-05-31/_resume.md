# Run prospection KUMO - 2026-05-31

## Couple (secteur, zone) du run
- **Secteur** : Paysagiste / Jardinier (mappe en "Artisan" dans Notion, pas d'option dediee).
- **Zone** : Fribourg (ville coeur) + agglo (Corminboeuf, Villars-sur-Glane, Treyvaux, Marly).
- **Rotation** : run(s) precedent(s) = Menuiserie / Ebenisterie region Neuchatel. Secteur ET zone changes.

## Marche mesure (DataForSEO)
- Google Ads (canton Fribourg, fr) : "paysagiste Fribourg" 140/mois, "pisciniste Fribourg" 880/mois,
  "paysagiste Bulle" 70/mois, "jardinier Fribourg" 20/mois, "amenagement exterieur Fribourg" 10/mois.
- DataForSEO Labs (canton Fribourg) : "paysagiste fribourg" 260/mois, difficulte 4.
- Requete coeur retenue : "paysagiste Fribourg".

## SERP reel "paysagiste Fribourg" (mobile, serp_organic_live_advanced)
- Pack local (top 3) : Jardin Passion Fribourg (marquee "Ferme"), La Feuille Verte - Ebneter, Art du Jardin Zbinden SA.
- Organique page 1 : search.ch, local.ch (annuaires), propaysages.ch (#6 abs), jardinsuisse-fribourg.ch,
  uni-vert.ch, deco-terre-jardin.ch, puis annuaires emploi/CCT, gachoud-paysagistes.ch (#18, page 2).

## Collecte
- Apify enckay/google-maps-places-extractor : keyword "paysagiste", location "Fribourg", maxResults 50,
  minReviews 15, fermes exclues, extractContactDetails=true. 18 etablissements (dataset AjbrDFccgFu0vNzwG).
- Emails : 1 seul via Maps (Lauper). Le reste via vdrmota/contact-info-scraper sur les sites.

## RETENUS - canal EMAIL avec Diagnostic + mail pret (Draft pret coche)
1. **Propaysages SA** (Villars-sur-Glane) - info@propaysages.ch - Score 76 - Diagnostic
   69 avis (plus gros budget), maison de 1948. Absent du pack local ; organique #6 mais etroit.
   Site : pas de meta description, 128 mots, head HTML en double, og:url errone (oxima.ch).
2. **Gachoud Paysages SA** (Treyvaux) - info@gachoudsa.ch - Score 70 - Diagnostic
   5,0/31, depuis 1980. Le domaine liste sur sa fiche Maps (gachoud-paysages.ch) renvoie une erreur 400 ;
   le vrai site est gachoud-paysagistes.ch. Organique tombe en page 2 (#18, etait #9). Absent du pack.
3. **Jardins Alexandre SA** (Fribourg) - jardins.alexandre@bluewin.ch - Score 62 - Diagnostic
   Beau site (OnPage 96), 30+ ans, 4,7/21. Sort #2 sur sa marque mais absent de "paysagiste Fribourg"
   (pack + page 1). Visibilite limitee au nom.
4. **Lauper SA** (Fribourg) - info@laupersa.ch - Score 64 - Diagnostic
   Tres bon sur la piscine (#4 "pisciniste Fribourg" 880/mois, pages dediees) mais absent sur
   "paysagiste Fribourg" (pack + ~#53 organique). Page d'accueil sans H1. Angle transfert piscine -> jardin.

## LEADS EMAIL secondaires (email present, draft NON redige - profil/priorite)
- **Yves Schafer SA** - info@yves-schafer.ch - commerce de machines de jardin (ICP partiel, retail).
- **JMG-Paysage** - contact@jmg-paysage.ch - petit acteur, site Wix, 5,0/20.
- **Muriset Jean-Louis et Fils SA** - michel.muriset@bluewin.ch - 4,2/24, SEO non approfondi ce run.

## A APPELER - canal BONUS (pas d'email) -> fiche Notion (Diagnostic, pas de mail)
1. **Paysage Equilibre** (Fribourg) - +41 79 362 71 24 - 5,0/23, invisible sur la requete metier.
2. **Les Artisans du Jardin Sarl** (Fribourg) - +41 26 656 06 06 - 47 avis (4,7) mais pas de vrai
   domaine (site sur digitalone.site). Angle creation.

## REJETES -> fiche Notion statut "Ancien"
1. **La Feuille Verte - Ebneter** (Corminboeuf) - deja #2 du pack local, pas d'ecart ; pas d'email.
2. **Frijardin Sarl** (Fribourg) - note 3,5/5 sur 39 avis, trop basse pour une approche a froid.

## Autres collectes non traitees en profondeur (pool)
Ansermet Paysagistes, Evertis SA (info@evertis.ch, mais grosse structure multi-sites), Clement Paysagisme,
Parcs et Jardins Krattinger (3,7), Bull-Jardin (Bulle), Jardins sur Perolles (fleuriste/traiteur),
GM Paysagiste. A reprendre sur un run dedie Bulle/Broye selon rotation.

## Dedup
Base Notion "Contacts" interrogee : les Place ID existants concernaient la Menuiserie (Neuchatel).
Aucun chevauchement avec les paysagistes de Fribourg. Aucun doublon.

## Cout estime du run
- Apify Maps : 2 runs (~0,024 CU).
- Apify contact-scraper : plusieurs passes, dont des essais a vide au depart (~0,25 CU au total).
- DataForSEO : 1 SERP live, 1 volume Ads, ~5 OnPage, ~5 ranked_keywords (~0,04 CHF).
- Total estime : ~0,6 CHF, bien sous le plafond de 10 CHF.

## Incidents / notes pour la prochaine fois
- IMPORTANT : en debut de run, une serie d'appels Apify/DataForSEO a echoue (datasets pas encore prets,
  mauvais format de localisation) et le travail a un moment avance sur des donnees non confirmees. Tout a ete
  repris ensuite sur les donnees reelles ; les fiches Notion ont ete corrigees avant livraison. A surveiller :
  toujours lire le dataset reel (get-dataset-items) avant d'ecrire quoi que ce soit.
- Format localisation DataForSEO Fribourg : utiliser "Fribourg,Switzerland" (canton). "Canton of Fribourg,..."
  et "Fribourg,Canton of Fribourg,Switzerland" sont REJETES.
- Notion : parent = data_source_id "de8f19f7-9e6a-416e-b484-4d1f184a47e2" (collection), pas l'ID de database.
  Secteur : pas d'option "Paysagiste" -> "Artisan". Offre KUMO = "Diagnostic". NPA = nombre.
- Signature mail : pas de numero de telephone de Thomas connu -> signer "Thomas / KUMO - kumo-seo.ch"
  (comme les fiches existantes), ne pas inventer de numero.
- contact-info-scraper : lancer toutes les URLs en un seul run (startUrls multiples, maxDepth 1) est plus
  fiable et moins cher que des runs separes.
