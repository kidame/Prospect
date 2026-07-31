# Handover — session dev 2026-07-31 : fiabilisation relances + mails V2 anti-pub

## Contexte
Session interactive avec Thomas (pas une routine). Deux chantiers menés et MERGES dans main (PR #86, merge 31280f1).

## Chantier 1 : controle des relances du 31.07 (batch 09:07-09:15)
- Croisement fiche par fiche Notion x dossier Envoyes Infomaniak : 2 relances sur 17 visaient des prospects dont le mail 1 n'a JAMAIS ete envoye (brouillon reste en Drafts / jamais redige) + 1 fiche hors batch dans le meme etat.
- Cause racine : "Statut pipeline = Mail 1 envoye" + "Date mail 1" poses EN MASSE le 22.07 (bascule de statut groupee) alors que les envois reels s'etalent du 08.06 au 26.06 -> ISS-004 (open, high) avec changement suggere : la routine relance doit verifier l'ENVOI REEL dans Sent avant toute relance + logger l'UUID des brouillons crees.
- Corrections de donnees faites directement dans Notion : 3 fiches repassees Lead froid (dates effacees, notes posees), 15 "Date mail 1" corrigees aux vraies dates (08.06-19.06). Thomas a supprime les 2 brouillons de relance fautifs au webmail.
- Reste cote Thomas : envoyer les 3 mails 1 manquants (2 brouillons de juin en Drafts + 1 texte dans la fiche du menuisier de Buttes), puis basculer ces fiches en "Mail 1 envoye" au jour reel.

## Chantier 2 : mails V2 anti-pub (constat Thomas : "ca fait trop artificiel / pub")
- Analyse du corpus (16 mails reels) + recherche web -> diagnostic : le rendu pub venait de l'ENVELOPPE (HTML style + signature-banniere logo/slogan -> onglet Promotions) et de la REPETITION (meme squelette/charnieres/ouverture partout).
- Changements MERGES dans main :
  * tools/signature.html : signature sobre 3 lignes (Thomas Puglisi / KUMO, Couvet - kumo-seo.ch / 078 939 81 00), plus de logo/titre/baseline.
  * tools/infomaniak_draft_api.py : HTML minimal (p nus, zero style inline). Teste.
  * .claude/skills/writing/ : V2 complete (5 lois data, 4 squelettes A/B/C/D a alterner, 60-90 mots, 1 chiffre max, ton hedge, 0-1 question, objets minuscules factuels, interdits de gabarit).
  * CLAUDE.md : bloc REGLES ANTI-PUB, 60-90 mots remplace 8-14 lignes partout, signature canonique avec Couvet.
- T-008 (open) : protocole de test — 10 prochains mails 1 en forme V2, baseline historique depuis Notion, decision a ~20 envois sur le taux mesure (cible >= 8%).

## Pour les prochaines runs (IMPORTANT)
- La run de cette nuit tourne AVEC les regles V2 (mergees). La routine controle de 3h devrait verifier : compte de mots (60-90), 1 chiffre max, squelettes alternes, objets non "[metier] [ville]".
- La routine relance de 04:00 : ISS-004 reste OPEN — tant que RELANCE_PROMPT.md n'est pas mis a jour (decision dev a prendre), le risque de relance-sans-mail-1 persiste ; les dates Notion sont maintenant fiables pour les fiches corrigees.
- Aucun couple metier x zone n'a ete traite cette session (pas de collecte) : la rotation reprend la ou elle en etait.

## Prochaines decisions dev (a trancher avec Thomas via /story)
1. Assimiler ISS-004 : editer RELANCE_PROMPT.md (verif Sent + log UUID) puis resoudre l'issue.
2. ISS-003 (query Notion / dedup Place ID) toujours open.
3. T-008 : etablir la baseline de reponses et suivre le test V2.
