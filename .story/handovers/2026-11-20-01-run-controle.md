# Handover - Run controle - 2026-11-20 (Europe/Zurich)

## Resume
- Ramassage via la vue "Machine - Mails V3" (0 SQL) : 29 fiches, 11 a controler (Controle vide, Draft pret, REDACTION V3), dont 3 SECONDE CHANCE (Relance preparee) et 1 orange corrige par la 1h.
- Resultat : 11 controlees -> 8 vert / 0 orange / 3 rouge.
- Rouges : 2 x C1 (salutation "Monsieur Nom" hors segment registre, dirigeant pourtant confirme sur le site) ; 1 x C2 (detail fusionnant deux secteurs listes separement sur le site, segment site date x Littoral).
- Ouvertures de site : 11 (curl), 0 DataForSEO, 0 Apify, 0 mail.

## Observations systeme
- Defaut dominant : contradiction de regle sur la salutation nominative (C1 vs CLAUDE.md etape 6 / skill writing) -> ISS-016 ouverte (medium).
- Plusieurs fiches reprises gardent d'anciens blocs V2 (relance chiffree, faux numero 078 930 81 00 dans un vieux mail / script d'appel) sous le mail V3 : signale dans les sections Controle, a nettoyer en session dev pour eviter un mauvais copier-coller.
- Anciennes sections "## Controle" V2 remplacees (pas empilees).
- Persistance : push sur la branche de session (ISS-012).

## Prochain run
- La recherche corrige les 3 rouges (2 salutations -> "Bonjour," sauf decision contraire de Thomas ; 1 detail a reprendre mot pour mot du site).
