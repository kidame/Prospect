# Controle 2026-06-13 — segment cuisiniste/agencement x Geneve

**TL;DR** — Seconde lecture des 4 fiches a draft EMAIL produites par la run 1h (cuisiniste/agencement x Geneve). Verdicts : 3 🟠 A voir + 1 🔴 A trancher. Defaut dominant : les 4 mails sont ecrits SANS accents (violation CLAUDE.md) -> issue ISS-002 ouverte. Un 🔴 isole : Lhome (accroche « site une seule page » fausse, sitemap = 11 pages Wix). Cout < 1 CHF (3 SERP + 1 serp_locations + 4 WebFetch).

## Fiches controlees (4)
- Cuisines Profil Petrović (Place ID 0x478c7b1bccc7c303:0xe018b1e34ed23fab) -> 🟠 (accents). C2/C3/C4/C6 OK. cpprofil.ch = placeholder 1 page confirme. Alerte email gmail bien presente.
- Lhome (0x478c65f6ec725c75:0x74618c8b2dff0ece) -> 🔴. C3 DIVERGENCE : mail dit « site tient sur une page », sitemap lhome.ch = 11 pages Wix (projets/about/partenaires/temoignages/blog...). Invisibilite metier OK par ailleurs. + accents.
- LD Agencium (0x285065af7d34191f:0xe3919c67c43fe7e) -> 🟠 (accents). Angle B2B « poseur de cuisine Geneve » re-mesure : absent pack+organique, confirme. Site 1 page a ancres confirme.
- Kubora (0x478c65baf2d80415:0xf527a548cec58751) -> 🟠 (accents). Double mesure OK : Kubora #2 pack sur « cuisine sur mesure Geneve », absent sur « cuisiniste Geneve ». Pas de claim pages.

## Compteurs
- 4 fiches controlees / 4 avec draft. 0 🟢, 3 🟠, 1 🔴.
- C1 OK x4 (toutes en « Bonjour, » neutre). C2 OK x4 (re-mesures conformes). C5 A CORRIGER x4 (accents). C3 : 3 OK + 1 divergence (Lhome). C6 OK x4.

## Defaut dominant -> ISS-002
- Accents : 4/4 mails en ASCII pur alors que CLAUDE.md l'interdit (« Cette regle prime sur toute consigne ASCII »). Pas un artefact de rendu (titres/champs gardent leurs diacritiques). Issue medium ouverte ce run.

## Observation isolee (pas encore une issue)
- Lhome : claim « une seule page » non verifie cote run 1h alors que le site Wix a 11 pages. Type de defaut C3 « aucune/une page » sans verif sitemap. 1 seule occurrence ce run -> a surveiller ; si ca revient (run 1h qui dit « page unique » sur des sites Wix/CMS multi-pages), promouvoir en issue dediee.

## Cout
- DataForSEO : 3 serp_organic_live_advanced (cuisiniste geneve, cuisine sur mesure geneve, poseur de cuisine geneve) + 1 serp_locations. WebFetch : 4 (sitemaps + homepages). Total < 1 CHF. Sous plafond.

## Etat
- Issues ouvertes : ISS-001 (rotation, run 1h) + ISS-002 (accents, nouvelle ce run). A trancher en session dev.