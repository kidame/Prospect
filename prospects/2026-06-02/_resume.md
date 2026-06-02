# Run prospection KUMO - 2026-06-02

**Couple (secteur, zone) du run** : Beaute / bien-etre (instituts de beaute, onglerie, massage, bien-etre) -- Yverdon-les-Bains (Vaud). Ville voisine majeure de comparaison : Lausanne.

**Rotation** : les runs precedents (31/05 -> 02/06) ont couvert paysagistes/jardins (Fribourg), fiduciaires (Yverdon), immobilier (Neuchatel), menuiserie. Ce run change nettement de secteur (beaute/bien-etre, jamais traite) tout en restant sur une zone prioritaire peu chargee cote beaute.

## Marche mesure (DataForSEO, Yverdon-les-Bains / Vaud, fr)
- massage Yverdon = 720/mois (le plus gros), onglerie/ongles Yverdon = 390/mois, institut de beaute Yverdon = 140/mois, epilation Yverdon = 70/mois, hypnose Yverdon = 170/mois, maquillage permanent Yverdon = 20/mois.
- Ville voisine Lausanne : massage Lausanne = 3600/mois, institut de beaute Lausanne = 390/mois, epilation Lausanne = 320/mois.

## Collecte
- Apify enckay/google-maps-places-extractor : keyword "institut de beaute", location Yverdon-les-Bains, minReviews 15, fermes exclus, contacts + emails site. 25 etablissements.
- Pre-filtre : retire les fiches sans vrai site propre (Salonkee, Instagram, yellow.local.ch, spa.center.ivof.com) et hors cible. ~12 finalistes analyses.
- Dedup Notion : aucune entree beaute/bien-etre prealable a Yverdon (base = fiduciaires + menuiseries). Tous les Place ID sont neufs.

## RETENUS - canal EMAIL (4)
1. **Koram - Stephane Maillefer** (koram.ch) - massage + kinesiologie. Pack local absent + page massage Yverdon (720/mois) en position 57 (page 6) malgre 21 avis 5,0 et OnPage 97. Page existe mais ne ranke pas. Offre : Diagnostic. Email info@koram.ch (fiable). Salutation "Bonjour Stephane" (dirigeant confirme).
2. **MaylyBe Beauty** (maylybebeauty.ch) - maquillage + coiffure. 70 avis 5,0 mais 0 mot-cle positionne, site une page sans title ni meta. Absent 2 axes. Offre : Refonte/Creation. Email contact@maylybebeauty.ch (fiable). Salutation neutre.
3. **BodyLooking** (bodylooking.swiss) - onglerie/tattoo/piercing. 159 avis 4,8 mais ongle(s) Yverdon (390/mois) en page 2-3 + absent pack ; fort piercing (#8). Offre : Diagnostic. Email info@bodylooking.com A CONFIRMER (domaine .com vs site .swiss). Salutation neutre.
4. **Rebout'Hyp** (rebouthyp.com) - reboutement + hypnose. 36 avis 5,0 mais hypnose Yverdon (170/mois) en position 56 + absent massage Yverdon (720/mois). 2 backlinks. Offre : Diagnostic. Email rebouthyp@bluewin.ch A CONFIRMER (bluewin perso). Salutation neutre.

Diagnostic + email complet (objet + corps + signature + bouton mailto) ecrits dans le corps de chaque fiche Notion. "Draft pret" coche. Aucun draft Gmail cree (revue manuelle de Thomas).

## A APPELER - canal BONUS (3, pas d'email)
- **Elodie Capraro Nail Designer** (+41 79 881 69 43) : pack local #2 onglerie, 58 avis 5,0, mais AUCUN site (Instagram). Angle : bien dans la carte, invisible en organique. Offre Creation.
- **Lotus Thai Massage** (+41 77 940 48 16) : 92 avis 4,9, aucun site propre (local.ch). Absent organique massage Yverdon 720/mois. Offre Creation.
- **Au fil d'Orient** (+41 78 915 49 45) : 30 avis 4,8, aucun site propre (Salonkee/OneDoc). Offre Creation.

## REJETES analyses (5, statut Ancien en base)
- **Kanjana massage thai** : deja present pack #2 + organique #9 sur massage Yverdon -> besoin faible (a un email).
- **Institut Beaute d'Or** : pack #1 + organique present (pages dediees rankent) -> besoin faible.
- **Institut Diva (Maria Ilardo)** : pack #2 + organique present -> besoin faible.
- **QIPAO** : chaine multi-salons deja visible organique -> hors coeur PME locale.
- **BODYWIN** : profil centre fitness (Lagree, cours collectifs) -> hors coeur ICP beaute (a un email).

Autres fiches vues mais ecartees au pre-filtre gratuit (pas de site propre / aggregateur seul, non fichees individuellement) : Make Me Beautiful, Catarina Nails, L'Onglerie Manoli, Nails by Dy, AP Beauty Salon, Edition Marine, Creation Beaute, Poudre d'argent, Sophie maquillage permanent Orphee, School And Shop Orpheus, Bulle Hair and Spa, Bibi Coiffure, Koram (retenu), Edition Marine. (Reapparaitront filtrees a un futur run beaute/Yverdon.)

## Cout estime du run
- Apify Maps : ~0.03 CU (~0.02 CHF).
- DataForSEO : 1 kw volume, 3 SERP live advanced, 5 ranked_keywords, 4 OnPage instant, 1 serp_locations -> ~0.10-0.15 CHF.
- Total estime < 0.20 CHF. Tres en dessous du plafond de 10 CHF/nuit.

## Erreurs / limites
- Emails BodyLooking et Rebout'Hyp marques "a confirmer" (domaine .com vs .swiss ; adresse bluewin perso). Alerte ecrite en tete du bloc email Notion.
- Recap envoye a hello.puglisi@gmail.com (brouillon Gmail ; aucun envoi automatique).
