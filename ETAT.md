# ETAT - Prospect (machine a prospects KUMO, Suisse)

## Derniere session (2026-11-27, chat Claude, depuis le VPS Kumo)

- PARAGRAPHE IDEE (decision Kidam) : pour toute entreprise qui a un site, le detail dit
  platement ("je suis tombe sur vous..., j'ai vu que vous louez aussi...") est remplace par
  un fait vu chez eux suivi d'une bonne premiere idee (35 a 50 mots, sans jargon, sans "a
  votre place", le paragraphe finit sur l'idee). Preparation obligatoire dans la fiche, bloc
  "### Portrait et idees" sous le Diagnostic (3 a 5 pages lues, portrait, 3 ecarts avec
  preuve, idee retenue, idee de reserve). Skill writing : section "Le paragraphe idee", avec
  3 modeles valides par Kidam (essai a la main sur Kime Carrelage, DMD Transport, Energy Pro ;
  ces 3 fiches Notion n'ont PAS ete modifiees).
- PORTE IDEE (mots de Kidam) pour ces mails : "Si vous avez envie d'en parler, repondez
  simplement a ce mail, j'en discuterai avec plaisir. Et si ce n'est pas le moment, aucun
  souci." PORTE UNIQUE pour tout mail ecrit depuis le 27.11, registre et sans site
  compris (decision Kidam) ; les portes A et B ne s'ecrivent plus.
- Marqueur : Notes += "IDEE : <trois mots>". Le controle (C2, C4) applique les nouvelles
  regles seulement aux fiches qui le portent. Pas d'idee etayee -> MAIL SIMPLE (presentation, services, porte, rien d'autre ; Notes
  "MAIL SIMPLE"), decision Kidam.
- RELANCE : si le mail 1 portait une idee, la relance prend l'idee de reserve.
- Alignes : CLAUDE.md, ROUTINE_PROMPT.md, CONTROLE_PROMPT.md, RELANCE_PROMPT.md, REPRISE.md,
  SECONDE_CHANCE.md. Registre et sans site : inchanges. Retour arriere : `git revert`.
- STOCK (decision Kidam) : les mails 1 V3 a detail plat deja ecrits pour une entreprise avec
  site ne sont plus deposes (BOITE.md 3) et sont reecrits avec une idee, 5 par nuit
  (REPRISE.md, "Stock V3 a detail plat"). Consequence attendue : moins de brouillons deposes
  les premieres nuits. Les secondes chances deja ecrites partent telles quelles.
- NON DECIDE (Kidam ne sait pas encore) : ecarter ou non les entreprises dont le site est
  deja tres travaille. En attendant, on leur ecrit.
- A surveiller dans le "KUMO matin" du 28.11 : nombre de mails a idee ecrits, fiches "pas
  d'idee etayee", duree du run (3 a 5 pages par fiche au lieu d'une), verdicts C2.

## Session precedente (2026-11-25, chat Claude, depuis le VPS Kumo)

- ZONE LARGE PERMANENTE (decision Kidam : "en plus, pas en moins") : un RANG 4 s'ajoute aux
  rangs 1 a 3, sans rien retirer. PISTES.md ("Rang 4" et etape 3bis) fait foi.
  Piste A : reste de Vaud, Geneve, Fribourg, Valais romand, Jura, Berne francophone
  (tools/fosc_nouvelles.py --large, publications en francais seulement). Pistes B et C :
  une commune par nuit dans une liste de villes moyennes et de stations (jamais les centres
  de Lausanne et de Geneve), 3 retenus au plus, tant qu'il y a moins de 6 fiches pretes.
- REDACTION "ZONE LARGE" (skill writing) : un bloc Services different, ou Thomas dit qu'il
  cherche des entreprises qui pourraient avoir besoin de ses services. Plus de "voisin" ni
  de "dans la region" sur ces fiches. Controle C2 et C4 alignes.
- DEPOT (BOITE.md 3) : une place de mail 1 sur trois va a une fiche "ZONE LARGE" au vert.
- Les fiches "ZONE LARGE" deja controlees avant le 25.11 gardent leur ancien bloc Services.
- Retour arriere : `git revert` de ce commit.
- A surveiller dans le "KUMO matin" du 26.11 : fiches "large" creees, etape 3bis faite ou
  sautee (temps, budget Apify), compteurs separes zone habituelle / ZONE LARGE.
- Pistes par signaux discutees le 25.11, PAS decidees : clients d'agences web disparues,
  sites faits maison ou loues, annonceurs Google sans referencement naturel, reprises et
  changements de nom au registre. Refusee par Kidam : la demo avant le contact.

## Session precedente (2026-11-23, chat Claude, depuis le VPS Kumo)

- SPRINT (decision Kidam) : viser 20 mails par jour ouvre du 2026-11-24 au 2026-12-02.
  Un seul fichier, SPRINT.md, porte les plafonds temporaires (file 20, reprise 10 par nuit,
  piste A registre chaque nuit sur 90 jours, mails "registre" deposes en premier). Trois
  renvois d'une ligne dans CLAUDE.md, PISTES.md et BOITE.md. Rien d'autre n'est modifie :
  ni les horaires des routines, ni la redaction, ni les controles.
- ZONE LARGE (decision Kidam, meme jour) : pendant le sprint, Vaud, Geneve et Fribourg entrent
  dans la piste A (tools/fosc_nouvelles.py --large, rang 4, inscriptions de 7 a 10 jours ; test
  du 23.11 : 88 candidats, 38 GE, 29 VD, 21 FR) et dans la reprise des anciennes fiches hors
  zone (5 par nuit). Pistes B et C inchangees. Variante d'accroche "du canton de X" ajoutee au
  skill writing et au controle. Sans --large, le script se comporte comme avant (teste).
