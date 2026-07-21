# Handover — Run Controle (QA 2e lecture) — 2026-07-21

## Resume
Controle 03:00, contexte neuf. 18 fiches 'Draft pret' sans verdict traitees : run de la nuit (electricien x Lausanne = 4) + RATTRAPAGE du backlog non controle des nuits precedentes (sanitaire x Lausanne 4, carreleur x Fribourg 5, peintre x Neuchatel 2, Yverdon divers 3). Chaque fiche : 6 controles + re-mesure SERP live (device mobile, requete coeur metier+ville) + verif salutation/sitemap. Aucun mail ni Diagnostic touche (lecture seule respectee) ; ecrit seulement le champ "Controle" + section "## Controle".

## Verdicts (18)
- 🟢 OK : 2 — les 2 fiches peintre x Neuchatel. Mails propres, accents corrects, angle C4 exemplaire (dont une PRESENTE #2 au pack local, correctement reconnue puis pivot honnete sur le site vide au lieu d'un faux "invisible").
- 🟠 A voir : 11 — majorite = accents manquants comme UNIQUE motif (mail sinon envoyable) ; qq variations de rang concurrent mineures (3e slot pack qui a tourne) ; 2 fiches Yverdon "legacy" avec CTA telephone + bouton mailto anterieurs aux regles (mailto 2026-06-10, CTA-par-mail 2026-06-20).
- 🔴 A trancher : 5.
  * 3 = OVER-CLAIM d'absence : accroche "absent / nulle part / ni dans les resultats web" DEMENTIE par la re-mesure (present bas de page 1 organique, ou #2 pack local). Regle d'or cassee -> ISS-005.
  * 1 = fait porteur PERIME : accroche basee sur un "contenu demo" de site corrige depuis la 1re mesure (site aujourd'hui propre) -> accroche a refonder.
  * 1 = CTA telephone a froid (fiche Yverdon legacy, anterieure a la regle CTA-par-mail 2026-06-20).

## Defaut dominant
1. ACCENTS manquants (mail ASCII) : ~14/18 fiches, 4 nuits / 4 segments ; seul peintre x Neuchatel conforme. -> ISS-004 (medium).
2. OVER-CLAIM absence vs SERP : 3 fiches, 2 segments, fait porteur falsifiable par le prospect. -> ISS-005 (high).
(Les CTA-telephone / boutons mailto vus sont LEGACY, anterieurs aux regles ; le run de la nuit — electricien — a un CTA-par-mail conforme et pas de mailto : pas d'issue, backlog seulement.)

## Issues ouvertes ce run
- ISS-004 accents ASCII (medium).
- ISS-005 over-claim absence vs SERP (high).

## Cout estime
~0.3-0.5 CHF. 18 re-mesures SERP live (serp_locations + serp_organic_live_advanced par fiche) + qq WebFetch (sitemap/HTML) + verifs registre salutation. Sous plafond.

## Note environnement (sandbox)
Session lancee sur la branche claude/determined-ride-mwv5fp (config de session : push direct sur main bloque). .story/ commite + pousse sur CETTE branche + PR draft, au lieu du push main habituel du controle. La memoire Storybloq (ISS-004/005 + ce handover) attend le merge pour rejoindre main.
