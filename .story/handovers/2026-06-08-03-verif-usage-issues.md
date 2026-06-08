# Verification de l'usage Storybloq + passage notes -> issues

**TL;DR** — Audit de conformite a la doc Storybloq (SKILL.md v1.4.4). 1 bug corrige (binaire CLI absent dans les conteneurs de routine -> hook SessionStart npm install -g). 1 changement de fond valide avec Thomas : les routines ouvrent desormais des ISSUES (et non des notes) -> conforme a la semantique "probleme decouvert = issue" ET ca remonte tout seul dans /story.

## Conformite verifiee
- OK : init/setup, lecons (usage + reinforce), handovers append-only, roadmap/phases/tickets, gitignore (tout sauf snapshots/).
- CORRIGE : les prompts appelaient `storybloq` en commande nue mais rien ne l'installait dans un conteneur frais (MCP/hooks via npx n'ajoutent rien au PATH). Ajout d'un hook SessionStart `npm install -g @storybloq/storybloq@1.4.4` -> conforme a la doc ("use npm -g, never npx, for the CLI"). MCP reste npx (anti-course au demarrage).
- ECARTS ASSUMES : npx sur MCP/hooks (conteneur ephemere + Stop hook retire) ; version pinnee 1.4.4 (repro automatisee).

## Changement notes -> issues
Raison : la doc classe les "problemes decouverts pendant le travail" en ISSUES (severite/impact), et surtout les issues remontent dans `/story` (table Open Issues + recommend) alors que les notes sont une boite cachee (`note list`). Plus correct ET plus facile a reviser.
- Routine 1h : `issue create --title "Amelioration: ..." --severity low/medium/high --components routine-1h <theme> --location <regle> --impact --stdin <corps>`.
- Routine controle : idem avec `--components routine-controle`, severite high si ca casse un mail envoyable.
- Dedup : `issue list --status open` avant, sinon `issue update`.
- Assimilation (session dev) : promotion en lesson/ticket puis `issue update <id> --status resolved --resolution ...`.
- Fichiers modifies : CLAUDE.md (section Storybloq reecrite), ROUTINE_PROMPT.md (etape 10), CONTROLE_PROMPT.md (section memoire).

## Reste a faire
- T-007 : valider au 1er run reel (npx/CLI joignables, push main OK).
- Note : le handover precedent (self-improve-loop) decrit le modele NOTES, desormais remplace par ISSUES -- garde pour l'historique (handovers append-only).
