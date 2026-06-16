# Handover — Routine CONTROLE (03:00) — 2026-06-16

## Run summary
- Routine : CONTROLE (seconde lecture qualite), contexte neuf.
- Date : 2026-06-16
- Fiches ramassees (Draft pret = vrai ET Controle vide) : 3 (canal EMAIL).
- Segment de la nuit (run-1h source) : menuisier/ebeniste x Lausanne.

## Verdicts
- 🟢 OK : 0
- 🟠 A voir : 1
- 🔴 A trancher : 2

Detail (refs segment, zero PII) :
- 🟠 A voir : Saint-Prex/Morges. Fait porteur reconfirme au SERP (pack top-3 + 2 concurrents avec page de zone dediee, prospect absent). Seul defaut : mail sans accents.
- 🔴 A trancher : Lutry/Lausanne. Re-mesure "menuisier Lausanne" -> prospect ABSENT de la page 1 organique, alors que le mail affirme "bien en premiere page, tout en bas" (coherent avec signal is_down ; probablement glisse en page 2). + accents.
- 🔴 A trancher : Lausanne. Re-mesure "menuisier Lausanne" -> prospect est #2 du pack local (DANS le top-3), alors que le mail dit "les trois premieres passent devant vous". Accroche inversee par la mesure. + accents.

## Defaut dominant de la nuit
ACCENTS MANQUANTS dans 3/3 mails (ASCII complet). Confirme non-artefact (le schema Notion et DataForSEO renvoient bien les accents). -> issue ISS-002 ouverte (medium). Regle CLAUDE.md "ACCENTS OBLIGATOIRES" non respectee par la run-1h.

Note systeme : les 2 🔴 viennent d'une volatilite SERP/pack entre la mesure run-1h (01h33) et le controle (~04h30) sur des accroches baties pile a la frontiere (page1/page2, bord du 3-pack). Le controle joue son role : il attrape les accroches sans marge. Pas une issue distincte (volatilite inherente), juste a garder en tete : eviter de batir une accroche sur une position frontiere instable.

## Hors perimetre (non controlees)
4 fiches du meme run sans draft : 1 "A APPELER" (pas d'email) + 3 rejetees (Statut Ancien). Conforme.

## Cout estime
~0,15 CHF (2 re-mesures SERP DataForSEO couvrant les 3 fiches ; 2 requetes coeur partagees).

## Erreurs
Aucune. Champ "Controle" deja en place (3 options). Toutes les ecritures Notion ont abouti.

## Storybloq
- Issue list etait VIDE au demarrage (cf. handovers precedents : suspicion de push casse recurrent T-007/ISS-002 mentionnee). ISS-002 creee cette nuit (accents). A verifier que le push aboutit.
