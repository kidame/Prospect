# tools/ — mail Infomaniak (brouillons + lecture)

Permet a la routine et a tes sessions Claude de **deposer des brouillons** et **lire les mails**
dans la boite Infomaniak `thomas.puglisi@kumo-seo.ch`. Aucun envoi automatique : `creer_brouillon`
pose un brouillon (`action: "save"`), la revue/envoi reste manuel.

Tout passe par l'**API mail HTTPS** d'Infomaniak (kMail), donc ca marche **depuis l'app web et la
routine nocturne** (le HTTPS/443 sort du cloud ; l'IMAP/993 non).

## A faire UNE fois : le jeton API
1. manager.infomaniak.com -> **Developpeur / Jetons API** -> nouveau jeton, scope **`mail`**.
2. Expose-le en variable d'environnement **`INFOMANIAK_API_TOKEN`** cote routine/environnement
   (meme endroit que les autres secrets). En local : dans un fichier `.env` (voir `.env.example`).

Le mot de passe IMAP ne sert PAS a cette API ; il ne reste utile que pour le repli IMAP.

## 1. Connecteur MCP `infomaniak-mail` (LA voie principale)

Declare dans **`.mcp.json`** a la racine du repo. Claude Code le lance tout seul dans
l'environnement cloud (et en routine, sans approbation). Code : `infomaniak_mcp.py` (pur Python,
zero dependance, increvable). Outils exposes dans l'app Claude :

| Outil              | Role                                                            |
| ------------------ | -------------------------------------------------------------- |
| `lister_boites`    | les boites accessibles (email + uuid)                          |
| `lister_dossiers`  | dossiers de la boite (INBOX, Brouillons, Envoyes...) + id/role |
| `creer_brouillon`  | depose un brouillon (`to`, `objet`, `corps`, `cc?`, `html?`)   |
| `lister_messages`  | entetes d'un dossier (expediteur, objet, date, uid)            |
| `lire_message`     | contenu complet d'un message (par `uid`)                       |

Une fois le jeton en place, tu peux juste demander en discussion : « dépose le brouillon de
<prospect> » ou « lis mes derniers mails », et la routine peut creer le brouillon apres avoir
ecrit la fiche Notion.

Test du protocole (sans token) :
```bash
printf '%s\n' \
 '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{}}}' \
 '{"jsonrpc":"2.0","id":2,"method":"tools/list"}' | python3 tools/infomaniak_mcp.py
```

## 2. Scripts en ligne de commande (meme API, hors connecteur)

`infomaniak_draft_api.py` — le meme depot de brouillon en CLI (utile pour tester / scripter) :
```bash
python3 tools/infomaniak_draft_api.py --to x@y.ch --subject Test --body "Bonjour," --dry-run
python3 tools/infomaniak_draft_api.py --list-mailboxes            # verifie le jeton
python3 tools/infomaniak_draft_api.py --to prospect@x.ch --from-file mail.txt
```

## 3. Repli IMAP `infomaniak_draft.py` (hors cloud uniquement)

IMAP `APPEND` + flag `\Draft`. **Ne marche pas depuis le cloud/web** (port 993 bloque par le
proxy). Reserve au VPS / machine perso, en secours si l'API mail kMail change un jour.
Config : `INFOMANIAK_IMAP_PASSWORD` (+ `INFOMANIAK_IMAP_USER`, defaut `thomas.puglisi@kumo-seo.ch`).
```bash
python3 tools/infomaniak_draft.py --to prospect@x.ch --from-file mail.txt
python3 tools/infomaniak_draft.py --list-folders
```

## Format "fiche" & .env

- Les scripts CLI lisent le format du bloc `## Email (brouillon)` des fiches Notion : 1re ligne
  `Objet : ...`, ligne vide, puis le corps. On colle le contenu Notion tel quel.
- `.env` (local seulement, gitignore) : `cp tools/.env.example .env`, remplis les secrets. En
  cloud, les memes variables se mettent cote environnement de la routine (pas de `.env`).

## Note sur l'API kMail
La route `POST /api/mail/{mailboxUuid}/draft` (et les routes de lecture) viennent des apps
officielles **kMail** open source (github.com/Infomaniak/android-kMail). Elles ne sont pas dans
le portail developpeur public (qui ne couvre que l'admin des boites) mais sont stables en prod.
Repli prevu (IMAP) si elles changent.
