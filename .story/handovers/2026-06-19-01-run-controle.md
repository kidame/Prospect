# Handover — Routine Controle (03:00) — 2026-06-19

## Run summary
- Routine : CONTROLE (seconde lecture qualite), contexte neuf.
- Date : 2026-06-19, ~03:00 Europe/Zurich.
- Perimetre : fiches "Draft pret" coche ET "Controle" vide.

## Fiches controlees : 5 -> toutes 🟠 A voir (0 🟢, 0 🔴)
Segments traites :
- menuisier/ebeniste x Lausanne (run 1h du 2026-06-19) : 4 fiches EMAIL.
- cuisiniste/agencement x Fribourg (run 1h du 2026-06-18) : 1 fiche EMAIL en RATTRAPAGE
  (creee 2026-06-17 ~23:37 UTC, jamais controlee par la run controle du 18 -> ramassee ce soir).

Le reste du run menuisier x Lausanne etait hors perimetre : 1 fiche "a appeler" (pas de mail)
et 5 fiches rejetees (deja #1 organique / B2B / contact non fiable / reputation faible).
Le batch cuisiniste x Fribourg du 06-18 (4 autres fiches) etait deja controle (🟠) le 06-18.

## Defaut dominant : ACCENTS MANQUANTS (C5) sur 5/5 fiches
Toutes 🟠 pour la meme raison : la run de 1h ecrit le corps du mail en ASCII (sans accents),
contre la regle CLAUDE.md "accents obligatoires, prime sur l'ASCII". Salutations (C1), faits
porteurs (C2, re-mesures SERP confirmes), angles (C4) et hygiene (C6) : tous OK.
1 nuance C2 sur une fiche menuisier Lausanne : le mail annonce "2e sur la carte" alors que la
re-mesure du jour la voit #3 du pack (un concurrent ads est remonte #1) -> argument intact
(present carte / absent organique), juste un chiffre a ajuster (pack local volatil). Reste 🟠.

## Issue ouverte
- ISS-002 (severity high) : "emails 1h-run rediges sans accents". Accumulation chiffree sur
  plusieurs nuits/segments (~100% des mails). Changement suggere = forcer la run 1h a produire
  le mail deja accentue (skill writing + garde-fou ROUTINE_PROMPT + self-check avant 'Draft pret').
  A trancher en session dev. NB : issue list etait VIDE en debut de session (cf. soupcon push
  casse des handovers precedents) -> ISS-002 est la 1re issue persistee depuis un moment, verifier
  qu'elle survit au push.

## Cout estime
~1 CHF (2 appels serp_organic_live_advanced mobile : "menuisier lausanne" + "cuisiniste bulle" ;
1 SERP couvrait les 4 fiches Lausanne, 1 pour Bulle. Lecture Notion = ~0).

## Erreurs
Aucune. Les 5 fiches ont recu champ "Controle" = 🟠 + section "## Controle" en bas du corps.

## Pour la session suivante
- Vue Notion "🔍 A trancher (controle)" : 5 nouvelles 🟠 ce matin, toutes = re-accentuer avant envoi
  (+ ajuster "2e->3e" sur la fiche Atelier Art Home menuisier Lausanne).
- Rien de 🔴, rien de "controle incomplet".
- Si ISS-002 ne reapparait pas au prochain `issue list`, le push .story/ est probablement casse.