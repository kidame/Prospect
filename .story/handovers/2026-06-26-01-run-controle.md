# Controle qualite 2026-06-26 (03:00) — NOOP cote fiches + 1 issue (accents) re-ouverte

**TL;DR** — 0 fiche a controler cette nuit (aucune fiche base "Contacts" avec Draft pret=true ET Controle vide). Toutes les fiches Contacts recentes (06-16 -> 06-25) portent deja un verdict : le controle est a jour jusqu'au batch du 06-25. Aucune fiche datee 2026-06-26 visible (le run 1h de cette nuit n'a pas produit de draft EMAIL Contacts indexe, ou n'a pas tourne). 1 issue re-ouverte (accents intermittents).

## Compteurs
- Fiches controlees cette nuit : 0 (noop legitime, CONTROLE_PROMPT etape 3).
- Verdicts deja en place sur les fiches recentes verifiees (controlees nuits precedentes, lecture seule) :
  * demenageur x Geneve (06-24) : 3x 🟢 (TBM, Erza, Fernand Blein)
  * peintre x Geneve (06-25) : 🟢 + 🟢 (Gomes, BA Renovation)
  * electricien x Geneve (06-23/06-25) : 🟠 x3 (DELelec, Watts, AGELEC — accents)
  * demenageur x Lausanne (06-22) : 🟠 x2 (CTA telephone a convertir en mail)
  * cuisiniste/agencement x Fribourg (06-18/06-19) : 🟠 x3 + cuisiniste x Geneve 🔴 (Lhome, "une seule page" vs sitemap 11 pages) ; menuisier x Lausanne (06-16) 🟠
- Cout : ~0 CHF (aucune re-mesure SERP ; lecture seule Notion + Storybloq).

## Perimetre / limite outillage
- Les outils Notion query_data_sources / query_database_view exigent un plan Business+ (refus 400) : impossible de filtrer "Draft pret=true ET Controle vide" par requete. Enumeration faite via notion-search multi-requetes + fetch individuel. Filet a surveiller : une fiche non indexee par la recherche pourrait echapper (peu probable ici, vu la couverture 06-16 -> 06-25).
- La base "Prospects Thai" (collection dab53fb3..., agences de voyage FR en Thailande) est HORS perimetre de ce controle : schema different, pas de champ Controle ni Draft pret, flux propre (Mail/Relance envoyes directement). Non traitee, conforme.

## Defaut dominant (-> ISS-002 re-ouverte)
- ACCENTS : le run 1h genere par INTERMITTENCE ses mails en ASCII pur (~moitie des batches recents : electricien x Geneve, cuisiniste/menuisier 06-16->06-19 ASCII ; demenageur+peintre 06-24/06-25 accentues). Defaut non resolu a la source. ISS-002 (ouverte le 06-14) avait disparu de `issue list` (liste vide = probable push casse, T-007) -> re-creee ce soir (ISS-002, medium). Fix vise : forcer l'accentuation a la GENERATION (ROUTINE_PROMPT etape 9 / skill writing).

## Observation systeme (a trancher en session dev, pas mon perimetre)
- Aucun handover run-1h ni run-controle dans Storybloq depuis le 2026-06-20, alors que des controles ont bien eu lieu (verdicts dates 06-22/06-23/06-24/06-25 dans les fiches) : confirme un push Storybloq casse/non systematique cote routines. A verifier cote dev (`git log -- .story/`).
- Residu mailto : la fiche menuisier x Neuchatel (Mail 2 envoye) porte encore le bouton "Ouvrir ce mail dans mon app" (banni 06-10). Residu pre-regle, deja signale, fiche deja controlee -> pas re-traite.

## Prochain controle
- Si le run 1h reprend : surveiller (1) accents tant que ISS-002 non corrige a la source, (2) CTA "15 min telephone" (vu sur le batch demenageur x Lausanne 06-22, contraire a "CTA = continuer par mail" du 06-20), (3) affirmations "une seule page" vs sitemap reel.
