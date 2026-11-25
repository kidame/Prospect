# PISTES - ce que la machine cherche (V2, decision Kidam du 2026-11-18)

Ce document PRIME sur CLAUDE.md pour tout ce qui touche a la RECHERCHE de prospects :
zones, rotation, sourcing, qualification, scoring (sections "Cible", "Process" etapes 2 a 5
et 7, "Grille de scoring", "Regle de rotation"). Les EXCLUSIONS DURES de CLAUDE.md restent
en vigueur. La redaction reste dans le skill writing, la boite dans BOITE.md.

## Pourquoi on change (constat du 2026-11-18)
- 521 fiches en 5 mois, ~90 entreprises contactees, 1 seule interessee.
- La machine retenait des artisans "mal places sur Google". Leurs reponses : "j'ai deja un
  prestataire", "on recoit ca tous les jours". Etre mal classe n'est pas une envie d'acheter.
- Elle visait Lausanne et Geneve, la ou les artisans sont le plus demarches et ou
  "un independant de Couvet" n'a aucun avantage.
- Elle faisait une analyse complete avant le premier contact, alors que le mail (V3) ne
  l'utilise plus.
On cherche donc un MOMENT D'ACHAT, pres de chez Thomas, avec une qualification legere.

## Zone : le rayon ou Thomas peut se deplacer
- Rang 1 : Val-de-Travers et communes voisines (Fleurier, Couvet, Motiers, Travers,
  Buttes, Boveresse, Noiraigue, Saint-Sulpice, La Cote-aux-Fees, Les Verrieres, Les Bayards).
- Rang 2 : le reste du canton de Neuchatel (Littoral, Val-de-Ruz, Montagnes).
- Rang 3 : Nord vaudois (Yverdon, Sainte-Croix, Grandson, Orbe, Vallorbe et alentours).
Toujours le rang 1 d'abord, puis 2, puis 3.

### Rang 4 : ZONE LARGE (decision Kidam du 2026-11-25, PERMANENTE, EN PLUS des rangs 1 a 3)
Kidam travaille a distance : la distance n'est plus un filtre. Constat du 2026-11-25 : les
rangs 1 a 3 forment un bassin trop petit (registre : environ 3,5 inscriptions par jour, contre
environ 22 pour Vaud, Geneve et Fribourg). Le rang 4 S'AJOUTE : il ne remplace rien et ne
passe jamais avant les rangs 1 a 3.
- Piste A (registre) : reste du canton de Vaud, Geneve, Fribourg, Valais romand, Jura et
  partie francophone du canton de Berne (Jura bernois, Bienne). L'option `--large` du script
  s'en charge (publications en francais seulement, inscriptions agees de 7 a 10 jours).
- Pistes B et C (Maps) : villes moyennes et stations, PAS les centres de Lausanne et de
  Geneve (constat du 2026-11-18 inchange : artisans surdemarches). Liste de depart :
  Nyon, Gland, Morges, Vevey, Montreux, Aigle, Payerne, Fribourg, Bulle, Sion, Sierre,
  Martigny, Monthey, Delemont, Porrentruy, Bienne (entreprises francophones), Moutier,
  Saint-Imier ; stations : Verbier, Crans-Montana, Nendaz, Champery, Villars-sur-Ollon,
  Leysin.
- Toute fiche du rang 4 porte Notes += "ZONE LARGE" et un Segment qui le dit :
  "registre large x {canton}", "sans site large x {commune}", "site date large x {commune}".
  Une fiche "ZONE LARGE" n'est PAS "hors zone" au sens de CLAUDE.md, BOITE.md ou
  SECONDE_CHANCE.md : elle suit le cycle normal (mail 1, puis relance).
- Redaction : variante "ZONE LARGE" du skill writing. Thomas y dit simplement qu'il cherche
  des entreprises a qui ses services peuvent servir. Aucun "voisin", aucun "dans la region".
