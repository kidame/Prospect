# Run prospection KUMO - 2026-06-01

## Couple (secteur, zone) de ce run
- **Secteur : Fiduciaire / comptabilite** (option Notion la plus proche : "Autre")
- **Zone : Yverdon-les-Bains** (ville voisine majeure de reference : Lausanne)
- Rotation : les runs precedents couvraient le batiment / jardin / bois (paysagistes,
  menuiserie, ebenisterie, charpente) autour de Fribourg / Neuchatel. Nouveau secteur ET
  nouvelle zone ce run. Ne pas reprendre fiduciaire+Yverdon la nuit prochaine.

## Marche mesure (DataForSEO, fr, location Yverdon-les-Bains / Vaud)
- "fiduciaire yverdon" = 260/mois (pic 480 en mars, saison fiscale ; quart bas l'ete)
- "fiduciaire yverdon-les-bains" = 50/mois
- "comptable yverdon" = 10/mois
- "impots yverdon" / "impot yverdon" = 720/mois chacun (forte demande, peu captee par les locaux)
- "fiduciaire lausanne" (voisin majeur) = 1000/mois (~4x Yverdon)
- "comptable lausanne" = 70/mois
- "fiduciaire" (national) = 3600/mois
- SERP coeur "fiduciaire yverdon" (mobile) : pack local = Synergie Fiduciaire, Fiduciaire
  Jeremie Lecoultre, Fidaceb. Organique p.1 sature d'annuaires (search.ch, local.ch,
  entreprisesdelaregion) et de nationales (In Extenso, Findea, Magic Heidi).

## RETENUS canal EMAIL (4) - fiches Notion avec Diagnostic + mail pret + bouton mailto
1. **EDEN Fiduciaire (Gilles-E. Tissot)** - edenfid.ch - get@edenfid.ch - Score 82 - Diagnostic
   Absent pack + 0 mot-cle organique malgre 9 avis 5,0 et site sain (OnPage 90). Besoin le + fort.
2. **Texfid (Troilo)** - texfid.ch - info@texfid.ch - Score 80 - Diagnostic
   ~15 requetes indexees mais TOUTES en page 2+ ("impots yverdon" 720/mois #19-25), absent pack.
3. **Fidu-8 Sarl (Olivier Corciulo)** - fidu-8.ch - info@fidu-8.ch - Score 74 - Diagnostic
   Organique page 2 (#12) sur le coeur, absent pack, etendue d'un seul mot-cle.
4. **Fiduciaire Fidaceb SA** - fidaceb.ch - info@fidaceb.ch - Score 68 - Diagnostic
   Present pack #3 + organique p.1 sur le coeur mais etendue tres etroite (3 mots-cles).
   Angle croissance. Confiance budget elevee (experts-reviseurs ASR, 1012 backlinks).

## A APPELER canal BONUS (3) - fiche Notion + Diagnostic, pas de mail
- **Synergie Fiduciaire Yverdon** - +41 24 426 07 08 - synergie-fiduciaire.ch
  Pack local #1 (4,7/25 avis) mais site absent de l'organique p.1. Meilleur lead a appeler.
- **FIDUVAUD** - +41 79 214 71 07 (mobile) - fiduvaud.ch
  5,0/7 avis, absent pack + organique. Analyse legere.
- **Chrystalle SA** - +41 24 588 02 08 - chrystalle.ch
  5,0/6 avis, absent pack + organique. Analyse legere.

## REJETES (resume)
- **Fiduciaire Jeremie Lecoultre** (fiche Notion creee, statut Ancien) : deja present pack #2
  + organique #10 page 1 sur le coeur. Besoin trop faible.
- Reseaux / franchises nationales (exclusion dure, non fichees) : In Extenso (groupefidexpert.ch),
  Fiduconsult Fidyver, BfB Fidam (succursale), FlexPME (succursale), Sageco (multi-bureaux
  Lausanne/Yverdon), Epsitec/Cresus (editeur logiciel, hors cible).
- Faible signal / placeholder : Y-Fiduciaire (site builder digitalone.site), Muller Christe,
  Daniel Heiz, Gonin Conseils (yellow.local.ch), Marc-Etienne Hefti (digitalone.site),
  AGL Fiduciaire & Immobilier (3,7/4, mix immobilier/assurance), et autres fiches a 0-1 avis
  sans email ni angle clair (Aplika, FiduDom, von Arx, fidufacile, Fidulon, Locasser, MNJ,
  Deskmachine, Fidarc, NNcompta, LP Compta, OC Fiduciaire dont l'email pointe vers une agence
  tierce youriste.com, Jurafisc, Fiduciaire BFC, Fiscaplan...). Conserves hors base ce run ;
  re-evaluables sur demande.

## Outils / cout estime
- Apify enckay/google-maps-places-extractor : 2 runs (minReviews 4 puis 0+keyword elargi),
  ~0,024 CU au total. Contacts + emails site extraits en meme passe (pas de run scraper separe).
- DataForSEO : serp_locations (1), kw_data search_volume (8 mots-cles), serp_organic_live_advanced
  (1, mobile, depth 30), on_page_instant_pages (5), ranked_keywords (4).
- WebFetch : 4 (pages reelles + dirigeants).
- Cout estime total du run : < 1 CHF (largement sous le plafond ~10 CHF/nuit).

## Erreurs / notes
- Aucune erreur d'outil. EDEN ranked_keywords = 0 resultat (confirme l'absence organique, pas une erreur).
- Salutations : EDEN -> "Monsieur Tissot" (2 dirigeants Tissot, nom de famille sur) ;
  Fidu-8 -> "Monsieur Corciulo" (responsable unique confirme) ; Texfid (Sandra+Paolo Troilo)
  et Fidaceb (Glauser+Richardet) -> "Bonjour," neutre (deux noms). Emails tous sur domaine
  officiel concordant -> aucune alerte "a confirmer".
- LCP mobile laisse vide (regle LCP). dom_complete utilise comme proxy dans les Notes.
- Drafts non crees dans Gmail (execution nocturne) : mails finalises dans le corps Notion,
  "Draft pret" coche. Thomas copie-colle / clique le bouton mailto au reveil.
