# Controle qualite 2026-06-25 (03:00) — segment peintre x Geneve

**TL;DR** — Seconde lecture des 5 fiches a draft EMAIL produites par le run 1h (peintre x Geneve). Verdicts : 4 🟢 OK + 1 🟠 A voir, 0 🔴. Bonne nouvelle systeme : les accents sont PRESENTS dans les 5 mails -> le defaut recurrent ASCII (ISS-002 des nuits precedentes) ne se reproduit PAS ce run. Cout ~0,1 CHF (1 SERP re-mesure + 1 serp_locations).

## Compteurs
- Fiches a controler (Draft pret=true ET Controle vide) : 5, toutes canal EMAIL, toutes segment peintre x Geneve.
- Verdicts : 4 🟢, 1 🟠, 0 🔴.
- Hors perimetre ce run : 2 fiches "A APPELER" (pas de draft) + 2 fiches rejetees (deja visibles) — non controlees, conforme.
- Cout : ~0,1 CHF (1 serp_organic_live_advanced "peintre geneve" mobile canton Geneve + 1 serp_locations).

## Methode
- C2 mutualise : les 5 mails partagent le meme fait porteur ("absent du pack local ET de l'organique sur 'peintre geneve' 170/mois ; concurrents devant"). UNE re-mesure SERP a valide l'axe organique pour les 5 : les 5 domaines sont absents du top 14 organique, concurrents (peintre-geneve.ch, El Pintor, Vansende, Pouseiro) presents -> conforme. Pack local non rendu dans la re-mesure au niveau canton (mesure 1h faite ~2h avant, non contredite) -> note de transparence dans chaque Controle, pas un flag (anti-bruit).

## Le seul 🟠
- 1 fiche : objet contenant "invisible" (terme range par CLAUDE.md dans les mots a eviter cote angle email). Fait exact (prospect bien absent), donc pas une contradiction de mesure -> 🟠 ton a adoucir, pas 🔴. Suggestion : objet plus factuel.

## Observation systeme
- ACCENTS : reproduits correctement sur les 5 mails ce run (contrairement aux runs 06-11/06-12/06-13 ou le run 1h ecrivait en ASCII pur). Si ca tient sur les prochains runs, ISS-002 pourra etre consideree comme reglee a la source.
- C6 email scrape incertain : 3/5 fiches en adresse perso (gmail x2, sunrise x1) -> alerte "⚠️ Email a confirmer" correctement presente sur les 3. Bon reflexe du run 1h.
- Pas de nouvelle issue ouverte (le 🟠 "invisible" = 1 occurrence isolee, pas un pattern ; pas d'accumulation).
- `storybloq issue list --status open` ressortait VIDE en debut de session.

## Prochain controle
- Surveiller si "invisible/introuvable" dans l'objet revient (si oui -> issue ton/angle).
- Confirmer que les accents restent presents (sinon ISS-002 toujours d'actualite).