# tools/

Petits utilitaires pour deposer les mails de la routine en BROUILLON dans la boite Infomaniak
(`thomas.puglisi@kumo-seo.ch`). Aucun envoi : la revue manuelle reste.

Deux voies, selon l'endroit ou ca tourne.

## 1. infomaniak_draft_api.py — API mail HTTPS (VOIE PRINCIPALE, marche depuis le web)

Cree le brouillon via l'API mail kMail en **HTTPS (443)**. Donc ca marche **depuis l'app web /
la routine nocturne cloud**, sans VPS ni pont.

```
POST https://mail.infomaniak.com/api/mail/{mailboxUuid}/draft
Authorization: Bearer <INFOMANIAK_API_TOKEN>
Body: {to, cc, bcc, subject, body, mime_type, action:"save"}
```

Cette route est celle des apps officielles **kMail** (open source, GPL : github.com/Infomaniak/
android-kMail). Elle n'est **pas** documentee sur le portail developpeur public (qui ne couvre
que l'admin des boites), mais elle est stable en pratique (la prod Infomaniak en depend). Si un
jour elle casse, le repli est l'IMAP (voir plus bas).

### A faire une fois : creer un jeton API
1. manager.infomaniak.com -> section **Developpeur / Jetons API** -> nouveau jeton, scope **mail**.
2. Ajoute-le comme variable d'environnement **`INFOMANIAK_API_TOKEN`** (cote routine/web : meme
   endroit que `INFOMANIAK_IMAP_PASSWORD` ; en local : dans `.env`).

### Usage
```bash
# voir la requete sans token ni reseau
python3 tools/infomaniak_draft_api.py --to x@y.ch --subject Test --body "Bonjour," --dry-run

# verifier le token + trouver le mailboxUuid
python3 tools/infomaniak_draft_api.py --list-mailboxes

# depuis le bloc Notion (1re ligne "Objet : ...", ligne vide, puis le corps)
python3 tools/infomaniak_draft_api.py --to prospect@exemple.ch --from-file mail.txt
```

| Variable                  | Role                                                | Defaut                       |
| ------------------------- | --------------------------------------------------- | ---------------------------- |
| `INFOMANIAK_API_TOKEN`    | jeton API scope `mail` (REQUIS)                     | —                            |
| `INFOMANIAK_MAIL_ADDRESS` | boite source (pour trouver le mailboxUuid)          | `thomas.puglisi@kumo-seo.ch` |
| `INFOMANIAK_MAILBOX_UUID` | force l'uuid (court-circuite la resolution auto)    | auto via l'API               |
| `INFOMANIAK_MAIL_API`     | host de l'API mail                                  | `https://mail.infomaniak.com`|

## 2. infomaniak_draft.py — IMAP APPEND (REPLI, hors cloud uniquement)

Depose le brouillon via IMAP `APPEND` + flag `\Draft`. **Ne marche PAS depuis le cloud/web** :
le port IMAP 993 y est bloque par le proxy (seul le HTTP/HTTPS sort). A n'utiliser que la ou le
993 est ouvert : VPS Infomaniak ou machine perso. Utile comme secours si l'API mail change.

```bash
python3 tools/infomaniak_draft.py --to prospect@exemple.ch --from-file mail.txt   # depose
python3 tools/infomaniak_draft.py --list-folders                                  # diag dossiers
python3 tools/infomaniak_draft.py --to x@y.ch --subject T --body "Bonjour," --dry-run
```

| Variable                   | Role                                   | Defaut                       |
| -------------------------- | -------------------------------------- | ---------------------------- |
| `INFOMANIAK_IMAP_PASSWORD` | mot de passe boite (REQUIS)            | —                            |
| `INFOMANIAK_IMAP_USER`     | login = adresse complete               | `thomas.puglisi@kumo-seo.ch` |
| `INFOMANIAK_FROM`          | From affiche                           | = l'adresse ci-dessus        |
| `INFOMANIAK_IMAP_HOST` / `INFOMANIAK_IMAP_PORT` | serveur / port            | `mail.infomaniak.com` / `993`|
| `INFOMANIAK_DRAFTS_FOLDER` | force le dossier Brouillons            | auto (`\Drafts`)             |

## Format "fiche"

Les deux scripts lisent le meme format, calque sur le bloc `## Email (brouillon)` des fiches
Notion : 1re ligne `Objet : ...`, une ligne vide, puis le corps. On colle le contenu Notion tel quel.

## .env (local seulement)

`cp tools/.env.example .env` a la racine, remplis les secrets. `.env` est gitignore (jamais sur
GitHub). Les scripts le chargent automatiquement. En cloud/web, les memes variables se mettent
cote environnement de la routine (pas de `.env`).