- Constat de depart (boite lue le 23.11) : 29 mails V3 envoyes en 3 jours, 1 reponse (refus).
  Registre : 313 inscriptions dans la zone sur 90 jours (rang 1 = 9, rang 2 = 207, rang 3 = 97).
- Retour arriere : supprimer SPRINT.md ou `git revert` de ce commit.
- Hors machine : Buchs Freres SA (La Cote-aux-Fees) contacte a la main le 23.11 par Thomas
  (angle 3D, lien personnel). Sa fiche Notion n'a PAS ete touchee : ne lui redige ni relance
  ni seconde chance, Thomas gere ce contact lui-meme.

## Prochaine etape (sprint)

1. Lire le "KUMO matin" du 24.11 : ligne SPRINT presente, nombre de depots, aucun controle saute.
2. Le 03.12 : lire le BILAN SPRINT et decider de la suite avec les chiffres par piste.

## Session precedente (2026-11-18, chat Claude, depuis le VPS Kumo)

- Constat : les 3 routines tournent chaque nuit sans erreur. Base "Contacts" : environ 174
  fiches "Lead froid" avec un mail redige jamais envoye ; environ 70 prospects deja
  contactes. Depuis le 2026-08-03 plus aucun brouillon Infomaniak n'est cree : les mails
  vivent dans les fiches Notion. Les brouillons restes dans la boite sont anterieurs.
- Redaction V3 (decision Kidam) : Thomas se presente (web designer et specialiste du
  referencement Google, independant, Couvet), un detail vrai vu chez eux, ses services,
  une porte ouverte par mail. Aucun chiffre ni analyse SEO dans le mail. Skill writing
  reecrit ; CLAUDE.md, ROUTINE, CONTROLE (C2) et RELANCE alignes.
- Mode REPRISE (REPRISE.md) : 10 fiches par nuit reecrites en V3, sans nouveau sourcing
  tant qu'il en reste.

- Audit de la boite Infomaniak fait depuis le chat (acces par tools/ + .env local, lecture
  seule) : 242 envoyes, 126 recus, 35 brouillons. Notion corrige (1 refus, 1 lead chaud a
  relancer a la main, 1 fiche jamais marquee, 1 doublon, 16 fiches creees pour des envois
  sans fiche). 31 brouillons perimes supprimes. Regle ajoutee : la boite fait foi avant
  tout mail (REPRISE.md).

- BOITE.md (decision Kidam) : la routine relance lit la boite chaque nuit (envois et
  reponses constates -> Notion a jour sans saisie), depose au plus 10 brouillons prets
  (mails V3 controles au vert), envoie un seul mail du matin "KUMO matin".

- PISTES.md (decision Kidam) : la recherche change de cible. Zone = Val-de-Travers, canton
  de Neuchatel, Nord vaudois. Trois pistes : nouvelles entreprises (registre du commerce,
  tools/fosc_nouvelles.py, ~120 inscriptions par mois dans la zone), sans site, site
  date. Recherche seulement si le stock de mails prets passe sous 20. Analyse complete
  uniquement pour un prospect qui a repondu. 3D / horlogerie : Thomas a la main.

### Soir du 2026-11-18 : controle et relance alignes sur la nouvelle machine
- CONTROLE_PROMPT.md reecrit : plus de re-mesure Google, 7 controles V3 (salutation registre,
  detail verifie sur le site ou sur le registre, zero SEO, blocs fixes et porte, formules,
  adresse confirmee par publication, signature "KUMO, Couvet"). Vert = depose en brouillon.
- RELANCE_PROMPT.md reecrit : lit la boite, redige les relances V3 sans re-mesure, depose les
  brouillons et envoie "KUMO matin" TOUTES les nuits, meme sans relance due (avant : s'arretait).
- REPRISE.md : la recherche corrige elle-meme les mails orange ou rouge la nuit suivante.
- tools/boite_etat.py : lecture de la boite en une commande (envoyes, brouillons, recus, retours).
- Regle Notion : 100 lignes au plus par requete SQL, 3 requetes ciblees par run.
- 8 brouillons V3 deposes a la main depuis le chat (controle fait en chat, fiches au vert).
- A surveiller : premier run complet de la nuit du 18 au 19 (recherche 00:20, controle 02:10,
  relance 03:05). Le controle ne tourne que du lundi au vendredi.

- SECONDE CHANCE (decision Kidam, soir du 18) : un nouveau mail V3 pour les fiches "Relance
  préparée" de la zone, jamais de reponse, 2 envois au plus, dernier envoi de plus de 120 jours.
  3 par nuit, Val-de-Travers d'abord. Hors zone (34 fiches) : seconde chance pour 5 fiches
  marquees dans Notion (site a refaire, 3 verifiees en chat, 2 a reverifier par la routine) ;
  les autres sont classees "Perdu" par la routine relance (BOITE.md 2h).

- SIGNATURE (soir du 18) : tools/signature.html reprend la signature complete du webmail de
  Thomas (logo KUMO, titre, coordonnees), a la place des 3 lignes sobres du 31 juillet. Les 8
  brouillons ont ete refaits. A verifier : le rendu du logo chez le destinataire (image integree).
- REDACTION (soir du 18) : aucun deux-points, aucun compliment, aucun slogan dans les mails.

## Prochaine etape

1. Lire le recap "KUMO reprise" du lendemain et juger les premiers mails V3.
2. Verifier le premier mail "KUMO matin" : brouillons deposes, envois constates.