- Exclusions dures, tris, dedoublonnage, controles : les memes que pour les rangs 1 a 3.
- Les anciennes fiches "hors zone" SANS la mention "ZONE LARGE" gardent leurs regles
  (reserve de l'etape 4, BOITE.md 2h, SECONDE_CHANCE.md).

## Hors perimetre de la routine
Horlogerie, industrie, sous-traitance, tout ce qui releve de l'offre 3D : Thomas prospecte
ces entreprises LUI-MEME, a la main. La routine n'ecrit pas de mail pour elles. Si elle en
croise une interessante, elle la cite dans le recap ("a voir par Thomas, 3D"), sans fiche.

> SPRINT du 2026-11-24 au 2026-12-02 inclus : si le fichier `SPRINT.md` existe a la racine du repo et que la date du run (Europe/Zurich) est dans cette periode, lis-le : ses plafonds PRIMENT sur ceux ecrits ici. Hors periode ou fichier absent : ignore ce renvoi.

## Programme d'une nuit (remplace l'ancien "mode reprise" seul)
1. Etape 1 de ROUTINE_PROMPT.md (CLAUDE.md, memoire, alertes), puis la regle "La boite fait
   foi" de REPRISE.md (lecture des Envoyes).
2. CORRECTIONS puis REPRISE DANS LA ZONE (REPRISE.md) : d'abord les mails que le controle a
   mis orange ou rouge (5 au plus), puis, tant qu'il reste d'anciennes fiches a reprendre
   dans la zone, reecris-en 5.
2bis. SECONDE CHANCE (SECONDE_CHANCE.md) : 3 fiches au plus par nuit, rang 1 d'abord.
3. STOCK : compte les fiches "Lead froid" avec Email dont les Notes contiennent
   "REDACTION V3" (mails prets, pas encore envoyes).
   - stock >= 20 : PAS de recherche cette nuit (Thomas n'a pas encore envoye, on n'empile pas).
   - stock < 20 : fais UNE piste ci-dessous (A, B ou C en alternance d'une nuit a l'autre),
     objectif 3 a 5 retenus.
3bis. PART ZONE LARGE (decision Kidam du 2026-11-25), chaque nuit, APRES les etapes 2 a 3 et
   QUEL QUE SOIT le stock. Dans le resultat de la requete de l'etape 3 (aucune requete en
   plus), compte les fiches pretes dont le Segment commence par "sans site large" ou
   "site date large".
   - 6 ou plus : rien cette nuit (Thomas n'a pas encore envoye, on n'empile pas).
   - moins de 6 : fais la piste B ou la piste C (en alternance d'une nuit a l'autre) sur UNE
     commune de la liste du rang 4, objectif 3 retenus au plus.
   Le budget Apify de 0,60 USD par nuit reste le plafond TOTAL de la nuit, zone habituelle
   et zone large confondues. Si le temps, le quota Notion ou le budget manque, c'est cette
   etape qui saute en premier, et tu le dis dans le recap.
4. RESERVE HORS ZONE : les anciennes fiches hors zone ne se reprennent que si, apres les
   etapes 2 et 3, le stock reste sous 10. Alors 5 par nuit.
5. ANALYSE A LA DEMANDE : pour chaque fiche passee en "Lead chaud" (une reponse est
   arrivee) qui n'a pas encore d'analyse complete, fais l'analyse 2 axes de CLAUDE.md
   (etape 4 du Process) et mets-en le resume dans le recap : Thomas repondra arme.
   C'est le SEUL moment ou cette analyse se fait.
6. Fiches Notion, recap, memoire : comme d'habitude.

## Piste A - Nouvelles entreprises (registre du commerce)
Une entreprise qui vient de s'inscrire a besoin d'un site maintenant.
1. `python3 tools/fosc_nouvelles.py --jours 45 --large` (les trois rangs, plus le rang 4
   "ZONE LARGE" : 3 retenus de rang 4 au plus par nuit, APRES les rangs 1 a 3) (API publique de la Feuille officielle
   suisse du commerce, rubrique HR01, sans cle). Sortie : une ligne JSON par entreprise
   (rang, date, nom, commune, NPA, UID, forme, adresse, but, fin du texte ou figure le
   titulaire ou les gerants). Si le shell n'a pas acces au reseau : lis la meme API par
   WebFetch (https://amtsblattportal.ch/api/v1/publications?publicationStates=PUBLISHED
   &cantons=NE&subRubrics=HR01&publicationDate.start=AAAA-MM-JJ&publicationDate.end=
   AAAA-MM-JJ&pageRequest.size=100, puis /api/v1/publications/<id>/xml). Si les deux
   echouent : passe a la piste B et signale-le.
2. Ecarte : les inscriptions de moins de 7 jours (trop tot) ; les exclusions dures de
   CLAUDE.md (sante, restauration, beaute et coiffure, immobilier, finance et agences
   d'assurance, pure detention) ; les societes sans activite visible (domiciliees chez
   une fiduciaire, but purement financier) ; le perimetre 3D ci-dessus. Question de
   tri : "des clients la chercheront-ils en ligne, et peut-elle payer un site ?"
3. Deja vue ? Cherche dans Notion le nom ET l'UID (note dans les Notes : "UID: CHE-...").
4. Verification LEGERE (aucune analyse de positions) : a-t-elle deja un site ? Une
   recherche sur son nom + sa commune suffit.
   - vrai site correct -> fiche "Ancien", note "deja un site" (sert au dedoublonnage) ;
   - pas de site, page de reseau social seule, ou "en construction" -> RETENUE.
