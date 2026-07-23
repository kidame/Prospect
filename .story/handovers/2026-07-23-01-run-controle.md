# Handover — Run Controle (03:00) — 2026-07-23

## Resume
- Fiches ramassees (Draft pret = coche ET Controle vide) : 3, toutes du segment "installateur PAC/solaire x Neuchatel" (run 1h de la nuit).
- Verdicts : 🟢 0 / 🟠 0 / 🔴 3. Toutes 🔴 A trancher.
- Champ "Controle" existait deja (setup OK). SQL Notion query : FONCTIONNE ce run (ISS-003 non reproduite cette nuit).

## Defaut dominant
- DEUX defauts systematiques, 3 fiches / 3 :
  1. FAIT PORTEUR faux ou non reproduit (les 3) -> ISS-004 (high) creee. Derive de requete Diagnostic->mail (ELKA : "pompe a chaleur" vs "installateur pompe a chaleur" -> ELKA en fait #1 pack), position pack non reproduite (STG absent du 3-pack Neuchatel-ville), "une seule page" faux (Laderach = site multi-pages).
  2. ACCENTS absents dans les 3 mails -> ISS-005 (medium) creee.

## Cout estime
~1 CHF. DataForSEO : 1 serp_locations + 2 serp_organic_live_advanced (mobile). 2 WebFetch (gratuit). Sous plafond.

## Observations systeme
- Le controle a paye ce run : 3 mails auraient ete envoyes avec un fait porteur faux/non verifie sans cette seconde lecture.
- Les 2 tool calls storybloq/notion en parallele du debut ont ete rejetes 2x (batch) ; passage en CLI storybloq (Bash) + appels Notion sequentiels = OK. A surveiller.

## Prochain
- Watcher si la derive de requete (ISS-004) et l'ASCII (ISS-005) reviennent sur les prochains runs -> promouvoir en lecons/tickets en session dev.
