---
name: audit-prospect
description: >
  Produit un audit SEO approfondi et gap-driven d'un prospect KUMO, en vue d'un Diagnostic
  payant ou d'un contact a forte valeur. A utiliser quand l'utilisateur demande "audit
  <entreprise>", "fais l'audit de <prospect>", "prepare le Diagnostic de <prospect>", ou
  veut comprendre precisement l'ecart SEO d'un prospect et ce que KUMO peut lui apporter.
  Croise positions reelles, volumes, difficulte, autorite, pages existantes et SERP
  local + organique pour isoler des actions concretes, chiffrees et DANS le perimetre KUMO.
  Ne pas utiliser pour la qualification de masse nocturne (ca, c'est CLAUDE.md / la routine).
---

# Mode audit prospect (KUMO)

But : transformer des donnees en un diagnostic actionnable. Pas un constat vague
("vous manquez de visibilite") mais un ecart decompose en causes precises, chiffre, et
relie a des actions que KUMO sait faire. Tu ne proposes JAMAIS ce qui est hors perimetre.

## Perimetre KUMO (ce qu'on peut vendre)
- Creation et optimisation de pages (par ville, par prestation), on-page, structure.
- Sante technique (vitesse, balises, indexation), refonte si besoin.
- Google Business Profile / pack local.
- Suivi mensuel (execution continue).
HORS perimetre : netlinking / acquisition de backlinks. L'autorite est donc un CONSTAT
(pour expliquer un ecart), jamais une action vendue.

## Entrees
- Le prospect : nom, domaine, ville, Place ID si dispo (souvent deja dans Notion).
- Si l'audit suit la qualification : reprends la fiche Notion existante.

## Process (ordre conseille)

### 1. Definir le perimetre de mots-cles
- Requete coeur : "metier ville" du prospect (ex. "paysagiste La Chaux-de-Fonds").
- 2-3 villes voisines a fort potentiel (ex. Neuchatel, Yverdon).
- 3-6 prestations du metier (ex. creation de jardin, terrasse, muret, elagage, arrosage).

### 2. Chiffrer le marche
- kw_data_google_ads_search_volume (ou dataforseo_labs_google_keyword_suggestions sur le
  metier) sur Switzerland / fr : volume mensuel + saisonnalite + CPC de chaque requete cible.
- Repere les pics (ex. paysagiste = pic printemps) : ca cale le TIMING du contact.
- Note l'intention (search_intent) : transactional/commercial = prioritaire ;
  informational = trafic mais peu de clients ; navigational = recherche de marque.

### 3. Mesurer ce que le prospect capte (les 2 axes)
- dataforseo_labs_google_ranked_keywords sur le domaine (Switzerland, fr, order by
  search_volume desc, filtre search_volume > 0) : ses mots-cles, leur POSITION, et surtout
  l'URL qui ranke pour chacun (page dediee vs page d'accueil).
- dataforseo_labs_google_domain_rank_overview : etendue globale (nb de mots-cles, trafic estime).
- serp_organic_live_advanced (device mobile) sur la requete coeur (et 1-2 voisines) :
  position dans le PACK LOCAL (Maps/GBP) ET en ORGANIQUE, + qui est devant.
  (location_name exact via serp_locations, country CH.)

### 4. Profil concurrent (qui capte ce qu'il rate)
- Depuis le SERP : note les 3 du pack local + le top organique.
- Option : dataforseo_labs_google_competitors_domain (ou serp_competitors) pour la force des concurrents.

### 5. Autorite (CONSTAT uniquement)
- ranked_keywords te donne, par mot-cle, avg_backlinks_info.referring_domains = l'autorite
  MOYENNE necessaire pour ranker dessus. Compare-la a l'autorite du prospect (referring
  domains de son domaine, visible dans le meme bloc ou via backlinks_summary).
- Conclus : son autorite SUFFIT-elle pour les cibles visees ? Si oui, le frein est ailleurs
  (on-page, page manquante) = perimetre KUMO. Si non (cible trop dure), on NE la vise pas.

### 6. Sante technique
- on_page_instant_pages sur la home + 1-2 pages cles : score, balises, H1, dom_complete.
- Lighthouse (on_page_lighthouse) seulement si un chiffre de vitesse est utile a l'argumentaire.

## Les croisements qui font l'audit (le coeur)
1. POSITIONS x VOLUMES x DIFFICULTE = quick wins.
   Mots-cles ou il est en page 2 (positions 11-20) ET a fort volume ET difficulte basse =
   gains rapides. C'est l'argument le plus vendeur.
2. PAGES EXISTANTES x REQUETES CAPTEES = pages manquantes.
   Regarde l'URL qui ranke pour chaque requete. S'il a une page dediee la ou il gagne, et
   qu'il s'appuie sur sa home la ou il echoue, la page dediee manquante EST la cause.
   (Cas reel Vurlod : page dediee Yverdon = page 1 ; pas de page Neuchatel = ~22e, via la home.)
3. AUTORITE REQUISE x AUTORITE REELLE = nature du frein.
   Si son autorite depasse la moyenne du mot-cle mais qu'il ne ranke pas : le frein est
   on-page/contenu (KUMO sait faire). Si son autorite est sous la moyenne sur une cible dure :
   c'est du netlinking (hors perimetre) -> on ne vise pas cette cible.
4. PACK LOCAL x ORGANIQUE = quel levier.
   Absent du pack mais present en organique -> levier GBP. Present pack, absent organique ->
   levier pages/contenu. Present sur sa ville mais absent du marche voisin -> levier croissance.

## Traduire en plan (ce que KUMO apporte)
Pour CHAQUE gap retenu : action concrete + levier KUMO + enjeu chiffre (volume x intention) +
faisabilite (difficulte, autorite, modele interne reproductible) + ordre de priorite.
Priorise les quick wins (fort volume, faible difficulte, autorite deja suffisante) en premier.
Rattache a une offre : Creation, page(s), refonte technique, GBP -> Diagnostic 1200 comme
porte d'entree (formalise le plan), puis Suivi pour l'execution.

## Sortie
- Remplis le gabarit audit-TEMPLATE.md (un fichier par prospect dans prospects/AAAA-MM-JJ/).
- Optionnel : mets a jour la fiche Notion du prospect (champ "Probleme principal" = l'ecart
  chiffre + l'action n1 ; "Offre KUMO" = porte d'entree).

## Regles d'honnetete (a ecrire dans l'audit)
- Positions, trafics et difficulte sont des ESTIMATIONS DataForSEO (modeles), pas les
  analytics reels du prospect.
- Tout "quick win" / "impact estime" est une PROJECTION etayee, jamais une garantie.
- Ne vise que des cibles atteignables dans le perimetre KUMO. Dis franchement ce qui
  necessiterait du netlinking (et qu'on ne le fait pas).
- Ne jamais inventer un chiffre. Si une donnee manque, dis-le.

## Cout
Plus lourd que la qualification : compte ~0,30 a ~2 CHF de data DataForSEO par audit
(ranked_keywords, keyword data, SERP, OnPage, eventuellement backlinks). A reserver aux
prospects chauds ou au moment de preparer un Diagnostic.
