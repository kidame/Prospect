# Handover — Run CONTROLE (seconde lecture) — 2026-10-16 (~03:00)

## Resume META
- 7 fiches controlees (Draft pret = true ET Controle vide).
  - 3 du segment "electricien x Yverdon / nord vaudois" = RATTRAPAGE (fiches du 2026-08-05 restees sans verdict, routine non passee depuis).
  - 4 du segment "menuisier/ebeniste x Veveyse-Lavaux" = produites par la run 1h de la nuit (2026-10-15 ~23:38).
- Verdicts : 5 🟢 OK / 1 🟠 A voir / 1 🔴 A trancher.

## Detail par verdict (META, zero PII)
- 🔴 (1) : segment menuisier x Veveyse-Lavaux. Fait porteur FAUX : Diagnostic + mail affirment "site absent de l'organique page 1" alors que la re-mesure (serp_organic_live_advanced mobile, meme location, depth 20) montre le domaine de la fiche en #1 organique (rank_absolute 5) + #12. Accroche effondree -> ISS-007 ouverte.
- 🟠 (1) : segment menuisier x Veveyse-Lavaux. Headline "absent du pack local" CONFIRME (solide), mais le detail organique du mail ("concurrent sort en premier / vous arrivez juste derriere dans les liens") non verifiable ce soir (ni le concurrent nomme ni le prospect en page 1 organique -> SERP organique volatil). Suggere a Thomas de verifier/retirer cette phrase avant envoi.
- 🟢 (5) : 3 electricien x Yverdon + 2 menuisier x Veveyse-Lavaux. Faits porteurs re-mesures et confirmes (absences pack/organique conformes). Salutations neutres. Alertes "⚠️ Email a confirmer" bien presentes sur les 3 fiches a email incertain (generique/domaine!=site/hotmail). Signatures conformes (078 939 81 00).

## Observations systeme
- Mutualisation des re-mesures : 1 SERP "electricien yverdon" couvre les 3 electriciens ; 1 SERP "menuisier vevey" couvre 2 menuisiers ; + "menuisier attalens" + "menuisier chatel-st-denis". 4 SERP + 4 serp_locations.
- Le defaut 🔴 (absence organique ecrite alors que present #1) est le MEME pattern que le cas 2026-07-21 deja cite dans CLAUDE.md -> ISS-007 propose une verification deterministe cote run 1h (comparer items[].domain au domaine fiche avant d'ecrire "absent"), symetrique de la regle accents L-008.
- Rappel ISS-005 (photo count = Avis Google) non re-verifiable au controle (on re-mesure la SERP, pas les compteurs GBP) : non evalue ce soir.

## Cout estime
~1-2 CHF (8 appels DataForSEO : 4 SERP live + 4 serp_locations ; serp_locations quasi gratuit). Sous plafond.

## Issue ouverte cette nuit
- ISS-007 (high) : "site absent de l'organique" faux par la run 1h alors que present #1 page 1.

## Suivi
- Rien a collecter (run de controle). Les fiches 🟠/🔴 remontent dans la vue Notion "A trancher (controle)" pour Thomas au reveil.