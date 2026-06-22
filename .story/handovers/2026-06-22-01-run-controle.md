# Controle qualite 2026-06-22 (03:00) — 5 fiches controlees (demenageur x Lausanne)

**TL;DR** — Rattrapage du batch "demenageur x Lausanne" (cree nuit 06-19->06-20) que le controle de la nuit 06-20 n'avait pas traite : 5 fiches a draft EMAIL controlees, 5x 🟠 A voir. Defaut dominant unique : CTA "15 min au telephone" sur 5/5 mails (viole la regle CLAUDE.md 2026-06-20 "CTA = continuer par mail"). C1/C2/C5/C6 OK partout, accents presents (pas le defaut ASCII des anciens batches). Issue ISS-002 ouverte. Cout < 0,5 CHF (1 serp_locations + 1 SERP mutualisee).

## Compteurs
- Fiches controlees cette nuit : 5 / 5 avec draft EMAIL non encore controle.
- Verdicts : 0 🟢 · 5 🟠 · 0 🔴.
- Segment : demenageur x Lausanne (Master Demenagement, Monachon, VSR, Qualidem, DMD Transport).
- Cout : ~0,4 CHF (1 serp_organic_live_advanced "demenagement Lausanne" mobile, mutualisee pour les 5 ; 1 serp_locations). Sous plafond.

## Methode (1 SERP pour 5)
Les 5 fiches partagent la requete coeur "demenagement Lausanne" -> 1 seule re-mesure (mobile, Lausanne, 2026-06-22) a couvert C2 des 5 :
- Pack local = DS.Demenagement / La Romande / Le Petit Demenageur. Conforme aux 5 fiches (chacune se dit absente du pack -> exact).
- Organique : Master Transport (demenagementlausanne.ch) PRESENT #3 web (conforme "present web / absent carte") ; Monachon / VSR / Qualidem / DMD absents du top 10 (DMD seulement cite dans l'annuaire ofri.ch, conforme au Diagnostic). Tous C2 conformes.

## Defaut dominant -> ISS-002 (medium)
- CTA "15 minutes au telephone" sur 5/5 mails alors que CLAUDE.md (2026-06-20) impose un CTA par mail au 1er contact. Seul point a corriger (sinon mails propres). Nuance : generes ~01h33 le 06-20, peut-etre juste avant la regle -> dev a verifier si ROUTINE_PROMPT/skill writing portent deja l'interdiction.

## Observation systeme (pas une issue de plus)
- Le controle TOURNE mais ne PERSISTE pas ses handovers : aucun handover run-controle entre le 06-14 et aujourd'hui, alors que les batches 06-16 / 06-18 / 06-19 portent bien des verdicts ecrits dans les fiches (controle effectif). + `issue list --status open` etait VIDE en debut de session. Forte presomption de push casse recurrent (cf. T-007 deja suspecte dans les handovers anterieurs). Le batch 06-20 (demenageur) etait reste SANS verdict : soit le controle 06-20 n'a pas tourne, soit il est mort avant d'ecrire -> c'est ce trou que cette session a rattrape.

## Prochain controle
- Surveiller : (1) CTA telephone tant qu'ISS-002 non corrige a la source ; (2) reapparition du defaut accents (ASCII) sur les nouveaux batches. Aucune fiche neuve creee les nuits 06-20/06-21/06-22 (run-1h sans output ou mort) -> si la 1h reprend, les nouveaux drafts apparaitront en "Non controlees".
