# Handover — Run CONTROLE (03:00) — 2026-10-26 (Europe/Zurich)

## Resume
- Routine de controle (seconde lecture), contexte neuf. Fiches ramassees (Draft pret = oui ET Controle vide) : 3, toutes du segment **menuisier/ebeniste x Lausanne** (run 1h de cette nuit).
- Verdicts : 0 🟢 OK / 2 🟠 A voir / 1 🔴 A trancher.

## Detail (meta, refs par Place ID)
- 1 🔴 (Place ID 0x478c31967877f07b:0xa940594201416483) : fait porteur C2 diverge. Le mail (objet + corps) ancre l'accroche sur "vous etes en DEUXIEME page sur 'volet'" (Diagnostic : #23). Re-mesure independante "volet" (mobile, Lausanne) -> le domaine ressort en PAGE 1 (8e organique, page produit /volet-battant/). L'ecart traverse la frontiere page1/page2 -> change l'argument (accroche falsifiable par le prospect). NB : "volet" est un terme mirage (SERP = Groupe Volet SA + Wikipedia/Larousse) ; sur "porte de garage", 2e terme du mail, re-mesure OK (hors page 1, conforme #33).
- 2 🟠 (Place ID 0x478c379cfb9d73af:0x2571917b6fce47af et 0x478c2daa4140dd1d:0xd56511769b21c334) : C2/C4 CONFIRMES par re-mesure "menuisier lausanne" (mobile, Lausanne). Pack local = N&J Interieurs / L'Atelier Bois / K-Hut (les 2 prospects absents). Organique p1 : BEM (page dediee /menuiserie-a-cheseaux-sur-lausanne/) present #6 abs ; les 2 prospects absents de l'organique p1. Salutations neutres, signatures conformes (078 939 81 00), C6 OK (emails domaine, fiables). Seul point : C5-accents.

## Defaut dominant de la nuit
- C5-accents : 3/3 fiches ont le corps de mail en ASCII pur (zero accent) alors que CLAUDE.md impose le check deterministe accents AVANT ecriture Notion. Defaut historique (L-008 + recidive 2026-07-21). -> Issue ouverte ISS-007 (severity medium).
- Fait porteur diverge (C2) : 1 fiche cette nuit (mecanisme = position sur terme generique/mirage traversant la frontiere page1/2), different du 🔴 de la nuit 10-23 (mauvaise lecture du pack local). Pas encore un pattern unique recurrent -> pas d'issue dediee, a surveiller.

## Cout estime
~0,8-1,0 CHF. DataForSEO : 1 serp_locations + 3 serp_organic_live_advanced ("menuisier lausanne" mutualise pour les 2 fiches 🟠, "volet" + "porte de garage" pour la fiche 🔴). Notion : lectures + 9 ecritures (3 champs Controle + 3 sections ## Controle, chacune en 2 appels). Sous plafond (~1-2 CHF).

## Observations systeme
- Mutualisation reussie sur "menuisier lausanne" (requete coeur commune aux 2 fiches 🟠) -> 1 seule re-mesure pour C2 des deux.
- SQL Notion a fonctionne (pas de gating Business ce run ; ISS-003 reste intermittent).
- Rappel fiabilite du "fait porteur" sur termes generiques/mirage : "volet" est un terme navigationnel domine par une marque homonyme (Groupe Volet SA) ; mesurer un rang sur ce type de terme est volatil et peu vendeur -> la run 1h devrait preferer des requetes "metier + ville" ou "prestation + ville" comme fait porteur, pas un terme generique mononym.

## Issue ouverte ce run
- ISS-007 (medium) : mails ASCII sans accents, 3/3 cette nuit + historique L-008/2026-07-21.