---
name: machine-prospects-expat
description: Deniche, score et qualifie des prospects SEO parmi les business detenus par des francophones a l'etranger (Thailande par defaut, parametrable a toute destination expat). Utiliser ce skill des que l'utilisateur veut trouver des prospects ou clients francophones dans un pays etranger, scanner une ville (Koh Samui, Bangkok, Phuket, Bali, Dubai...), detecter des business francais mal references, construire une liste de prospection SEO internationale, ou execute la "methode 3 canaux" (annuaires, SERP inversee, Google Maps). Declencheurs - "prospects francophones", "business francais en", "scan de zone", "machine a prospects expat", "qui demarcher a".
---

# Machine a Prospects Expat - methode 3 canaux

Trouve les business detenus par des francophones dans une zone etrangere,
qui visent une clientele francophone, qui ont besoin de SEO et les moyens
de le payer. Sortie: prospects scores + fiche argumentaire chiffree par
prospect Tier 1, format compatible pipeline W4.

## Pre-requis
- MCP DataForSEO actif (SERP organic live + domain rank overview).
- MCP Apify actif avec acces a compass/crawler-google-places.
- python3. Aucune autre dependance.

## Les 4 criteres (tout prospect doit les cocher)
- C1 Francite: faisceau d'indices, score >= 5 (bareme dans references/methode.md)
- C2 Cible FR: la clientele du business cherche en francais (match money keywords)
- C3 Besoin: PAS en page 1 sur ses money terms (invisible, GBP-only ou page 2 lourde)
- C4 Budget: verticale a ticket suffisant (data/verticales.json) + signaux solidite

Regle d'or: aucun signal seul ne decide. C'est le cumul qui tranche.
Un business present dans 2+ canaux = francite quasi certaine.

## Pipeline en 6 etapes

