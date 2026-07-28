Session dev 2026-07-28 (a la demande de Thomas, en journee).

1) MISE EN BROUILLON SUR DEMANDE : 5 fiches Lead froid "Draft pret" poussees en brouillons
Infomaniak (segments : demenageur x Geneve, carreleur x Lausanne, transition energetique x
Fribourg, cuisiniste x Neuchatel, fiduciaire x Yverdon). Fait porteur re-verifie par SERP
mobile sur les 4 fiches dont la mesure datait de plus d'un mois : tous conformes ; 1 mail
ajuste (un concurrent cite dans le mail avait quitte le pack local depuis la mesure). 3 mails
dataient d'avant la regle CTA du 2026-06-20 (creneau "15 min" au 1er contact) -> CTA reecrit
en micro-offre par mail dans la fiche Notion (source unique) AVANT creation du brouillon ;
2 anciens boutons mailto retires. Notes des fiches tracees (re-mesure + brouillon cree).

2) AUTONOMIE DES ROUTINES (demande explicite de Thomas : plus jamais de demande d'autorisation
la nuit). Cause identifiee : le recap passait par Gmail, et la creation de draft Gmail exige
une approbation UI -> session en pause a 1h/4h, travail perdu. Symptome corroborant : AUCUN
handover pousse sur main entre 2026-06-27 et 2026-07-28 alors que les runs produisaient des
fiches Notion. Correctifs : recap bascule sur brouillon Infomaniak (ROUTINE_PROMPT.md etape 9,
RELANCE_PROMPT.md etape 7) + interdit explicite de tout appel mcp__Gmail__* la nuit (sections
Execution autonome) + allowlist .claude/settings.json completee (Notion, Apify, Dataforseo,
KUMO-tools, WebFetch/WebSearch) en double filet du bypassPermissions + CLAUDE.md aligne
(Outils, Livrables etape 9, Garde-fous).

A VERIFIER apres la prochaine nuit : handover run-1h bien pousse sur main + brouillon recap
present dans les Brouillons Infomaniak. Si un outil prompte encore, il sera nomme dans le
recap (regle existante) -> l'ajouter a l'allowlist.
