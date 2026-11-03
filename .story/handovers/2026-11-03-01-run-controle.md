# Handover — Run CONTROLE (03:00) — 2026-11-03 (Europe/Zurich)

## Resume
- Seconde lecture des fiches "Draft pret" sans verdict. Perimetre : les 5 fiches EMAIL du run 1h de cette nuit, segment **peintre x Lausanne** (couple suggere par le handover 10-30, confirme frais). Rattrapage : 0 fiche en retard.
- Fiches controlees : **5**. Verdicts : **0 🟢 / 3 🟠 A voir / 2 🔴 A trancher**.

## Verdicts (meta, refs par Place ID)
- 🟠 x3 (0x478c2f053aa632f3:0x6891c713e21a8040 ; 0x478e9d5acb873853:0xc1877e4ed8c50765 ; 0x478c6f19ed51184d:0x8e6ee21dc12b4cfd) : fait porteur SOLIDE (absence pack + absence/enfouissement organique re-mesures et confirmes, accroche ne nommant que le trio du pack = confirme), MAIS corps en ASCII -> seule correction = ré-accentuer. Alertes "email a confirmer" presentes quand l'adresse etait incertaine.
- 🔴 x2 (0x478c31a02b9202db:0x2ce77535023cf047 ; 0x478c2f065e4e54c3:0x6309aa924ddf8304) : accroche nomme des concurrents ("lausanne-peintre", "BS Peinture") comme ce que le prospect trouve en tete de "peinture lausanne", mais re-mesure p1 = bio-construct #1 + superprof/comparis/yoojo/socol ; NI l'un NI l'autre en page 1 -> accroche falsifiable par le prospect. Un des deux est EN PLUS present en page 1 organique (#8) sur la requete soeur "peintre lausanne" alors que le mail le dit "page 4". Absence propre du prospect = vraie ; c'est le concurrent nomme + le cadrage qui divergent. Signale aux deux fiches.

## Re-mesures C2 (serp_organic_live_advanced, mobile, "Lausanne,Vaud,Switzerland")
- "peintre lausanne" : pack = Gaetano / Vernay / Diday (conforme a l'etiquette du run 1h). Organique p1 = artisanlocal, didaypeinture, jobup, superprof, bio-construct, yoojo, PROPEINTURE (#8 organique = p1), starofservice, gamboni.
- "peinture lausanne" : pack = Colore Box / Classidur Jallut / Vernay ; organique p1 #1 = bio-construct, puis superprof, comparis, artiloft, yoojo, socol, apprentus, reddit. ABSENTS de la p1 : "lausanne-peintre.ch" et "BS Peinture" (que 2 mails nomment comme concurrents en tete). "lausanne-peintre.ch" ressemble a une confusion du run 1h avec peintrelausanne.ch (= Gaetano, #1 du PACK, pas organique).

## Defaut dominant + issue
- Defaut MATERIEL dominant : corps de mail livres en ASCII (zero accent) sur les 5/5 fiches, malgre le verrou deterministe (regression totale vs 10-30 ou accents conformes). Famille L-008 / recidive 07-21. Ouvert : **ISS-009** (high) -> rendre le verrou accents vraiment bloquant/mecanique (decision session dev).
- Defaut secondaire (2 fiches, 1 nuit) : concurrent organique NOMME dans l'accroche non confirme par la re-mesure (accroche falsifiable). Pas d'issue (isole ce run) ; a surveiller comme voisin de ISS-008 (invisibilite/fait porteur affirme sans verif SERP cote concurrent).

## Cout estime
~0.06-0.1 CHF (1 serp_locations + 2 serp_organic_live_advanced mobile ; aucun OnPage/ranked_keywords). Sous plafond ~1-2 CHF.

## Perimetre respecte
Lecture seule sur les fiches : ecrit uniquement le champ "Controle" + la section "## Controle" de chaque fiche. Aucun mail / Diagnostic / autre champ touche. Aucun brouillon, aucun mail envoye.
