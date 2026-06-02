# Design — Routine de contrôle KUMO (seconde lecture des drafts)

Date : 2026-06-02
Statut : validé en brainstorming, prêt pour plan d'implémentation
Branche : `claude/controle-routine-design`

## Problème

La routine nocturne de 1h (`ROUTINE_PROMPT.md`) qualifie 3 à 5 prospects et écrit,
pour chacun, une fiche Notion avec `## Diagnostic` + `## Email (brouillon)`, coche
« Draft prêt », et envoie un mail récap. Au réveil, Thomas doit **re-contrôler à la
main** chaque draft, parce que la run de 1h produit régulièrement les mêmes erreurs
(visibles dans l'historique git) :

- mauvais prénom dans la salutation (ancien dirigeant, société tierce, marque voisine) ;
- « invisible » alors que la mesure montre une présence ;
- « aucune page » écrit sans avoir vérifié le sitemap ;
- accroche (« Problème principal ») polluée par une note de canal ; email scrapé
  incertain non signalé ;
- formulations IA / accents manquants.

But : une **seconde lecture automatique** qui relit chaque nouvelle fiche avec draft,
revérifie l'essentiel, et donne un **verdict par fiche** — pour que le matin Thomas ne
*cherche* plus les erreurs, et ne traite à la main que les fiches signalées.

## Objectif de succès

Le matin, Thomas ouvre Notion et ne lit en détail que les fiches 🟠/🔴. Les 🟢 sont
fiables telles quelles. La charge de **détection** est portée par la routine ; Thomas
ne garde que la charge de **décision** sur les cas signalés (qu'il applique au moment
où il copie le mail dans Gmail).

## Principe directeur : fiabilité par simplicité

Chaque pièce mobile est aussi un mode de panne. Le design est volontairement maigre.
Deux garanties structurelles portent la fiabilité :

1. **Lecture seule sur la fiche.** Le contrôleur n'écrit QUE le champ `Contrôle` et une
   section `## Contrôle`. Il ne touche jamais au mail ni aux autres champs. Il ne peut
   donc structurellement pas dégrader un draft. Tout ce qu'il trouve est *signalé*, pas
   corrigé ; Thomas applique au copier-coller (qu'il fait déjà).

2. **Un seul oracle externe, indépendant.** Sur le seul fait porteur de l'email (la
   requête sur laquelle l'accroche est bâtie), le contrôleur **re-mesure lui-même** via
   DataForSEO. Il ne fait confiance à aucune affirmation de la run de 1h. Pas de
   couplage entre les deux routines.

Corollaires :
- **Jamais 🟢 par omission.** Si le contrôleur n'a pas pu vérifier (DataForSEO HS,
  fiche incomplète), la fiche passe 🔴 « contrôle incomplet », jamais 🟢.
- **Anti-bruit.** Le faux 🔴 détruit la valeur de l'outil (si tout est 🔴, Thomas
  re-contrôle tout). Donc : tolérance sur la re-mesure (on ne flague que si l'écart
  **change l'argument**, pas une gigue de rang) ; salutation **asymétrique** (le
  contrôleur ne pousse que vers le « Bonjour, » neutre, jamais vers l'ajout d'un prénom).
- **Pas de drift.** La checklist pointe vers `CLAUDE.md` comme source unique des règles ;
  elle ne les recopie pas.

## Architecture

- **Une seule** nouvelle routine, indépendante, contexte neuf (vrais yeux neufs : elle
  ne voit pas le raisonnement de la run de 1h).
- Cron **03:00 Europe/Zurich** (2h après la run de 1h ; pour 3-5 prospects elle est
  largement finie). Même repo, mêmes connecteurs (Apify, DataForSEO, Notion, Gmail).
- **Aucune modification de la run de 1h.**

### Flux

```
03:00 → lit la base Notion Contacts
      → ramasse les fiches :  Draft prêt = vrai  ET  Contrôle vide
        (inclut le rattrapage des fiches restées vides des nuits précédentes)
      → pour chacune : passe la checklist (6 contrôles)
      → écrit le champ Contrôle (🟢/🟠/🔴) + la section ## Contrôle (preuves)
      → noop si rien à ramasser
```

Le ramassage sur « Contrôle vide » ne dépend d'aucun sentinelle posé par la run de 1h :
une fiche neuve a naturellement `Contrôle` vide. Une fiche jamais contrôlée (routine qui
a planté, ou ajoutée après le passage) reste vide → visible dans la vue « Non contrôlées ».

## Portée v1

- **Inclus** : fiches **avec draft** (canal EMAIL, `Draft prêt = vrai`) → passe complète.
- **Exclus de v1** : fiches « à appeler » (Diagnostic sans mail, aucun risque sortant) ;
  fiches rejetées. À ajouter plus tard si besoin.

## La checklist — 6 contrôles

Ancrés sur les erreurs réellement observées + le seul re-check factuel porteur. Tout est
**signalé** (jamais corrigé par le contrôleur).

- **C1 — Salutation (asymétrique).** Le prénom employé est-il bien le dirigeant **actuel**
  de **cette** entreprise ? Re-fetch /contact, mentions légales. Doute, nom = tiers /
  partenaire / marque voisine, indice d'ancien propriétaire → **flag + suggère « Bonjour, »**.
  Le contrôleur ne propose JAMAIS d'ajouter un prénom (sens unique vers le neutre = plus sûr).

