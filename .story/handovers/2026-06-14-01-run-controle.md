# Controle qualite 2026-06-14 (03:00) — NOOP cote fiches + 1 issue ouverte

**TL;DR** — Aucune fiche a controler cette nuit (0 fiche avec Draft pret=true ET Controle vide). Le run 1h du 06-14 n'a produit aucune fiche neuve (rien de plus recent que le 06-13 01:11). Les 4 retenus EMAIL du run 06-13 (segment cuisiniste/agencement x Geneve) portaient deja un verdict (poses par le controle du 06-13). Catch-up verifie propre : batches 06-11 (energie x Fribourg) et 06-12 (sanitaire x Neuchatel) deja controles (verdicts 🟢). 1 issue ouverte (defaut accents recurrent).

## Compteurs
- Fiches controlees cette nuit : 0 (noop legitime, cf. CONTROLE_PROMPT etape 3).
- Verdicts deja en place sur les fiches recentes (controlees nuits precedentes) : 06-13 batch = 3x 🟠 + 1x 🔴 (divergence "pages" sur 1 fiche) ; 06-12 = 🟢 ; 06-11 = 🟢.
- Cout : ~0 CHF (aucune re-mesure SERP, lecture seule Notion + Storybloq).

## Defaut dominant observe (-> ISS-002)
- ACCENTS : le run 1h ecrit ses mails en ASCII pur (sans accents) alors que CLAUDE.md impose l'accentuation ("prime sur toute consigne ASCII"). Vu 4/4 fiches le 06-13, et corrections manuelles d'accents notees sur les fiches 06-11/06-12 -> >=3 nuits, >=6 fiches. Le controle l'attrape a chaque fois mais le mail n'est pas envoyable tel quel. Issue ISS-002 (medium) ouverte : forcer l'accentuation a la GENERATION (ROUTINE_PROMPT etape 9 / skill writing), pas en aval.

## Observation systeme (a trancher en session dev, pas mon perimetre)
- `storybloq issue list --status open` ressortait VIDE en debut de session, alors que le handover du run 1h 06-13 affirme avoir ouvert une issue rotation (ISS-001). Forte presomption de push casse (cf. T-007 deja suspecte). Si le push de cette nuit echoue aussi, ISS-002 sera perdue -> a verifier cote dev (`git log -- .story/`). Je ne duplique pas la meta-observation rotation, deja portee par le handover 1h.

## Prochain controle
- Rien de specifique en attente. Si le run 1h reprend, surveiller : (1) accents (ISS-002 tant que non corrige a la source), (2) affirmations "une seule page" vs sitemap reel (1 divergence 🔴 le 06-13 sur fiche Wix multi-pages).
