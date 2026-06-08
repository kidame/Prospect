# tools/

Petits utilitaires hors routine nocturne.

## infomaniak_draft.py — deposer un brouillon dans la boite Infomaniak

Pose un mail finalise (objet + corps) en **brouillon** dans le dossier Brouillons d'une
boite Infomaniak, via IMAP `APPEND` + flag `\Draft`. Aucun envoi : la revue manuelle reste.
Objectif : que le mail redige par la routine soit pret a envoyer directement dans la boite
mail, sans copier-coller depuis Notion.

### Contrainte reseau (a lire absolument)

L'environnement cloud de Claude Code (ou tourne la routine nocturne) ne laisse sortir que le
**HTTP/HTTPS (443)** via un proxy. Les ports **IMAP 993 / SMTP 465-587 sont bloques** et le
restent meme en network access "Custom" (l'allowlist ouvre des domaines pour le proxy HTTP/S,
pas un port TCP brut). **Donc ce script ne peut pas tourner depuis la routine cloud.** Il doit
s'executer la ou le 993 est ouvert :

- le **VPS Infomaniak** en cron (recommande), ou
- une **machine perso** (terminal local / `claude --teleport`).

Le mode `--dry-run` n'ouvre aucune connexion : il imprime le mail genere et marche partout
(utile pour tester l'encodage).

### Configuration (variables d'environnement)

| Variable                   | Role                                              | Defaut               |
| -------------------------- | ------------------------------------------------- | -------------------- |
| `INFOMANIAK_IMAP_USER`     | login = adresse mail complete (REQUIS)            | —                    |
| `INFOMANIAK_IMAP_PASSWORD` | mot de passe app/boite (REQUIS)                   | —                    |
| `INFOMANIAK_IMAP_HOST`     | serveur IMAP                                      | `mail.infomaniak.com`|
| `INFOMANIAK_IMAP_PORT`     | port IMAPS                                         | `993`                |
| `INFOMANIAK_FROM`          | From affiche, ex. `Thomas Puglisi <thomas@...>`   | = `INFOMANIAK_IMAP_USER` |
| `INFOMANIAK_DRAFTS_FOLDER` | force le nom du dossier (sinon auto `\Drafts`)    | auto-detection       |

### Exemples

```bash
# 1) Verifier le mail genere sans rien envoyer (aucune connexion)
python3 tools/infomaniak_draft.py --to x@y.ch --subject "Test" --body "Bonjour," --dry-run

# 2) Lister les dossiers IMAP (pour reperer le dossier Brouillons)
python3 tools/infomaniak_draft.py --list-folders

# 3) Depuis un fichier "fiche" : 1re ligne "Objet : ...", le reste = corps
python3 tools/infomaniak_draft.py --to prospect@exemple.ch --from-file mail.txt

# 4) Arguments directs, corps sur stdin
python3 tools/infomaniak_draft.py --to prospect@exemple.ch \
    --subject "Votre visibilite a Neuchatel" --body-stdin < corps.txt
```

Le format "fiche" colle au bloc `## Email (brouillon)` des fiches Notion : 1re ligne
`Objet : ...`, ligne vide, puis le corps. On peut donc coller le contenu Notion tel quel.
