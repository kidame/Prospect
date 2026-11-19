# Handover — Run CONTROLE (03:00) — 2026-10-22 (Europe/Zurich)

## Resume
Controle qualite des fiches "Draft pret" sans verdict. 4 fiches controlees (toutes du run 1h de cette nuit, segment cuisiniste/agencement x Geneve). Verdicts : 2 🟢 OK, 1 🟠 A voir, 1 🔴 A trancher.

## Detail verdicts (niveau META, refs par segment/mesure, zero PII)
- 🟢 x2 : les 2 fiches dont le fait porteur (absent pack + organique sur la requete coeur) est confirme par re-mesure SERP mobile et dont l'accroche cite des concurrents verifies dans le pack. Mails propres (accents, hedge, CTA par mail, signature 078 939 81 00 conforme).
- 🟠 x1 : fait porteur partiellement confirme. Le prospect est bien absent du pack ET de l'organique (OK) et le 1er concurrent cite est confirme dans le pack #1 ; MAIS le 2e concurrent nomme dans l'accroche (organique) n'apparait PAS dans l'organique page 1 au re-controle (seulement en "Recherches associees") -> nom falsifiable. Organique entierement different du Diagnostic = forte volatilite SERP sur cette requete. Suggere : retirer/remplacer le 2e nom, mener sur le concurrent pack confirme.
- 🔴 x1 : C3 pages. Le mail affirme "le site tient en une seule page" ; le sitemap.xml liste 6 pages (prestations, presentation, realisations, contact, empty-page, accueil). Contenu bien tres mince (~107 mots) mais l'affirmation "une seule page" est falsifiable par le prospect. Concurrent-double par ailleurs confirme. Suggere : reformuler en "site tres mince" avant envoi.

## Controles appliques
- C2 re-mesure : 3 SERP live (serp_organic_live_advanced, mobile, Geneva,Switzerland) couvrant les 4 fiches (2 partagent la requete coeur). Packs locaux tous conformes aux Diagnostics. Organique de la requete "architecte d'interieur" tres volatil (voir 🟠).
- C3 : 1 sitemap.xml verifie (le cas "une seule page") -> a infirme l'affirmation.
- 1 verif site (realisations citees) : confirmees reelles -> fiche restee 🟢.
- C1/C4/C5/C6/C7 : RAS sur les 4 (salutations neutres partout, aucun prenom a risque ; accents complets ; CTA par mail ; signatures conformes ; "Probleme principal" propre ; emails sur domaine -> pas d'alerte requise).

## Observations systeme
- 2 flags sur 4 portent sur des SPECIFICS du fait porteur non verifiables (nom de concurrent organique volatil ; affirmation "une seule page" non recoupee au sitemap cote run 1h). Pas d'issue ouverte : occurrences isolees cette nuit, pas d'accumulation chiffree multi-nuits (le trou de handovers 15-20 oct empeche de voir si ca recidive). A re-surveiller : si "concurrent organique cite mais absent au controle" ou "une seule page sans sitemap" reviennent, ouvrir une issue routine-controle.
- Champ "Controle" (Select 3 options) deja en place, aucun setup requis.

## Cout estime
~0,4-0,5 CHF. DataForSEO : 1 serp_locations + 3 serp_organic_live_advanced (mobile, depth 20). 2 WebFetch (sitemap + site) ~0. Sous plafond 1-2 CHF.

## Prochain controle
Rien en attente : apres ce run, toutes les fiches "Draft pret" ont un verdict. Vue Notion "Non controlees" doit etre vide.