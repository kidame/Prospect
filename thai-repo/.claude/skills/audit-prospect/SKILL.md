---
name: audit-prospect
description: >
  Produit un audit SEO approfondi et gap-driven d'un prospect THAI (business francophone
  en Thailande), en vue d'un appel de closing ou d'un contact a forte valeur. A utiliser
  quand l'utilisateur demande "audit <entreprise>", "fais l'audit de <prospect>", "prepare
  l'appel avec <prospect>" (typiquement un Lead chaud qui a repondu), ou veut comprendre
  precisement l'ecart SEO d'un prospect et ce que KUMO peut lui apporter. Croise positions
  reelles sur les requetes FR, volumes, difficulte, autorite, pages existantes et SERP
  France + Thailande pour isoler des actions concretes, chiffrees et DANS le perimetre
  KUMO. Ne pas utiliser pour la qualification de masse nocturne (ca, c'est CLAUDE.md /
  la routine + le skill machine-prospects-expat).
---

# Mode audit prospect (KUMO Thai)

But : transformer des donnees en un diagnostic actionnable, typiquement pour PREPARER
L'APPEL avec un Lead chaud (un prospect qui a repondu au mail). Pas un constat vague
("vous manquez de visibilite") mais un ecart decompose en causes precises, chiffre, et
relie a des actions que KUMO sait faire. Tu ne proposes JAMAIS ce qui est hors perimetre.

## Perimetre KUMO (ce qu'on peut vendre)
- Creation et optimisation de pages FR (par prestation, par ville/zone), on-page, structure.
- Version francaise d'un site anglophone (l'angle OPPORTUNITE_LANGUE pousse jusqu'au devis).
- Sante technique (vitesse, balises, indexation), refonte si besoin.
- Google Business Profile (fiche, lien casse vers Facebook, avis).
- Suivi mensuel (execution continue).
HORS perimetre : netlinking / acquisition de backlinks. L'autorite est donc un CONSTAT
(pour expliquer un ecart), jamais une action vendue.
PRIX : JAMAIS fixes par l'audit (regle du repo). L'audit chiffre l'ENJEU (volumes,
positions) ; le montant, c'est Kidam, au cas par cas. Champs prix livres en [A FIXER].

## Entrees
- Le prospect : nom, domaine, ville, verticale (tout est deja dans sa fiche Notion
  "Prospects Thai" : Diagnostic, profil SEO, francite, mails echanges).
- Les money keywords de sa verticale : data/money_keywords_thailand.json du skill
  machine-prospects-expat (chaque kw porte son champ loc : FR ou TH).

## Process (ordre conseille)

### 1. Definir le perimetre de mots-cles
- Les money keywords de SA verticale (fichier du skill), + variantes par prestation et
  par ville/zone thaie. Tout NOUVEAU mot-cle : valider son volume AVANT de l'utiliser
  (jamais a l'instinct -- lecon fondatrice de l'etude Thailande).
- La regle des DEUX MARCHES : la clientele d'un business expat cherche depuis la FRANCE
  (avant-voyage, immobilier, visa, assurance) OU sur place en THAILANDE (excursions,
  nautisme, restaurants). Suis le champ loc du keyword ; en cas de doute, mesure les deux.

### 2. Chiffrer le marche
- kw_data_google_ads_search_volume, language fr, location France OU Thailand selon loc :
  volume mensuel + saisonnalite + CPC de chaque requete cible.
- Saisonnalite Thailande : pic de recherches FR avant la haute saison (sept-dec pour un
  voyage nov-fev). Ca cale le TIMING de l'argumentaire.
- Note l'intention (search_intent) : transactional/commercial = prioritaire ;
  informational = trafic mais peu de clients ; navigational = marque.
- Decote mentale de 20-30% sur les loanwords identiques FR/EN (yacht, catamaran,
  massage...) : le volume "langue fr" peut etre surestime.

### 3. Mesurer ce que le prospect capte
- dataforseo_labs_google_ranked_keywords sur son domaine (language fr, location France ;
  refais en location Thailand si sa verticale est "sur place") : ses mots-cles FR, leur
  POSITION, et surtout l'URL qui ranke (page dediee vs page d'accueil vs rien).