ETAPE 0 - CONFIG. Lire data/money_keywords_thailand.json (ou creer
l'equivalent pour une autre destination en validant les volumes via
DataForSEO AVANT, jamais a l'instinct), data/verticales.json,
data/blocklist_domains.txt. Definir zone = {pays, villes[]}.

ETAPE 1 - COLLECTE, 3 canaux. Details d'execution: references/methode.md
section "Canaux".
- A. Annuaires communautaires (UFE, rawai.fr, CCI...): web fetch + parsing.
  Attrape les invisibles du web. S'il n'existe pas d'annuaire pour la zone,
  continuer avec B et C (degradation normale).
- B. SERP inversee: pour chaque money keyword, SERP organic live (depth 20-30,
  langue fr, location pays cible ET pays source selon le keyword). Tout
  domaine organique ou local_pack HORS blocklist en position 2-50 = entite.
  C2 et C3 sont garantis par construction.
- C. Google Maps via Apify compass/crawler-google-places: requetes FR
  neutres par ville x verticale, language=fr, maxReviews=10. Le signal cle
  est reviews[].originalLanguage (% d'avis FR) + la langue des reponses du
  gerant. Attrape les business sans site (prospects GBP-only).

ETAPE 2 - FUSION. Cle primaire = domaine racine normalise. Fallback pour
les sans-site: slug(nom) avec containment match. Script:
scripts/score_prospects.py fait fusion + scoring d'un coup.

ETAPE 3 - SCORING FRANCITE. Bareme fige dans le script (parametres
ajustables en tete de fichier). Seuil: >= 5 prospect, 3-4 a verifier
manuellement, < 3 exclu. Flag OPPORTUNITE_LANGUE si francite >= 5 et site
non-FR (gerant francais invisible en francais = argumentaire premium).

ETAPE 4 - QUALIFICATION SEO. Pour chaque entite passee au seuil ET ayant
un site: DataForSEO domain_rank_overview (langue fr, location = pays
SOURCE de la clientele, ex France). Classer: invisible / gbp_only /
sous_performant / emergent / deja_gagnant. Les deja_gagnant sont ECARTES
et listes a part comme references concurrentes.

ETAPE 5 - SCORING FINAL + TIERS. tier = f(valeur verticale, besoin,
francite, profil SEO). Regles exactes dans le script. Sorties possibles:
T1 (attaquer maintenant), T2 (pipeline), T3 / T3_A_VERIFIER (opportuniste
/ francite incomplete), A_QUALIFIER (francite OK mais besoin SEO PAS
confirme par DataForSEO: ne jamais demarcher avec un angle non prouve),
T1_VOLUME_A_VALIDER (verticale forte sans money keyword valide),
CONCURRENT_LOCAL (agence web/SEO du coin: change l'angle, ne pas cacher),
CONCURRENT_REF (deja gagnant), EXCLU.

ETAPE 6 - OUTPUT BUSINESS. Produire:
1. prospects.json : sortie machine complete (schema dans references/
   format-sortie.md), pour pipeline W4. Chaque prospect porte deja:
   offre_recommandee, prix_conseille (vide, a fixer), niveau_confiance,
   a_verifier_avant_contact, gbp_issue, volume_fr_valide.
2. 1 fiche MD par prospect T1 via scripts/build_fiche.py. La fiche SEPARE
   faits prouves / hypotheses / a verifier, propose l'offre Kumo, et laisse
   le prix en [A FIXER] (le prix se decide au cas par cas, jamais en dur).
3. Optionnel: un tableau humain trie par priorite (prospect, ville,
   verticale, preuve FR, probleme SEO, angle, offre, confiance) si demande.

REGLE PRIX: le skill ne fixe JAMAIS de prix automatiquement. Il propose
l'offre et la structure; le montant depend du positionnement, de la marge
et du client. Champs prix livres vides.

## Ordre d'execution type (zone deja configuree)
1. Lancer canal C (Apify) en premier: ~100s par run, le plus lent.
2. Pendant ce temps, canal B (SERP) et canal A (annuaires).
3. Construire entities_raw.json (un objet par observation par canal).
4. python3 scripts/score_prospects.py entities_raw.json > scored.json
5. Qualification DataForSEO des candidats avec site, injecter les profils
   seo dans le json (champ seo_profile), relancer le script en mode final.
6. python3 scripts/build_fiche.py scored_final.json <slug> pour chaque T1
   (le fichier money_keywords est charge par defaut; un 3e argument permet
   d'en pointer un autre pour une destination differente).

## Garde-fous
- Couts: ~0.007 compute unit Apify par fiche avec 10 avis; DataForSEO
  domain overview = centimes. Un scan ville complet (5 verticales x 20
  fiches + 15 SERP + 25 domain overviews) reste sous quelques dollars.
- Ne jamais elargir maxReviews au-dela de 10-15: le signal langue sature vite.
- Blocklist = agregateurs, OTA, medias, blogs metropole. Les residus
  ambigus (media local, TO base en France) se jugent au cas par cas:
  la cible est un business OPERANT dans la zone, pas un site qui en parle.
- Detecter les agences SEO/web locales croisees en chemin (categorie
  "Web Design / SEO", valeur verticale negative) et les sortir en
  CONCURRENT_LOCAL (jamais EXCLU, jamais prospect). Un concurrent local
  change l'angle de vente: "vous avez deja des agences locales mais elles
  vendent du site; moi je vous montre les requetes FR ratees".
- RGPD/demarchage: les emails viennent d'annuaires professionnels publics
  publies pour etre contactes. Rester en B2B, mentionner la source.

## Fichiers du skill
- references/methode.md : methode complete, baremes, procedures par canal,
  cas limites. A LIRE avant un premier scan ou pour adapter a un nouveau pays.
- references/format-sortie.md : schemas entities/prospects + template fiche.
- scripts/score_prospects.py : fusion + francite + tiers (deterministe).
- scripts/build_fiche.py : genere la fiche argumentaire MD d'un prospect.
- data/money_keywords_thailand.json : clusters valides par la donnee (volumes
  DataForSEO, juin 2026). Modele a dupliquer pour une autre destination.
- data/verticales.json : valeur budget par verticale (1-5).
- data/blocklist_domains.txt : domaines a ignorer en canal B.
