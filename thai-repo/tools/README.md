# tools/ — mail Infomaniak (ENVOI REEL + brouillons + lecture)

Permet aux routines Thai et a tes sessions Claude d'**envoyer des emails**, **deposer des
brouillons** et **lire les mails** de la boite Infomaniak `thomas.puglisi@kumo-seo.ch`.

⚠️ Difference majeure avec le repo suisse : ce connecteur expose `envoyer_email`, qui envoie
REELLEMENT (action `"send"` de l'API kMail, meme route que les brouillons). Les garde-fous
sont dans `CLAUDE.md` (T1 only, checklist bloquante) et dans le serveur lui-meme : un fichier
**`PAUSE`** a la racine du repo fait refuser tout envoi (un brouillon est cree a la place).

Tout passe par l'**API mail HTTPS** d'Infomaniak (kMail), donc ca marche **depuis l'app web et
les routines nocturnes** (le HTTPS/443 sort du cloud ; l'IMAP/993 non).

## A faire UNE fois : le jeton API
1. manager.infomaniak.com -> **Developpeur / Jetons API** -> nouveau jeton, scope **`mail`**.
2. Expose-le en variable d'environnement **`INFOMANIAK_API_TOKEN`** cote environnement de la
   routine. En local : dans un fichier `.env` (voir `.env.example`).

## 1. Connecteur MCP `infomaniak-mail` (LA voie principale)

Declare dans **`.mcp.json`** a la racine du repo. Code : `infomaniak_mcp.py` (pur Python,
zero dependance, increvable). Outils exposes :

| Outil                 | Role                                                                  |
| --------------------- | --------------------------------------------------------------------- |
| `lister_boites`       | les boites accessibles (email + uuid)                                 |
| `lister_dossiers`     | dossiers de la boite (INBOX, Brouillons, Envoyes...) + id/role        |
| `envoyer_email`       | **ENVOI REEL** (`to`, `objet`, `corps`) — refuse si fichier `PAUSE`   |
| `creer_brouillon`     | depose un brouillon (`to`, `objet`, `corps`, `cc?`, `html?`)          |
| `supprimer_brouillon` | supprime un brouillon par son uuid                                    |
| `lister_messages`     | entetes d'un dossier (expediteur, objet, date, uid)                   |
| `lire_message`        | contenu complet d'un message (par `uid`)                              |

`envoyer_email` et `creer_brouillon` partagent les memes regles de rendu : corps en TEXTE
BRUT avec accents, un paragraphe par ligne vide ; le serveur met en page en HTML et ajoute
la signature (`signature.html`) ; un pied "Thomas / KUMO..." deja present est retire (jamais
de double signature).

Test du protocole (sans token) :
```bash
printf '%s\n' \
 '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{}}}' \
 '{"jsonrpc":"2.0","id":2,"method":"tools/list"}' | python3 tools/infomaniak_mcp.py
```

## 2. Scripts en ligne de commande (meme API, hors connecteur)

`infomaniak_draft_api.py` — brouillon par defaut, envoi reel avec `--send` :
```bash
python3 tools/infomaniak_draft_api.py --to x@y.ch --subject Test --body "Bonjour," --dry-run
python3 tools/infomaniak_draft_api.py --list-mailboxes              # verifie le jeton
python3 tools/infomaniak_draft_api.py --to toi@x.ch --subject "Test envoi" \
  --body "Bonjour," --html --send                                   # ENVOI REEL (test)
```
C'est la commande du TEST D'ENVOI initial (cf. README racine, etape 5) : a faire vers ta
propre adresse avant d'activer les routines.

## 3. Repli IMAP `infomaniak_draft.py` (hors cloud uniquement)

IMAP `APPEND` + flag `\Draft`. **Ne marche pas depuis le cloud/web** (port 993 bloque).
Reserve a une machine perso, en secours si l'API kMail change un jour.

## Format "fiche" & .env

- Les scripts CLI lisent le format des fiches Notion : 1re ligne `Objet : ...`, ligne vide,
  puis le corps.
- `.env` (local seulement, gitignore) : `cp tools/.env.example .env`. En cloud, les memes
  variables se mettent cote environnement de la routine.

## Note sur l'API kMail
La route `POST /api/mail/{mailboxUuid}/draft` (action `save` = brouillon, `send` = envoi)
vient des apps officielles **kMail** open source (github.com/Infomaniak/android-kMail).
Stable en prod mais pas dans le portail developpeur public. Si l'action `send` reclame une
identite, le code resout automatiquement la signature par defaut de la boite et retente.
Repli prevu (IMAP/SMTP) si ces routes changent.
