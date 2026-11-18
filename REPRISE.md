# REPRISE - reecriture des mails jamais envoyes (decision Kidam, 2026-11-18)

## Pourquoi
Au 2026-11-18, la base Notion "Contacts" contient environ 174 fiches "Lead froid" avec un
email et un mail redige ("Draft pret" coche) qui n'ont JAMAIS ete envoyes. Ces mails
sont ecrits avec l'ancienne redaction, que Kidam ne veut plus. On les reecrit tous avec la
redaction V3 (skill .claude/skills/writing/), par lots, pour que Kidam les relise et les
envoie lui-meme. La reprise s'insere dans le programme de la nuit de PISTES.md : 5 fiches par nuit, celles de la zone d'abord ; les fiches hors zone restent en reserve.

## Fiches a reprendre (requete)
Base "Contacts", TOUTES ces conditions :
- "Statut pipeline" = "Lead froid" ;
- "Email" rempli ;
- "Draft pret" coche ;
- "Date mail 1" VIDE (jamais contacte) ;
- "Notes" ne contient pas "REDACTION V3".
JAMAIS une fiche deja contactee (Mail 1 envoye, Relance preparee, Mail 2 envoye, Lead
chaud, Perdu, Audit en cours) : on n'y touche pas. Si la requete structuree est refusee
par Notion, enumere par recherche + lecture des fiches.

## La boite fait foi (audit du 2026-11-18)
L'audit de la boite a montre des fiches en double et des fiches "Lead froid" alors qu'un
mail etait deja parti. Notion ne suffit donc pas. Au debut de chaque run, liste le dossier
Envoyes de thomas.puglisi@kumo-seo.ch (connecteur infomaniak-mail, `lister_messages` avec
`offset` jusqu'au bout ; `lire_message` si le destinataire n'apparait pas) et construis
l'ensemble des adresses et des domaines deja destinataires (ignore les domaines
generiques : gmail, bluewin, hotmail, outlook, sunrise, yahoo...). Pour CHAQUE fiche,
avant d'ecrire ou de reecrire un mail :
- son Email ou son domaine figure dans les Envoyes -> DEJA CONTACTE : aucun mail. Ajoute
  aux Notes "deja contacte (boite) le AAAA-MM-JJ, N mails" et signale-la au recap dans une
  section "Fiches a corriger" (Thomas ou le chat corrigera le statut).
- une AUTRE fiche porte le meme Email ou le meme domaine avec une "Date mail 1" ou un
  statut d'envoi -> doublon : aucun mail, meme note.
Si le connecteur de la boite est indisponible : n'ecris AUCUN mail cette nuit, recap avec
l'objet prefixe "BLOQUE" et la raison.

## Chaque nuit
Prends 5 fiches : d'abord celles de la zone de PISTES.md (rang 1, puis 2, puis 3), les plus
recentes d'abord. Hors zone : seulement dans le cas prevu par PISTES.md (point 4). Pour chacune :
1. Lis la fiche en entier (Diagnostic, ancien mail, Notes). Reverifie qu'elle remplit
   toujours les conditions ci-dessus.
2. Visite le site (1 requete). Site mort, activite arretee ou hors cible -> statut
   "Ancien" + note "reprise : site inactif le AAAA-MM-JJ", pas de mail, fiche suivante.
3. Reverifie que l'adresse email est toujours publiee (site, mentions legales). Sinon
   garde l'alerte "⚠️ Email a confirmer avant envoi" en tete du bloc mail.
4. Trouve UN detail vrai sur leur site (regle du skill writing). Aucun detail -> note
   "reprise : pas de detail verifiable", pas de mail, fiche suivante.
5. Reecris le bloc "## Email (brouillon)" avec la redaction V3 : il REMPLACE l'ancien
   mail (ne garde pas l'ancien texte). Ne touche pas au "## Diagnostic". Salutation :
   regle habituelle (prenom seulement si dirigeant actuel confirme).
6. Verrou accents + passe de relecture du skill writing.
7. Champs : ajoute aux "Notes" la ligne "REDACTION V3 - mail reecrit le AAAA-MM-JJ" ;
   vide le champ "Controle" (l'ancien verdict portait sur l'ancien mail) ; laisse le
   statut "Lead froid" et "Draft pret" coche. Ne change RIEN d'autre.
Tu ne deposes PAS de brouillon ici : la routine relance s'en charge ensuite (BOITE.md), apres le controle.

## Recap de la nuit
Objet : "KUMO reprise - AAAA-MM-JJ". En tete : "Reprise : N mails reecrits cette nuit,
N fiches restantes". Puis, pour chaque mail reecrit : nom de l'entreprise, adresse du
destinataire, objet, corps complet (pret a copier), lien de la fiche Notion. Puis les
fiches ecartees (site inactif, pas de detail) avec la raison.

## Fin
Quand il ne reste plus aucune fiche a reprendre dans la zone, dis-le une fois dans le recap. La reserve hors zone suit PISTES.md.
