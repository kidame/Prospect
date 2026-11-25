# SPRINT - viser 20 mails par jour ouvre (decision Kidam, 2026-11-23)

VALIDITE : runs dates du 2026-11-24 au 2026-12-02 inclus (date Europe/Zurich du run).
A partir du 2026-12-03 ce fichier ne s'applique PLUS : ignore-le entierement et reviens aux
plafonds habituels de PISTES.md, REPRISE.md et BOITE.md.
Pendant sa validite, ce fichier PRIME sur les plafonds chiffres de CLAUDE.md, PISTES.md,
REPRISE.md et BOITE.md, et sur la zone (point 5), et sur eux seulement.

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
   que soit le stock, avec `python3 tools/fosc_nouvelles.py --jours 90 --large` (au lieu de
   `--jours 45` ; le script met 3 a 4 minutes, c'est normal). Objectif 5 a 8 retenus par nuit :
   d'abord la zone habituelle (rang 1, puis 2, puis 3) jusqu'a 5 retenus, puis le rang 4
   (point 5) pour 3 retenus au moins s'il y en a de valables. Si le stock reste sous 20 apres
   la piste A, fais en plus la piste B ou C du jour, dans la zone habituelle. Stock >= 20 :
   ni B ni C. L'etape 3bis de PISTES.md (part zone large, piste B ou C) s'applique EN PLUS
   et ne depend pas de ce stock.
5. ZONE LARGE (decision Kidam du 2026-11-23, "pas que le Vallon") : pendant le sprint, le reste
   du canton de Vaud (Lausanne comprise), Geneve et Fribourg entrent dans le perimetre, de
   deux facons seulement :
   (MISE A JOUR du 2026-11-25 : la zone large est devenue PERMANENTE et plus etendue, voir
   PISTES.md "Rang 4" et etape 3bis. Ce point ne garde que les plafonds propres au sprint.)
   a. Piste A : `--large` ajoute un RANG 4 (champ "canton" : VD, GE, FR, VS, JU ou BE), limite aux
      inscriptions agees de 7 a 10 jours, une tranche qui avance toute seule chaque nuit.
      Memes tris et memes exclusions que les rangs 1 a 3. Fiche : Segment
      "registre large x {canton}", Notes += "ZONE LARGE". Une fiche "ZONE LARGE" n'est PAS
      "hors zone" au sens de CLAUDE.md, PISTES.md ou BOITE.md.
   b. Reserve hors zone (PISTES.md etape 4) : 5 anciennes fiches hors zone jamais contactees
      reecrites par nuit, quel que soit le stock, APRES la reprise dans la zone. Notes +=
      "ZONE LARGE".
   Pistes B et C : depuis le 2026-11-25 elles ont une part en zone large (PISTES.md etape
   3bis : villes moyennes et stations, jamais les centres de Lausanne et de Geneve, constat
   du 2026-11-18 inchange). Redaction des fiches "ZONE LARGE" : variante "ZONE LARGE" du
   skill writing.

## Ce qui ne change PAS
Ordre des rangs, exclusions dures, perimetre 3D (Thomas a la main), redaction V3 (skill
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
  site date, ancienne fiche, seconde chance), en separant zone habituelle et "ZONE LARGE",
  et la phrase "sprint termine, plafonds
  habituels retablis".

## Revenir en arriere avant la date
Supprimer ce fichier (ou `git revert` du commit qui l'a ajoute) suffit : les trois renvois
places dans CLAUDE.md, PISTES.md et BOITE.md deviennent sans effet.
