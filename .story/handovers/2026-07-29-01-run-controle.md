# Handover — Run controle 03:00 — 2026-07-29

## Resume META (zero PII)
- 8 fiches controlees (Draft pret + Controle vide). Deux lots :
  * 5 fiches carreleur x Montagnes NE (rattrapage du run 07-28, restees sans verdict).
  * 3 fiches sanitaire x Geneve (run 07-29 de la nuit).
- Verdicts : 2 🟢 OK, 4 🟠 A voir, 2 🔴 A trancher.

## Defaut dominant
1. SIGNATURE (C7) — les 5 fiches carreleur 07-28 ont une signature tronquee
   ("Thomas / KUMO - kumo-seo.ch", sans nom complet "Puglisi" ni numero 078 939 81 00).
   MAIS : les 3 fiches sanitaire 07-29 portent la signature canonique complete et correcte
   -> le correctif signature (session dev 07-28 : signature verbatim CLAUDE.md + C7) est
   CONFIRME cote nouveau run. Les 5 carreleur sont des fiches PRE-correctif -> defaut residuel,
   pas un nouveau bug. Pas d'issue (deja regle).
2. FAIT PORTEUR "absence" falsifiable (2 🔴) :
   * 1 carreleur (Place ID 0x478de564ab8159ed:0xa04e3fd93e0807e3) : mail dit "pas dans le pack,
     relegue sous les annuaires" alors que la re-mesure le montre fiche #3 du pack local sur sa
     requete coeur ("carreleur Le Locle"). Accroche entiere fausse.
   * 1 sanitaire (Place ID 0x478c7ba3cc35b5bb:0xcdf37ad422284ad9) : mail etend "n'apparait pas
     sur la 1re page" a la requete vedette "plombier Geneve" (720/mois), or re-mesure = position
     absolue 13, page 1. Absence vraie seulement sur l'autre requete (sanitaire Geneve).
   + 1 🟠 proche (Place ID 0x478dfb39744c89d9:0xb0f2a674988a8984) : "vous disparaissez" en
     organique alors que present bas (#6). Constat relatif a preferer.
   Ce pattern "absence non re-verifiee / groupee sur plusieurs requetes dont une seule vraie"
   RECIDIVE (deja vu 07-23 per handover) et PERSISTE post-correctif (le sanitaire est du 07-29).
   -> Issue ouverte ce run.

## Mesure / cout
- ~7 SERP live (mobile, fr, depth 30-100) + 5 serp_locations. Cout estime ~1.5-2 CHF. Sous plafond.
- ISS-003 (query Notion gatee Business plan) : NON reproduite ce run -> le SQL query_data_sources
  a fonctionne (dump des 8 fiches OK). A surveiller (intermittent).

## Prochain
- Rien de special cote controle. Les 5 fiches carreleur 🟠 : Thomas complete la signature au
  copier-coller. Les 2 🔴 : reformulation d'accroche requise avant envoi.