# Methode 3 canaux - reference complete

Origine: etude Thailande juin 2026, validee sur donnees reelles
(DataForSEO + Apify + annuaire UFE Phuket + SERP live). Chaque seuil
ci-dessous a ete calibre sur un echantillon reel mais PETIT (16 fiches
Maps, ~25 domaines SERP, 1 annuaire). Garder les seuils en parametres.

## Pourquoi 3 canaux (et pas 1)
- La "nationalite du proprietaire" n'existe dans aucune base. La francite
  est un faisceau d'indices, donc un scoring, pas un filtre.
- Chaque canal a un angle mort:
  - A (annuaires) rate ceux qui ne reseautent pas.
  - B (SERP) rate les invisibles totaux (0 keyword) et les sans-site.
  - C (Maps) rate les pure-players web sans pignon sur rue.
- Le recoupement entre canaux EST le meilleur signal de francite.

## Canal A - Annuaires communautaires
Sources types: UFE <ville> (ufe-<ville>.org/annuaire/, suivre la
pagination alphabetique /annuaire/char/A ... /Z), rawai.fr (Phuket),
sections CCI/chambre de commerce (souvent derriere login: ne prendre que
le public), lepetitjournal edition locale (media: source d'entites, pas
prospect lui-meme), groupes et pages "francophones de <ville>".
Parsing: nom, contact (prenom francais = indice), tel, email, site,
categorie. Exclure categories {Associations, Media, Ecoles publiques} et
marques corporate (Club Med, Accor...). Bruit connu: champs pays errones,
entrees sans site (= prospects GBP-only, a garder).
IMPORTANT: reperer la categorie "Web Design / SEO" = CONCURRENT local.
Le lister dans l'output a part; sa presence change l'angle de vente
(differenciation par la data) ou la geographie (frapper ailleurs).

## Canal B - SERP inversee
Pour chaque money keyword du fichier data/money_keywords_<pays>.json:
- outil: DataForSEO serp_organic_live_advanced, language fr, depth 20-30.
- location: lancer la SERP dans le pays de la CLIENTELE du keyword
  (champ loc du fichier): FR pour l'avant-voyage et l'immobilier,
  pays cible pour le "sur place". En cas de doute: les deux.
- garder organic + local_pack, positions 2-50, hors blocklist.
- position 1 organique: ambigu (peut etre deja gagnant) -> garder mais
  la qualification etape 4 tranchera.
- les domaines blocklistes ou juges "media/blog metropole" sont ignores.
  Test de jugement pour les residus: ce site VEND-il un service rendu
  dans la zone, ou PARLE-t-il de la zone? On ne prospecte que le premier.
C2 (cible FR) et C3 (besoin si pos > 3) sont garantis par construction.

## Canal C - Google Maps via Apify
Actor: compass/crawler-google-places. Input type:
{ "searchStringsArray": ["<requete fr> <ville>", ...],
  "language": "fr", "maxCrawledPlacesPerSearch": 8-20,
  "maxReviews": 10, "reviewsSort": "newest",
  "scrapeReviewsPersonalData": false, "maxImages": 0 }
Requetes NEUTRES de preference ("agence immobiliere <ville>"): le test a
montre que les francais remontent sans forcer, et la requete neutre donne
des negatifs pour calibrer. Ajouter 1-2 requetes marquees ("restaurant
francais <ville>") par verticale grand public.
Signaux a extraire par fiche:
- pct_fr_reviews = part des reviews[].originalLanguage == "fr"
- owner_responds_fr = reponses du gerant en francais (regex mots FR:
  merci|bonjour|notre|nous|vous|plaisir|equipe|tres|ravis)
- category_fr = categoryName contient "francais(e)"
- website absent ou facebook.com -> prospect GBP-only
- reviews_count faible (< 20) et absence de reponses = faiblesses vendables
Couts mesures: ~0.11 CU pour 16 fiches x 10 avis (~100s de run).

## Bareme francite (v2, fige)
annuaire FR +4 | rank >=2 money kw +3 (1 kw: +2) | avis FR >=60% +3
(30-59%: +1) | gerant repond FR +2 | nom a motif FR +2 | categorie Google
FR +2 | site FR +2 | domaine .fr ou mot FR +1 | tel +33 +1.
Seuils: >=5 prospect, 3-4 a verifier, <3 exclu.
Lecon du terrain: le % d'avis seul donne des faux negatifs (ex: resto
francais a clientele internationale qui ecrit en anglais. Cas reel:
Chez Francois, 10% FR). Le nom et la categorie rattrapent ces cas.
Flag OPPORTUNITE_LANGUE: francite >=5 ET site en anglais seulement.
Cas reel: ASIA Global Yachting, gerant francais (annuaire UFE), site EN,
invisible sur "yacht phuket" en FR alors que la SERP FR est vide.