- dataforseo_labs_google_domain_rank_overview : etendue globale (nb mots-cles, trafic estime).
- serp_organic_live_advanced (language fr, depth 20-30) sur la requete coeur et 1-2
  voisines, dans le bon pays : QUI capte ce marche aujourd'hui (OTA ? blogs ? un
  concurrent francophone ? la SERP FR est-elle VIDE -- le cas en or) ?
- LANGUE DU SITE : verifie en VISITANT (jamais deduit) s'il existe une version FR.
  Site EN-only + SERP FR faible = OPPORTUNITE_LANGUE, l'argument principal de l'appel.

### 4. Profil concurrent (qui capte ce qu'il rate)
- Depuis le SERP : nomme les domaines devant lui (hors blocklist du skill : OTA,
  agregateurs, blogs metropole -- des intermediaires, pas des concurrents directs ;
  "vos clients tombent sur TripAdvisor, pas sur vous" est un argument, pas un concurrent).
- Option : dataforseo_labs_google_competitors_domain pour la force des vrais concurrents.

### 5. Autorite (CONSTAT uniquement)
- ranked_keywords donne, par mot-cle, avg_backlinks_info.referring_domains = l'autorite
  MOYENNE necessaire. Compare a la sienne (meme bloc, ou backlinks_summary).
- Conclus : son autorite SUFFIT-elle pour les cibles visees ? Si oui, le frein est
  ailleurs (page FR manquante, on-page) = perimetre KUMO. Si non, on NE vise PAS la cible.
- Particularite du marche : les SERP FR "thailande" sont souvent peu defendues (KD bas,
  peu de sites FR locaux) -- verifie au lieu de supposer la difficulte suisse.

### 6. Sante technique
- on_page_instant_pages sur la home + 1-2 pages cles : score, balises, H1, dom_complete,
  hreflang si site multilingue (un site EN/FR sans hreflang gaspille sa version FR).
- Lighthouse seulement si un chiffre de vitesse est utile a l'argumentaire.

## Les croisements qui font l'audit (le coeur)
1. POSITIONS x VOLUMES x DIFFICULTE = quick wins. Page 2 (11-20) + volume + difficulte
   basse = gains rapides. L'argument le plus vendeur (profil sous_performant).
2. PAGES EXISTANTES x REQUETES CAPTEES = pages manquantes. S'il ranke avec une page
   dediee la ou il gagne et s'appuie sur sa home (ou rien) la ou il echoue, la page
   manquante EST la cause.
3. LANGUE x MARCHE = l'angle expat. Site EN-only + demande FR mesuree + SERP FR vide =
   le gap le plus rentable du marche (OPPORTUNITE_LANGUE). Chiffre-le : somme des volumes
   FR de sa verticale qu'il ne peut PAS capter sans version FR.
4. AUTORITE REQUISE x AUTORITE REELLE = nature du frein (on-page = KUMO ; netlinking =
   hors perimetre, on ne vise pas).
5. GBP x SITE = trafic perdu betement : fiche Google qui pointe vers Facebook au lieu du
   site (gbp_issue), fiche sans site, avis sans reponse.

## Traduire en plan (ce que KUMO apporte)
Pour CHAQUE gap retenu : action concrete + levier KUMO + enjeu chiffre (volume x
intention) + faisabilite (difficulte, autorite) + priorite. Quick wins d'abord.
Rattache a l'offre du profil SEO (cf. skill : Sprint 90 jours / Fondation FR /
Acceleration / Site one-page + GBP), prix [A FIXER] par Kidam.

## Sortie
- Remplis le gabarit audit-TEMPLATE.md (le livrable de preparation d'appel).
- Mets a jour la fiche Notion "Prospects Thai" du prospect : enrichis le `## Diagnostic`
  (sans toucher aux sections `## Email envoye` / `## Relance envoyee`) et le champ Notes.

## Regles d'honnetete (a ecrire dans l'audit)
- Positions, trafics et difficulte sont des ESTIMATIONS DataForSEO, pas ses analytics.
- Tout "quick win" / "impact estime" est une PROJECTION etayee, jamais une garantie.
- Ne vise que des cibles atteignables dans le perimetre. Dis franchement ce qui
  necessiterait du netlinking (et qu'on ne le fait pas).
- Ne jamais inventer un chiffre. Si une donnee manque, ecris "non mesure".

## Cout
Plus lourd que la qualification : ~0,30 a ~2 CHF de data DataForSEO par audit. A reserver
aux Leads chauds (il a repondu : l'audit prepare l'appel) ou a une decision importante.
