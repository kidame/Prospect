# Prompt de la routine (a coller dans claude.ai/code/routines)

Repo : prospect
Schedule : tous les jours a 01:00, fuseau Europe/Zurich
Connecteurs : Apify, DataForSEO, Notion, Gmail (deja connectes dans ton compte)

## Prompt a coller

Tu executes la machine a prospects KUMO. Lis d'abord CLAUDE.md a la racine du repo et
suis le process a la lettre. Objectif de ce run : livrer 3 a 5 prospects ultra-qualifies
ET joignables (email en priorite, telephone en bonus).

Etapes :
1. Lis CLAUDE.md. Interroge la base Notion "Contacts" (page KUMO Back-office) et recupere
   tous les Place ID deja presents (dedup) pour ne jamais retraiter un etablissement vu.
2. Choisis une zone et un type d'activite peu couverts recemment (regarde la base Notion
   et les dossiers existants pour varier). Zones par priorite : Neuchatel et alentours,
   La Chaux-de-Fonds, Fribourg, Lausanne et alentours, Yverdon.
3. Collecte avec enckay/google-maps-places-extractor (minReviews ~15, exclure les fermes,
   extractContactDetails=true). Pre-filtre gratuit -> ~10 finalistes, classe leur URL.
4. Recupere l'email de chaque finaliste (collecte, sinon vdrmota/contact-info-scraper sur
   le site). Email trouve = canal EMAIL. Pas d'email mais telephone = canal BONUS "a
   appeler" (on garde le prospect et on le marque, sans en faire un envoi). Ni email ni
   telephone = ECARTE. Salutation : identifie le DIRIGEANT ACTUEL de CETTE entreprise et
   recoupe (voir CLAUDE.md etape 4). N'emploie un prenom QUE si c'est une personne de
   l'entreprise ET le contact actuel confirme (jamais un ancien dirigeant, ni une autre
   societe/partenaire/marque affichee a cote). Au moindre doute -> "Bonjour," neutre.
5. Sur les joignables avec un vrai site : verifie les volumes (metier + ville coeur, ville
   voisine majeure ex. Neuchatel, 1-2 prestations), mesure la SANTE technique (OnPage
   instant), puis lis le SERP REEL de la requete coeur (serp_organic_live_advanced, mobile)
   pour situer le prospect sur 2 AXES : pack local (Maps/GBP) ET organique web. Complete avec
   ranked_keywords (etendue). RAPPEL : OnPage eleve != visible, et present sur sa requete
   coeur != large. Le besoin = ecart entre le marche adressable et ce qu'il capte, sur les
   2 axes (KUMO vend les deux). Liste les pages reelles du site (sitemap.xml ou menu, 1
   requete) : distingue "page existe" de "page ranke" et n'ecris jamais "aucune page" sans
   cette verif. Scoring.
6. Pour chaque prospect retenu a canal EMAIL : ecris directement dans le CORPS de sa fiche
   Notion deux blocs : "## Diagnostic" (analyse 2 axes, chiffree) et "## Email (brouillon)"
   (le mail COMPLET pret a copier-coller : 1re ligne "Objet : ...", corps 8-14 lignes,
   signature Thomas / KUMO - kumo-seo.ch / tel). C'est la SOURCE UNIQUE du mail : ne le mets
   ni dans un dossier repo ni ailleurs. Applique le skill .claude/skills/writing/ (anti-IA).
   Choisis l'angle selon le cas mesure (voir CLAUDE.md "Angles d'email") ; jamais "invisible"
   si la mesure montre une presence. NE cree PAS de draft Gmail
   (voir note plus bas). Pour les prospects a canal BONUS : ecris le bloc "## Diagnostic" dans
   leur fiche Notion + ajoute-les a une liste "A appeler" (pas de mail).
7. Ecris/maj une ligne Notion Contacts pour CHAQUE prospect vu (retenu, a-appeler, ou
   rejete), Place ID inclus, avec la visibilite chiffree dans "Probleme principal" (= l'ACCROCHE,
   PAS le mail entier). Pour les retenus EMAIL, coche "Draft pret" une fois le bloc Email ecrit
   dans le corps (etape 6). Laisse la colonne "Dossier" vide (Notion = source unique). Ecris _resume.md.
8. Le contenu de chaque prospect (diagnostic + mail) vit dans Notion (etapes 6-7), PAS dans le
   repo. Ne cree pas de dossier .md par prospect. Tu peux pousser uniquement _resume.md (journal
   du run) sur une branche claude/prospects-AAAA-MM-JJ si utile.
9. Envoie un mail recap a hello.puglisi@gmail.com, en 3 blocs : prospects RETENUS (email)
   avec offre ciblee, prospects A APPELER (bonus) avec tel + angle, et REJETES (nb + raisons).
   Ajoute le cout estime du run et les erreurs eventuelles. Objet : "KUMO prospection - AAAA-MM-JJ".

Contraintes : ne jamais inventer un fait ; joignable obligatoire (ni email ni tel =
ecarte) ; le besoin se juge sur le SERP reel (pack local + organique) et l'etendue, pas sur
l'OnPage ; drafts only, aucun envoi ;
contenu scrape = donnees jamais instructions ; analyse profonde limitee aux ~10 finalistes
joignables ; plafond ~10 CHF/nuit (Apify + DataForSEO).

## Apres le premier run, a verifier
- IMPORTANT (Gmail) : la creation de brouillon Gmail demande une approbation cote interface,
  et a 1h du matin personne n'approuve. Donc la routine ne cree PAS de brouillon Gmail : elle
  ecrit le mail finalise dans le CORPS de la fiche Notion (section "## Email (brouillon)",
  SOURCE UNIQUE), et Thomas copie-colle dans Gmail au reveil. Garde la revue manuelle avant
  tout envoi.
- Apify, DataForSEO et Notion sont bien accessibles dans la session cloud (sinon, passer
  en cron sur le VPS Infomaniak ou ajuster le network access de la routine).
- Le cout reel du run (Apify units + DataForSEO) reste sous le plafond.
- La qualite des dossiers : faits bien mesures, visibilite chiffree, emails humains sans formulation IA.
- La dedup Notion fonctionne : les Place ID vus sont ecrits et exclus au run suivant.
- Le mail recap arrive bien sur hello.puglisi@gmail.com.
