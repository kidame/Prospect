# Instauration du handover comme boucle de continuite des routines

**TL;DR** — Le handover (fonction phare Storybloq) est maintenant instaure dans les DEUX routines, pas seulement les sessions dev. Chaque run lit `handover latest --count 3` au debut et ecrit `snapshot` + `handover create` a la fin. Gain cle : la memoire de ROTATION (couple metier x zone deja couvert) devient PERSISTANTE (handover versionne/pousse) au lieu d'etre perdue dans `_resume.md` gitignore.

## Boucle canonique adoptee (ref reference.md)
- Debut de session : `handover latest --count 3` + `status` + `issue list --status open`.
- Fin de session : `snapshot` PUIS `handover create`.
- Append-only : jamais reecrire un handover.

## Branchements
- ROUTINE_PROMPT.md : etape 1 lit les handovers (rotation) ; etape 2 s'appuie dessus pour ne pas refaire un couple ; etape 10 = snapshot + handover (TOUJOURS, slug run-1h) + issue (conditionnelle) + un seul push.
- CONTROLE_PROMPT.md : section memoire = lit handover latest au debut ; fin = snapshot + handover (slug run-controle) + issue conditionnelle + push.
- CLAUDE.md : nouvelle sous-section HANDOVER (boucle + niveau META + append-only) ; regle de rotation pointee sur les handovers et non `_resume.md`.

## Frontiere respectee
Handover des routines = META seulement (segment, compteurs, cout, prochain segment). Aucun detail prospect (Notion reste la source).

## Reste a faire / valider
- T-007 : 1er run reel (CLI/push). Verifier que les handovers run-1h / run-controle apparaissent bien sur main et que la rotation s'appuie dessus.
- Modele final : ISSUES (signalements) + HANDOVERS (continuite) cote routines ; LECONS + TICKETS cote dev (assimilation).
