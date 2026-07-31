# Handover — run-controle — 2026-07-31 03:00 — cuisiniste/agencement x Valais (Sion)

## Perimetre
Controle qualite (seconde lecture) des fiches "Draft pret" sans verdict. 4 fiches ramassees, toutes du run-1h de la nuit (segment cuisiniste/agencement x Valais / Sion). Aucune fiche de rattrapage.

## Verdicts (4 fiches)
- 🟢 OK : 0
- 🟠 A voir : 3
- 🔴 A trancher : 1
Total controle : 4.

## Defaut dominant
ACCENTS : 4/4 corps de mail en ASCII pur (flag C5), RECIDIVE de L-008 APRES le verrou deterministe pose le 2026-07-28 -> le rappel textuel de relecture ne tient pas a l'execution. Tiret cadratin en plus sur 3/4. Issue ouverte ISS-004 (high) avec proposition d'un garde-fou systeme plus fort (post-traitement deterministe / few-shot accentue) a trancher en session dev.

## Le 🔴 (fait porteur)
1 fiche (specialiste cuisine exterieure) : le mail nomme 3 concurrents "qui remontent sur 'cuisine exterieure'", mais la re-mesure de la requete litterale (mobile, Sion) montre un organique retail-domine (Beliani/IKEA/Hornbach/Galaxus/Miele...) SANS ce trio. Le coeur "absent de l'organique" reste vrai, mais les concurrents cites — checkables par le prospect — ne se reproduisent pas. Flag C2 divergence -> Thomas tranche. Rejoint le theme "lecture organique / constat relatif non-falsifiable" (deja correctif 07-23) ; 1 seule occurrence de ce sous-type cette nuit -> pas d'issue dediee, surveille.

## Faits porteurs confirmes
Les 3 autres (2x "menuisier Sion", 1x "cuisiniste Sion") : re-mesures SERP conformes (absences pack/organique verifiees ligne a ligne). Mono-page de la fiche menuisier verifiee au sitemap (sert la home, title "Index").

## Systeme
Storybloq MCP a disconnect en debut de session ; fallback CLI `npx @storybloq/storybloq@1.4.4` OK (le package `storybloq` nu renvoie 404 npm — toujours utiliser le scope @storybloq). Cout DataForSEO : 3 appels SERP + 1 serp_locations (~sous plafond 1-2 CHF). Prochain controle : rien de special en attente.
