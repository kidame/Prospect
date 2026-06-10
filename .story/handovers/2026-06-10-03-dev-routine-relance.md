# Routine 3 (relance J+7) implementee

**TL;DR** — Troisieme routine creee : RELANCE_PROMPT.md (04:00). Detecte Statut="Mail 1 envoyé" + "Date mail 1" <= J-7 + "Date relance 1" vide, relit la fiche (Diagnostic + mail 1 + Controle), re-mesure le fait porteur (1 SERP), redige une relance courte au cas par cas (fait neuf / micro-valeur / pivot honnete), l'ecrit en "## Relance 1 (brouillon)" + cree le brouillon Infomaniak, puis pose Statut="Relance préparée" + "Date relance 1" (verrou idempotence). Zero geste manuel nouveau pour Thomas.

## Decisions (validees avec Thomas)
- Delai 7 jours apres "Date mail 1" (remplie par SON automation Notion au passage en "Mail 1 envoyé").
- Marquage = statut "Relance préparée" + champ date "Date relance 1" (les deux, poses par la routine).
- Re-mesure legere systematique (1 appel SERP/eligible) ; la relance part toujours sauf contradiction totale (skip signale).
- Toutes les eligibles chaque nuit (volume reel ~20 mails/jour max), garde-fou >20 ou plafond 10 CHF.
- UNE seule relance auto par prospect ; relance 2 = manuelle. Frontiere clarifiee dans CLAUDE.md avec le garde-fou re-contact 120j (la relance J+7 = conversation ouverte, pas un re-contact a froid).

## Fait cote Notion (base Contacts)
- Champ date "Date relance 1" ajoute ; option "Relance préparée" (rose) ajoutee au Statut pipeline.
- VERIFIE : l'ALTER du select a preserve tous les IDs d'options existants (board + automation intacts).
- Dry-run complet sur fiche TEST (puis nettoyee + brouillon Infomaniak test supprime) : section relance, brouillon, statut, date, idempotence OK.

## Decouvertes systeme (a surveiller)
- Des fiches "Mail 1 envoyé" ont "Date mail 1" VIDE (vu sur 1 fiche reelle, segment cuisiniste x Geneve) : automation pas declenchee ou statut pose avant sa creation. La routine les IGNORE et les signale au recap. Thomas doit verifier l'automation + remplir les dates a la main sur l'existant, sinon ces prospects ne seront jamais relances.
- Le connecteur Notion ne pose PAS les dates a la CREATION de page (silencieux) ; en UPDATE ca marche. Sans impact routine (lecture seule de Date mail 1, ecriture de Date relance 1 en update), mais a savoir.
- T-002 mis a jour (partie relance J+7 faite ; reste cadence 1h + re-contact 120j).

## Suite
- Thomas : creer la routine 04:00 dans claude.ai/code/routines avec le bootstrap de RELANCE_PROMPT.md ; verifier l'automation "Date mail 1" ; optionnel : ajuster la formule "Relancer le" pour exclure "Relance préparée" ; supprimer la page TEST deplacee sous KUMO Back-office.
- Apres les 1ers runs : verifier qualite des relances (angles, pas de redite) via les handovers run-relance.
