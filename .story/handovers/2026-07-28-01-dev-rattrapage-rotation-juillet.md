# Handover — Session dev — 2026-07-28 — Rattrapage memoire de rotation (juillet)

## Pourquoi ce handover
La persistance `.story/` est morte depuis le 2026-06-27 (dernier commit) alors que les routines
ont continue a produire des fiches Notion en juillet. Cause identifiee : les routines demandaient
des validations de permission cote UI claude.ai/code et personne ne cliquait la nuit -> les
sessions stallaient avant l'etape de persistance. Les handovers de juillet sont PERDUS. Ce
handover RECONSTRUIT la memoire de rotation depuis le champ Segment des fiches Notion
(filet L-010), pour que le prochain run ne re-pioche pas un couple deja traite.
Reconstruction PARTIELLE (notion-search plafonne a 25 resultats ; outils query gates, cf. ISS-003) :
le crosscheck Notion par Segment reste le verrou faisant foi.

## Segments couverts depuis le 27 juin (reconstruits depuis Notion, dates Europe/Zurich)
- 2026-06-27 : carreleur x Fribourg (Bulle) — handover normal existant (dernier persiste).
- 2026-07-01 : peintre x Neuchatel (~6 fiches, dont 1 Creation site-vide et plusieurs a-appeler).
- 2026-07-02 -> 07-19 : AUCUNE fiche = trou de ~3 semaines (runs stalles sur validations).
- 2026-07-21 : electricien x Lausanne (~7 fiches). Controle 03:00 actif la meme nuit + rattrapage
  des fiches de fin juin restees sans verdict.
- 2026-07-23 : installateur PAC/solaire x Neuchatel (~5-6 fiches energie, dont sanitaire/chauffage
  proches). Relance active la meme nuit (1 relance micro-valeur ; brouillon Infomaniak en ECHEC,
  connecteur bloque).
- 2026-07-25 -> 07-27 : menuisier/ebeniste x Geneve (rejets logges le 25, retenus le 27 ;
  probablement un run interrompu puis refait).
- 2026-07-28 (matin) : carreleur x La Chaux-de-Fonds / Montagnes NE (au moins 1 retenu, mail
  redige accentue mais SIGNATURE SANS numero de telephone).

## Prochain segment a couvrir (suggestion)
Frais d'apres la reconstruction : sanitaire x Geneve, peintre x Lausanne, carreleur x Sion/Valais,
demenageur (echeance bail 30 sept a l'approche), cuisiniste x Neuchatel. Eviter : Geneve/Lausanne
sur electricien/menuisier/peintre recents, Neuchatel sur peintre/energie, Fribourg sur carreleur.

## Observations systeme (accumulation juillet, zero PII)
- ACCENTS : recidive massive malgre L-008 — 4 des 5 mails de juillet inspectes sont en ASCII
  (flagues C5 par le controle a chaque fois). Correctif applique ce jour (session dev) : verrou
  deterministe de relecture dans ROUTINE_PROMPT etape 6 + RELANCE_PROMPT etape 5 + CLAUDE.md.
- SIGNATURE : 2 defauts reels (numero errone 078 930 81 00 sur un mail parti ; numero absent le
  07-28). Correctif : signature canonique verbatim dans CLAUDE.md + controle C7 ajoute.
- FAIT PORTEUR : le controle a attrape le 07-23 une derive de requete (le mail lache le mot
  "installateur" et affirme une absence la ou le prospect est #1 du pack). Correctif : regle
  "lecture de l'organique" + preference au constat relatif (CLAUDE.md etape 4 + angles).
- Detecteur de trou memoire ajoute aux prompts 1h et relance (alerte en tete du recap si dernier
  commit .story > ~3 jours).
- ACTION REQUISE (Thomas, une fois) — CORRIGEE apres verification des docs officielles : il
  n'existe PAS de mode de permission par routine dans l'UI claude.ai/code, et le settings.json
  PROJET est ignore en session cloud. Le vrai levier : claude.ai -> Parametres -> Connecteurs ->
  pour chaque connecteur des routines (Notion, Apify, DataForSEO, Gmail), passer les outils en
  "autorise sans approbation" (un outil connecteur en mode "demander" prompte meme en
  bypassPermissions -- c'est la cause du mois de runs stalles).
