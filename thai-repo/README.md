# prospect-thai -- Machine a prospects THAI (KUMO expat)

Machine de prospection 100% autonome pour les business francophones de Thailande :
qualification (methode 3 canaux), redaction, ENVOI AUTOMATIQUE des emails (Infomaniak),
detection des reponses, relance J+7. Le cerveau est `CLAUDE.md` ; les deux routines sont
`ROUTINE_THAI_PROMPT.md` (02:00) et `RELANCE_THAI_PROMPT.md` (05:00).

⚠️ Ce dossier a ete construit dans le repo `prospect` (dossier `thai-repo/`) parce que la
session n'avait pas acces a un repo separe. Il est concu pour devenir UN REPO AUTONOME.

## Migration vers le repo autonome (a faire une fois, ~10 min)

1. Creer le repo GitHub vide `prospect-thai` (prive).
2. Copier TOUT le contenu de ce dossier `thai-repo/` a la RACINE du nouveau repo
   (y compris `.claude/`, `.mcp.json`, `.gitignore`), commit, push sur `main`.
3. Sur claude.ai/code : creer un ENVIRONNEMENT pour `prospect-thai` avec la variable
   `INFOMANIAK_API_TOKEN` (le meme jeton API scope "mail" que le repo suisse) et l'acces
   reseau necessaire (Apify, DataForSEO, Notion, mail.infomaniak.com).
4. Memoire Storybloq : `.story/` est DEJA initialise dans ce dossier (projet
   "prospect-thai", vierge) -- il suffit de le copier avec le reste. Ne pas re-init.
5. TEST D'ENVOI OBLIGATOIRE avant toute routine (valide l'API kMail action=send) :
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
6. Creer les 2 routines sur claude.ai/code/routines en collant les bootstraps de
   `ROUTINE_THAI_PROMPT.md` (02:00 Europe/Zurich) et `RELANCE_THAI_PROMPT.md` (05:00),
   mode de permission AUTONOME/bypass dans l'UI.
7. Premier run : suivre la section "Apres le premier run, a verifier" des deux prompts.
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
