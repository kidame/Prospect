# ETAT - Prospect (machine a prospects KUMO, Suisse)

## Derniere session (2026-11-18, chat Claude, depuis le VPS Kumo)

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
  3 par nuit, Val-de-Travers d'abord. Hors zone (35 fiches) : decision en attente.

## Prochaine etape

1. Lire le recap "KUMO reprise" du lendemain et juger les premiers mails V3.
2. Verifier le premier mail "KUMO matin" : brouillons deposes, envois constates.
