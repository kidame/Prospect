# Installation de Storybloq sur le repo prospect

**TL;DR** — Storybloq installe et rapatrie dans le repo (skill `/story`, MCP via npx auto-amorce, hooks projet). Roadmap (Vagues A/B + controle + outillage), 5 lecons data-2026-06, 6 tickets seedes. `.story/` = memoire du META-travail, JAMAIS les donnees prospect (Notion).

## Ce qui a ete fait
- `storybloq init` avait deja ete lance par une session anterieure (config.json + roadmap p0), mais `setup` jamais termine. Setup complete cette session.
- Skill `/story` copie dans `.claude/skills/story/` (committe -> survit au conteneur ephemere + dispo en session web).
- MCP `storybloq` ajoute a `.mcp.json` via `npx -y @storybloq/storybloq@1.4.4 --mcp` (auto-amorce, pas d'install global a maintenir).
- Hooks projet dans `.claude/settings.json` : PreCompact (snapshot avant compaction) + SessionStart/compact (recap). En npx. Le hook Stop (status.json pour l'app Mac) a ete volontairement OMIS (overhead inutile en cloud).
- Roadmap : phases `p0` -> `vague-a` (actuel) -> `vague-b` -> `controle` -> `outillage`.
- 5 lecons (faits valides data 2026-06 deja dans CLAUDE.md) : piliers, batiment=pire population email, niches mortes, pas de draft Gmail en routine, OnPage != visible.
- 6 tickets (T-001..T-006), surtout Vague B (filtre dur >=1 signal, cadence/re-contact, croisement signaux x conversion) + outillage (zefix, cout/run) + controle.
- Note ajoutee a CLAUDE.md (section "Storybloq") avec la FRONTIERE : aucune donnee prospect dans .story.

## Pourquoi npx et tout-dans-le-repo
Conteneur cloud ephemere + routines nocturnes : un `npm install -g` ne survit pas et le chemin binaire absolu ecrit par `setup` (`/opt/node22/bin/storybloq`) disparait. Tout ce qui doit persister est committe (skill, .mcp.json, settings.json, .story/) et l'execution passe par npx pinne sur 1.4.4.

## A TRANCHER (decision de Thomas)
Licence Storybloq = **PolyForm Noncommercial 1.0.0**. KUMO est une activite commerciale. Utiliser Storybloq pour outiller le repo qui fait tourner la prospection commerciale peut sortir du cadre "noncommercial". A clarifier (contact mainteneur pour licence commerciale) avant de s'appuyer dessus durablement.

## Suite
- Brancher le travail Vague B sur les tickets T-001..T-003.
- `storybloq ticket next` pour la prochaine action.
