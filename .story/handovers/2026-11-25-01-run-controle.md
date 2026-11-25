# Handover - Run controle - 2026-11-25 (Europe/Zurich), sprint jour 2

## Resume
- 20 fiches controlees (vue "Machine - Mails V3", 0 SQL) : 14 🟢 / 0 🟠 / 6 🔴.
- Repartition : reprise zone rang 3 (10) -> 7 🟢, 3 🔴 ; reserve hors zone ZONE LARGE (5) -> 4 🟢, 1 🔴 ; secondes chances hors zone (3) -> 1 🟢, 2 🔴 ; registre (2) -> 2 🟢.
- Defaut dominant : salutation nominative hors registre (4 rouges, C1 seul, reste conforme) -> ISS-016 mise a jour, passee en high.
- 2e defaut : signe d'abandon cite d'apres le HTML brut, invisible sur la page rendue (2 secondes chances hors zone) -> ISS-019 creee (high).
- Les anciennes sections "## Controle" ("Controle a refaire" / ancien mail) ont ete remplacees, pas empilees.
- Cout : 0 CHF (aucun DataForSEO/Apify). Notion : 0 SQL, 1 vue. Sous-agents x4.

## Pour la relance (03:00)
- 14 verts disponibles au depot (dont 2 registre, 4 ZONE LARGE, 1 seconde chance).

## Pour la recherche (nuit suivante)
- Corrections : 4 salutations a passer en "Bonjour," (sauf si ISS-016 est tranchee autrement en session dev) ; 2 secondes chances hors zone a reangler sur un signe visible ou a abandonner.
