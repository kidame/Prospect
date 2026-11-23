# Handover - Run controle - 2026-11-23 (lundi, Europe/Zurich)

## Resume
- Ramassage via la vue "Machine - Mails V3" (0 SQL) : 17 fiches, 12 a controler (Controle vide, Draft pret, REDACTION V3), dont 2 SECONDE CHANCE (Relance preparee) et 3 rouges du 20.11 corriges par la 1h du 21.11.
- Resultat : 12 controlees -> 12 vert / 0 orange / 0 rouge. Les 3 corrections (2 salutations rendues neutres, 1 detail repris mot pour mot) sont conformes.
- Pistes : 6 reprise zone (cuisiniste/peintre/PAC Neuchatel, carreleur Montagnes), 2 site date (Val-de-Ruz, Littoral), 2 registre (Neuchatel, Le Landeron), 2 seconde chance Val-de-Travers.
- Ouvertures de site : 11 (curl), 0 DataForSEO, 0 Apify, 0 mail. Notion : 0 SQL, 1 vue.

## Observations systeme
- Defaut dominant (forme, pas bloquant) : anciens blocs V2 (mail chiffre avec "15 min", relance V2, script d'appel au faux numero) laisses dans les fiches reprises -> ISS-017 ouverte (medium). Signale dans chaque section Controle concernee.
- Anciennes sections "## Controle" (3 rouges du 20.11 + 1 vert V2 de juin) remplacees, pas empilees.
- Le controle n'a pas tourne le week-end : 12 mails attendaient depuis le 21.11.
- Persistance : push sur la branche de session (ISS-012).

## Prochain run
- La relance peut deposer jusqu'a 10 de ces 12 verts (file a 6/10 au 22.11 selon le handover relance : verifier la place).