5. Contact : email de source officielle uniquement (son site, sa fiche Google, local.ch,
   un annuaire professionnel), jamais devine. local.ch est la meilleure source pour ces
   entreprises. Une adresse personnelle (gmail, bluewin...) publiee sur une de ces sources
   est CONFIRMEE : pas d'alerte "Email a confirmer" (regle du 2026-11-18, ISS-013).
   Un "site web" annonce par un annuaire se verifie : domaine parque ou vide = pas de site. Pas d'email mais un telephone -> "a
   appeler". Ni l'un ni l'autre -> fiche "Ancien", note "injoignable".
6. Salutation : le titulaire ou le gerant inscrit au registre est une source officielle,
   "Bonjour Monsieur Nom," ou "Bonjour Madame Nom," est donc permis. Jamais le prenom seul.
7. Fiche : Segment = "registre x <commune>", Offre KUMO = "Creation". Rang 4 : Segment =
   "registre large x {canton}", Notes += "ZONE LARGE".

## Piste B - Entreprises sans site
1. Google Maps (Apify, memes reglages que CLAUDE.md, `keywords` en tableau) sur une
   commune ou un secteur de la zone, minReviews 5. Graines : menuisier, charpentier,
   peintre, platrier, carreleur, electricien, sanitaire, chauffagiste, couvreur,
   ferblantier, macon, paysagiste, nettoyage, garage, carrosserie, serrurier, ramoneur,
   vitrier, storiste, demenageur. Budget Apify : 0,60 USD par nuit au maximum (le compte
   est partage avec la machine Thai).
2. RETENUE si : fiche Google active (au moins 5 avis, dont un de moins de 12 mois) ET
   aucun site, ou seulement une page Facebook / Instagram / local.ch / annuaire.
3. Contact et salutation : regles habituelles. Sans email -> "a appeler".
4. Fiche : Segment = "sans site x <commune ou secteur>", Offre KUMO = "Creation". Rang 4
   (etape 3bis) : Segment = "sans site large x <commune>", Notes += "ZONE LARGE".

## Piste C - Sites visiblement dates
1. Meme recolte Maps que la piste B ; cette fois les entreprises qui ONT un site.
2. Ouvre la page d'accueil (1 requete). RETENUE si au moins DEUX signaux concrets :
   pas adaptee au telephone (pas de balise viewport) ; pas de https ; derniere date
   visible (copyright, actualite) en 2019 ou avant ; mention Flash, "optimise pour
   Internet Explorer", compteur de visites ; page cassee ou "en construction".
   Note les signaux constates dans la fiche.
3. Fiche : Segment = "site date x <commune ou secteur>", Offre KUMO = "Refonte". Rang 4
   (etape 3bis) : Segment = "site date large x <commune>", Notes += "ZONE LARGE".
4. Dans le mail, on ne dit JAMAIS que le site est vieux (regle du skill writing).

## La fiche (qualification legere)
"## Diagnostic" tient en quelques lignes : la piste, les faits constates avec leur
source et leur date, le contact et sa source, pourquoi elle est retenue, l'offre.
Pas de positions, pas de volumes, pas de concurrents : cela vient a la reponse (etape 5).
"Probleme principal" = une phrase simple ("nouvelle entreprise sans site", "pas de site",
"site non adapte au telephone").

## Score (simple, pour trier)
Piste A sans site : 85. Piste B : 75. Piste C : 65 (70 avec trois signaux ou plus).
Ajoute 5 pour le rang 1.

## Dedoublonnage (corrige le defaut constate le 2026-11-18)
Avant de creer une fiche, cherche dans Notion : le Place ID, le domaine, l'email, le nom
avec le NPA, et l'UID. Une seule correspondance = deja vue. Puis la regle "La boite fait
foi" (adresse ou domaine deja destinataire d'un mail = aucun mail).

## Rotation
Alterne A, B, C d'une nuit a l'autre. La piste A revient souvent : chaque entreprise n'y
passe qu'une fois (UID). Pour B et C, ne refais pas la meme commune avant 30 jours.
Rang 4 (etape 3bis) : alterne B et C d'une nuit a l'autre, une seule commune de la liste par
nuit, en variant les cantons.

## Mesure (c'est elle qui decidera de la suite)
Le mail du matin donne, par piste (prefixe du Segment), le nombre de mails envoyes et de
reponses, en separant la zone habituelle (rangs 1 a 3) et la "ZONE LARGE" (rang 4). Apres 20
mails envoyes sur une piste, on compare et on garde ce qui repond.