## Qualification SEO (etape 4)
Outil: DataForSEO domain_rank_overview, language fr, location = pays
source de la clientele (France en general).
Classes (parametres dans le script):
- deja_gagnant: etv >= 8000 OU (>= 150 kw en page 1 ET page 2 < page 1)
  -> ECARTE, sortie CONCURRENT_REF. Cas reel: thailand-roads.fr.
- invisible: 0 keyword. Cas reel: emotions.asia.
- sous_performant: >= 10 kw en page 2 OU page2 >= page1. Le MEILLEUR
  profil de vente. Cas reels: thaiunika (162 en p.2), coolasiatravel.
- gbp_only: aucun vrai site (Facebook/linktr seulement, et aucun domaine
  trouve par un autre canal). Offre: GBP + site 1 page.
- emergent: le reste.
- non_qualifie: DataForSEO PAS encore lance. REGLE DURE: un non_qualifie
  ne sort jamais en T1/T2 final, il va en A_QUALIFIER. On ne demarche
  jamais avec un angle SEO non prouve par la data.

## Cas particulier: GBP qui pointe vers Facebook
Si un business a un VRAI site (trouve par un canal) mais que sa fiche
Google pointe vers une page Facebook/linktr, ce N'EST PAS un gbp_only.
Le script le detecte (champ gbp_issue) et garde le vrai profil SEO.
C'est meme un excellent angle: "votre fiche Google envoie vers Facebook
au lieu de votre site, vous perdez du trafic pour rien".

## Regle Maps-only (doctrine "aucun signal seul ne decide")
Un business connu UNIQUEMENT par Google Maps (canal C seul) ne monte en
T1 que s'il est gbp_only: dans ce cas Maps est la seule source possible,
l'exiger ailleurs serait absurde. Si le business a un vrai site mais n'est
sorti que sur Maps, il plafonne a T2 tant qu'un 2e canal (SERP ou annuaire)
ne confirme pas. Le bloc gbp en sortie est agrege sur TOUTES les fiches
Maps (meilleur signal), coherent avec le score: pas de fiche qui annonce
80% en francite puis 10% dans le bloc Google Business.

## Offre gouvernee par le tier
L'offre recommandee depend du TIER avant le profil SEO. Un CONCURRENT_LOCAL
ou CONCURRENT_REF recoit "NE PAS PROSPECTER", pas une offre SEO. Un
A_QUALIFIER recoit "diagnostic DataForSEO d'abord". Seuls les vrais
prospects (T1/T2/T3) recoivent une offre operationnelle selon leur profil.

## Tiers
T1 = verticale >=4 ET besoin max ET francite >=5 ET profil SEO prouve.
T2 = verticale 3 avec bons signaux, ou verticale >=4 avec un signal moyen.
T3 = le reste qualifie.
A_QUALIFIER = francite OK mais besoin SEO pas confirme (lancer DataForSEO).
T1_VOLUME_A_VALIDER = verticale forte mais sans money keyword FR valide.
T3_A_VERIFIER = francite incomplete (3-4), oeil humain requis.
CONCURRENT_LOCAL = agence web/SEO du coin. CONCURRENT_REF = deja gagnant.
EXCLU = francite < 3 ou verticale a valeur nulle.

## Lecon volumes par verticale (verifie 06/2026)
Toutes les verticales "intuitives" n'ont pas de demande FR. Verifie:
immobilier, visa/relocation (visa thailande 9900), receptif (CPC 6-12),
nautisme, excursions = demande FR reelle. MAIS construction/piscine (30),
gestion locative (<10), demenagement (40) = demande FR quasi nulle.
Ces dernieres ne produisent pas de vrai T1 par volume; si francite forte,
les vendre sur signaux locaux (avis, GBP) et non sur le volume de recherche.
Assurance: volume national existe mais marche sature, pas un creneau local.

## Adapter a une nouvelle destination (Bali, Dubai, Maurice...)
1. Construire money_keywords_<pays>.json en VALIDANT chaque volume via
   DataForSEO (jamais a l'instinct: l'etude Thailande a montre que
   l'intuition se trompe sur ou est le volume).
2. Reperer les annuaires communautaires locaux (UFE <ville>, CCI,
   lepetitjournal local, groupes FB).
3. Verifier s'il existe un prestataire SEO francophone deja en place
   (recherche "<ville> web design SEO francais") et choisir l'angle.
4. Memes scripts, memes seuils au depart, recalibrer apres le 1er scan.

## Limites connues
- Seuils calibres sur petit echantillon: les garder parametrables.
- Loanwords (yacht, catamaran, massage...): identiques FR/EN, le volume
  "langue fr" peut etre legerement surestime, decoter mentalement 20-30%.
- Un gerant thai qui repond via traducteur peut passer le signal owner_fr:
  acceptable car aucun signal ne decide seul.
- ETV DataForSEO = estimation, fiable en ordre de grandeur seulement.
- Le scoring DETECTE, l'humain QUALIFIE: toujours visiter le site des T1
  avant le premier contact.
