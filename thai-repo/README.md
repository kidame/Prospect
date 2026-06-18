# prospect-thai -- Machine a prospects THAI (KUMO expat)

Machine de prospection 100% autonome pour les business francophones de Thailande :
qualification (methode 3 canaux), redaction, ENVOI AUTOMATIQUE des emails (Infomaniak),
detection des reponses, relance J+7. Le cerveau est `CLAUDE.md` ; les deux routines sont
`ROUTINE_THAI_PROMPT.md` (02:00) et `RELANCE_THAI_PROMPT.md` (05:00).

⚠️ Ce contenu a ete construit dans le repo `prospect` (dossier `thai-repo/`) puis livre en
zip. Il est concu pour vivre A LA RACINE du repo `prospect-thai`.

## Si tu es Claude Code, ouvert sur le repo prospect-thai, avec ce contenu en zip

1. Decompresse TOUT le contenu du zip a la RACINE du repo (y compris les fichiers caches :
   `.claude/`, `.story/`, `.mcp.json`, `.gitignore`). Rien ne doit rester dans un sous-dossier.
2. Lis `CLAUDE.md` en entier : c'est le cerveau du repo (methode, garde-fous d'envoi,
   mapping Notion, Storybloq). Les regles d'envoi automatique sont NON NEGOCIABLES.
3. Commit + push sur `main` ("Machine a prospects Thai - import initial").
4. Verifie le connecteur : `printf` du test protocole dans `tools/README.md` (7 outils dont
   `envoyer_email`), puis `python3 tools/infomaniak_draft_api.py --list-mailboxes` si
   INFOMANIAK_API_TOKEN est present.
5. Si `tools/signature.html` est encore vide, signale-le a Kidam (etape 5 ci-dessous) AVANT
   tout test d'envoi.
6. Propose a Kidam le TEST D'ENVOI (etape 6 ci-dessous) vers SA propre adresse -- jamais un
   prospect -- et attends sa confirmation de reception avant de considerer l'envoi valide.
7. Termine par un handover Storybloq (`--slug dev-import`) et indique a Kidam les etapes
   restantes : variable d'environnement + creation des 2 routines (etapes 3, 5 et 7 ci-dessous).

## Migration / mise en route (Kidam, ~10 min)

1. Creer le repo GitHub vide `prospect-thai` (prive). [FAIT le 2026-06-11]
2. Copier TOUT le contenu a la RACINE du nouveau repo (y compris `.claude/`, `.story/`,
   `.mcp.json`, `.gitignore`), commit, push sur `main` (voir section Claude Code ci-dessus).
3. Sur claude.ai/code : creer un ENVIRONNEMENT pour `prospect-thai` avec la variable
   `INFOMANIAK_API_TOKEN` (le meme jeton API scope "mail" que le repo suisse) et l'acces
   reseau necessaire (Apify, DataForSEO, Notion, mail.infomaniak.com).
4. Memoire Storybloq : `.story/` est DEJA initialise dans ce dossier (projet
   "prospect-thai", vierge) -- il suffit de le copier avec le reste. Ne pas re-init.
5. ⚠️ REMPLIR `tools/signature.html` (signature HTML : Thomas / KUMO - kumo-seo.ch / tel).
   Le fichier est VIDE aujourd'hui : en envoi automatique, les mails partiraient SANS
   signature. La copier depuis le repo suisse si elle y a ete remplie, sinon l'ecrire
   (quelques lignes de HTML simple suffisent).
6. TEST D'ENVOI OBLIGATOIRE avant toute routine (valide l'API kMail action=send ET la
   signature de l'etape 5) :
   ```
   python3 tools/infomaniak_draft_api.py --to TON_ADRESSE --subject "Test envoi Thai" \
     --body-stdin --html --send <<'EOF'
   Bonjour,

   Test de l'envoi reel (accents : e accent aigu, c cedille).

   Thomas
   EOF
   ```
   Verifier : reception, rendu des paragraphes, accents, UNE seule signature.
   (En cas d'echec "identity", le code retente avec l'identite par defaut de la boite ;
   si ca echoue encore, ouvrir tools/infomaniak_draft_api.py::send_email.)
7. Creer les 2 routines sur claude.ai/code/routines en collant les bootstraps de
   `ROUTINE_THAI_PROMPT.md` (02:00 Europe/Zurich) et `RELANCE_THAI_PROMPT.md` (05:00),
   mode de permission AUTONOME/bypass dans l'UI.
8. Premier run : suivre la section "Apres le premier run, a verifier" des deux prompts.
   Les 2 premieres semaines, relire chaque mail envoye dans le recap quotidien.

## Kill-switch

Creer un fichier `PAUSE` a la racine du repo = plus AUCUN envoi (les mails partent en
brouillon a la place ; la regle est appliquee par le serveur MCP lui-meme). Le supprimer
pour reactiver.

## Base Notion

La base "Prospects Thai" (separee de la base Contacts suisse) est le CRM + dedup + archive
des mails envoyes. DEJA CREEE le 2026-06-11 sous "KUMO · Back-office" :
https://app.notion.com/p/62f4217643814fa88a2f6f286b2e66a5
Schema dans `CLAUDE.md`, section "Mapping Notion".
