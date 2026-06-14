# Controle 2026-06-12 — segment sanitaire/chauffage x Neuchatel

**TL;DR** — Controle de la run 1h du 12/06 (segment sanitaire/chauffage x Neuchatel littoral). 4 fiches EMAIL avec draft controlees : 3 🟠 A voir + 1 🔴 A trancher. Defaut dominant = mails generes sans accents (de nouveau). 1 issue ouverte (ISS-001). ~0,5 CHF (2 SERP mutualisees).

## Perimetre
- Fiches Draft pret=true + Controle vide : 4 (CHRISTEN, Inesan, Rosselet & Manco, n-tecservices).
- Hors perimetre : 1 fiche "A APPELER" sans email (pas de draft) ; les 3 fiches EMAIL du 11/06 (transition energetique x Fribourg) avaient deja un verdict 🟢 → non re-controlees.
- SERP mutualisee : 2 requetes coeur ("chauffagiste neuchatel" + "sanitaire neuchatel", canton Neuchatel, mobile) ont couvert les 4 fiches. A garder (confirme la lecon SERP mutualisee).

## Verdicts (compteurs)
- 🟢 OK : 0
- 🟠 A voir : 3 — toutes pour le MEME motif unique : corps de mail entierement sans accents (C5). Fait porteur, salutation, angle OK par ailleurs.
- 🔴 A trancher : 1 — fait porteur contredit par la SERP du jour : le prospect est en #3 du PACK LOCAL sur ses 2 requetes coeur alors que le mail le dit invisible / concurrents "prennent la place" (et concurrents cites en partie faux). + meme defaut d'accents. La run-1h avait ecrit "absent du pack" dans le Diagnostic → erreur de mesure cote run, pas seulement de redaction.

## Defaut dominant
- ACCENTS : 4/4 mails du run sans accents, apres 3/3 deja sans accents la veille (corriges a la main par Thomas). 7/7 sur 2 nuits. → ISS-001 ouverte (severity high, run-1h redaction). Suggestion : normaliser les accents a la GENERATION, pas au controle.

## Cout
- DataForSEO : 2 serp_organic_live (mobile) + 1 serp_locations. ~0,5 CHF. Largement sous plafond.

## Note systeme
- `.story/issues/` n'existait pas → premier issue_create a echoue (io_error) ; dossier cree a la main puis ISS-001 ecrite. A surveiller : si le dossier disparait (conteneur ephemere / clone), recreer avant issue_create.
- Pas d'issue ouverte pre-existante (issue list vide en debut de session malgre des issues mentionnees dans d'anciens handovers → coherent avec un dossier issues absent / pushes anterieurs perdus).