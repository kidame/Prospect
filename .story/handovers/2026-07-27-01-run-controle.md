# Controle 2026-07-27 — segment menuisier/ebeniste x Geneve

**TL;DR** — 4 fiches EMAIL controlees (run de 1h du 2026-07-25, ramassees ce controle). Verdict : 0 🟢 / 3 🟠 A voir / 1 🔴 A trancher. Deux patterns ouverts en issues (ISS-004 high, ISS-005 medium).

## Perimetre
- Vue Notion "⏳ Non controlees" (Draft pret = vrai ET Controle vide) : 4 fiches, toutes canal EMAIL, meme segment menuisier/ebeniste x Geneve. Aucune fiche "a appeler" en attente. Champ "Controle" deja en place (pas de setup a faire).

## Methode / cout
- 5 re-mesures serp_organic_live_advanced (mobile) : "menuisier Geneve" x3 points (Geneva-city, Vernier, Lancy) + "ebeniste Geneve" (Geneva-city) + 1 serp_locations. Le multi-point etait necessaire : le pack local Geneve est tres proximite-dependant (3 packs disjoints selon la commune). Cout estime <0,1 CHF, tres sous plafond.

## Resultat des 6 controles
- 3 🟠 A voir : les 3 fiches ou le SEUL defaut est C5 (mail entierement SANS accents). Faits porteurs re-mesures et confirmes depuis la commune du prospect : Concept&Bois (Vernier) #1 pack confirme depuis Vernier ; Kimmeier (Vernier) absent + concurrent Concept&Bois #1 confirme depuis Vernier ; AF Agencement (Carouge) present pack #2 sur "ebeniste" et absent "menuisier" sur les 2 axes confirme. Salutations neutres OK, alerte email hotmail presente sur Kimmeier, emails de domaine confirmes sur les autres.
- 1 🔴 A trancher : Colaizzi (Lancy). L'accroche nomme "Concept&Bois et J. Farina sur la carte" pour "menuisier Geneve", mais depuis Lancy (commune du prospect) le pack = menuisier-geneve.com / Aliance / BNBOIS -> aucun des deux noms. L'invisibilite de Colaizzi (fond de l'argument) est, elle, confirmee sur les 3 points. -> recadrer les noms ou mener sur l'absence organique.

## Defaut dominant + issues ouvertes
- ISS-005 (medium) : 4/4 mails de la nuit rediges SANS accents (viole CLAUDE.md). Defaut d'hygiene rattrapable au copier-coller, mais systematique -> a corriger a la source (skill writing / ROUTINE_PROMPT etape 9).
- ISS-004 (high) : concurrent nomme (pack local) faux depuis la COMMUNE du prospect. 2e occurrence du pattern deja "a surveiller" au handover run-controle 2026-06-10 (carreleur x Geneve). Le pack local Geneve varie par commune -> imposer la re-verif du concurrent nomme avec le location de la commune du prospect, ou basculer sur l'absence organique.

## Prochain controle
- Rien en attente (has_more:false). Si la 1h renvoie encore un segment Geneve avec angle "concurrent nomme", verifier en priorite la coherence nom-cite / pack-depuis-la-commune (cf. ISS-004) et la presence des accents (cf. ISS-005).
