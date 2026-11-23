# SPRINT - viser 20 mails par jour ouvre (decision Kidam, 2026-11-23)

VALIDITE : runs dates du 2026-11-24 au 2026-12-02 inclus (date Europe/Zurich du run).
A partir du 2026-12-03 ce fichier ne s'applique PLUS : ignore-le entierement et reviens aux
plafonds habituels de PISTES.md, REPRISE.md et BOITE.md.
Pendant sa validite, ce fichier PRIME sur les plafonds chiffres de CLAUDE.md, PISTES.md,
REPRISE.md et BOITE.md, et sur eux seulement.

## Pourquoi
Kidam a besoin d'un contrat vite. Il envoie tout ce que la machine depose : la file de 10 se
vide chaque matin et c'est la machine qui le freine. On monte le debit pendant 7 jours ouvres,
sans toucher a la qualite ni aux garde-fous, puis on juge sur les chiffres.

## Ce qui change (et rien d'autre)
1. FILE DE BROUILLONS (BOITE.md section 3) : 20 au maximum au lieu de 10.
   Places libres = 20 - brouillons de prospection en attente.
2. ORDRE DE DEPOT DES MAILS 1 (BOITE.md section 3, point 2) : apres les relances, d'abord les
   fiches dont le Segment commence par "registre" (nouvelles entreprises), puis les autres
   mails 1, les reecritures les plus anciennes d'abord. Les secondes chances restent en dernier.
3. REPRISE DANS LA ZONE (PISTES.md etape 2, REPRISE.md) : 10 reecritures par nuit au lieu de 5.
   Les corrections apres controle restent a 5 au plus et passent toujours avant.
4. RECHERCHE (PISTES.md etape 3) : la piste A (registre du commerce) se fait CHAQUE nuit, quel
   que soit le stock, avec `python3 tools/fosc_nouvelles.py --jours 90` (au lieu de 45 ; le
   script met environ 2 minutes, c'est normal), objectif 5 a 8 retenus. Toujours rang 1, puis
   2, puis 3. Si le stock reste sous 20 apres la piste A, fais en plus la piste B ou C du jour,
   comme d'habitude. Stock >= 20 : ni B ni C.

## Ce qui ne change PAS
Zone et rangs, exclusions dures, perimetre 3D (Thomas a la main), redaction V3 (skill
writing), les 7 controles (aucun depot sans controle au vert), "la boite fait foi", un seul
brouillon par adresse, seconde chance (3 par nuit), reserve hors zone (regle du stock sous
10), relances (10 par nuit au plus), plafonds de cout, regles Notion (3 requetes SQL, 100
lignes), 3 appels du jour, aucun envoi automatique.

## Garde-fous du sprint
- Qualite avant quantite. Si le temps, le quota Notion ou le budget manque : traite moins de
  fiches, mais completes. Ne baisse jamais un controle et n'invente jamais un detail pour
  remplir la file. Moins de 20 est un resultat normal, pas une erreur.
- Si une ligne de ce fichier contredit un garde-fou (boite indisponible, controle vide ou non
  vert, "Email a confirmer", doublon, deja contacte), le garde-fou gagne.
- Recap de la recherche et mail "KUMO matin" : ajoute une ligne
  "SPRINT : X deposes cette nuit, file Y/20, stock Z, dont registre N".
- BILAN : dans le "KUMO matin" du 2026-12-03, ajoute une section "BILAN SPRINT" : mails V3
  envoyes du 2026-11-24 au 2026-12-02, reponses obtenues, par piste (registre, sans site,
  site date, ancienne fiche, seconde chance), et la phrase "sprint termine, plafonds
  habituels retablis".

## Revenir en arriere avant la date
Supprimer ce fichier (ou `git revert` du commit qui l'a ajoute) suffit : les trois renvois
places dans CLAUDE.md, PISTES.md et BOITE.md deviennent sans effet.
