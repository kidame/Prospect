# Boucle d'auto-amelioration : les routines alimentent Storybloq

**TL;DR** — Les deux routines nocturnes (1h prospection, 3h controle) deposent desormais des NOTES-propositions d'amelioration dans `.story/` et les poussent sur main. Thomas les promeut en lecons/tickets en session dev. La memoire durable n'est jamais ecrite par une routine -> pas de pollution.

## Decision (validee avec Thomas)
- Curation : routines = ecrivent des NOTES (propositions detaillees) quand un pattern emerge de l'accumulation, PAS chaque nuit. Thomas distille en lecons/tickets via /story en session dev.
- Persistance : push sur **main**, mais confine a `.story/` (jamais `-A`) et aux NOTES seulement -> le pire cas est une note bancale dans une boite de reception curee, jamais une corruption du code/prompts ni une fuite PII.
- Concurrence : `git pull --rebase origin main` avant push (les 2 routines partagent .story/, tournent a 2h d'ecart).
- Frontiere PII : apprentissages sur le SYSTEME dans Storybloq ; donnees prospect dans Notion ; references par Place ID/segment, jamais nom/email/tel.

## Fichiers modifies
- CLAUDE.md : section Storybloq reecrite (qui-ecrit-quoi, persistance, format note, frontiere PII).
- ROUTINE_PROMPT.md : etape 10 (memoire Storybloq).
- CONTROLE_PROMPT.md : section "Memoire Storybloq" (le controle est le meilleur detecteur d'erreurs recurrentes).

## Risques ouverts (ticket dedie, phase outillage)
- npx joignable depuis l'env routine ? push main autorise (branche protegee) ? -> a verifier au 1er run reel. Fallback push : branche `storybloq-memory`.

## Suite
- Apres quelques nuits : faire une session /story, lire `storybloq note list` (tag proposition), promouvoir les recurrentes en lecons/tickets.