- **C2 — Fait porteur (re-mesure indépendante).** Identifie la requête cœur sur laquelle
  l'accroche du mail est bâtie. Re-mesure via `serp_organic_live_advanced` (mobile,
  `location_name` exact). **Flag seulement si l'écart change l'argument** (le mail dit
  « absent du pack » mais la fiche est en fait dans les 3 ; ou inversement), **pas** une
  gigue de rang (±1-2 en organique). Si la re-mesure échoue → 🔴 « contrôle incomplet ».

- **C3 — Pages.** Si la fiche affirme « aucune page » (par ville/prestation) : vérifie au
  sitemap.xml (1 requête). Page qui existe mais dite absente → flag (« page X existe mais
  ne ranke pas » est la formulation correcte).

- **C4 — Angle vs mesure.** Le mail dit « invisible / absent » alors que le Diagnostic ou
  la mesure montre une présence (pack local et/ou organique) → flag (contradiction).

- **C5 — Formules IA + accents.** Phrase de la liste interdite (`CLAUDE.md` « Rédaction de
  l'email ») détectée, ou accents manquants → **signalés** (jamais réécrits : ré-accentuer
  est une opération sémantique en français, hors du périmètre du contrôleur).

- **C6 — Hygiène.** « Problème principal » pollué par une note de canal (`EMAIL`,
  `A APPELER`…) au lieu de la seule accroche ; email scrapé incertain (perso bluewin/gmail,
  ou domaine ≠ site) sans l'alerte « ⚠️ Email à confirmer » → signalés.

## Grille de verdict

- **🟢 OK** — aucun souci de jugement ; envoyable telle quelle. **Doit être le cas normal.**
- **🟠 À voir** — au moins une suggestion à appliquer (accents, formule IA, hygiène, typo),
  mais aucun problème de salutation / fait / angle. Coup d'œil rapide.
- **🔴 À trancher** — au moins un de : salutation risquée (C1), fait porteur qui diverge
  (C2), claim « aucune page » faux (C3), angle qui contredit la mesure (C4), **ou** contrôle
  incomplet. Demande la décision de Thomas.

Jamais 🟢 par omission.

## Sortie : Notion seul (zéro mail strict)

- **Nouveau champ `Contrôle`** dans la base Contacts — Select : *(vide)* / `🟢 OK` /
  `🟠 À voir` / `🔴 À trancher`.
- **Vue « À trancher »** : filtre `Contrôle = 🔴 OU 🟠`. La liste de travail du matin.
- **Vue « Non contrôlées »** : filtre `Draft prêt = vrai ET Contrôle vide`. **Seul filet
  d'échec** en zéro-mail : si la routine plante ou ne tourne pas, les fiches orphelines s'y
  empilent.
- **Section `## Contrôle`** dans le corps de chaque fiche contrôlée : les vérifs faites, les
  flags + la preuve + la correction suggérée. **Réécrite à chaque passage** (remplace, jamais
  empilée) → idempotent si une fiche est re-contrôlée.

Aucun mail n'est envoyé, jamais — y compris en cas d'échec.

**Risque résiduel assumé (choix de Thomas).** Le filet « Non contrôlées » est passif : il
faut prendre l'habitude de jeter un œil à cette vue. Un plantage complet de la routine n'a
pas d'alarme active ; il se manifeste par l'absence de verdicts et l'empilement dans la vue.

## Budget

~1 CHF/nuit (≈ une re-mesure SERP par fiche avec draft, $0.002/tâche, + éventuellement 1
volume + 1 sitemap). Largement dans l'enveloppe nocturne (~10 CHF). Si le plafond approche
ou DataForSEO échoue → fiches concernées en 🔴 « contrôle incomplet », stop.

## Livrables

1. **`CONTROLE_PROMPT.md`** (racine) — le prompt à coller dans la nouvelle routine 3h.
   Contient la checklist (6 contrôles) + la grille de verdict + les règles anti-bruit
   (tolérance, salutation asymétrique). Pointe vers `CLAUDE.md` pour les règles de fond.
   Pas de skill séparé (on calque le modèle de `ROUTINE_PROMPT.md`).
2. **Notion** — ajouter le champ `Contrôle` + créer les 2 vues (« À trancher »,
   « Non contrôlées »). Via le connecteur Notion ou manuellement.
3. **`CLAUDE.md`** — court pointeur : existence de la routine de contrôle, le champ
   `Contrôle`, et le fait que le contrôle est lecture seule.

Aucune modification de `ROUTINE_PROMPT.md` ni de la run de 1h.

## Ce qui a été explicitement écarté (anti-sur-ingénierie)

- **Auto-correction de forme** par le contrôleur (édition du mail + ré-encodage du bouton
  mailto) → coupé : pièce fragile pour un gain trivial. Lecture seule à la place.
- **Citation des sources par la run de 1h** → coupé : couple deux routines, défait
  l'indépendance, résout un quasi-non-problème (page changée en 2h). Re-mesure indépendante
  à la place.
- **Skill `controle-prospect/` séparé** → coupé : un seul `CONTROLE_PROMPT.md` suffit.
- **Contrôle des fiches « à appeler »** → hors v1 : aucun risque sortant.
- **Checklist de 14 points** → réduite à 6, ancrés sur les bugs réels.
- **Mail récap du contrôle / alerte d'échec** → écarté : zéro-mail strict, filet = vue Notion.

## Questions ouvertes pour l'implémentation

- Mécanique exacte du champ `Contrôle` côté Notion (création via MCP `notion-update-data-source`
  vs manuelle) et nom exact des vues.
- Formulation de la « requête cœur de l'accroche » à re-mesurer quand l'email s'appuie sur
  plusieurs faits : prendre le fait le plus structurant (celui qui porte l'angle).
