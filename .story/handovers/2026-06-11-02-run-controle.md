# Run controle 2026-06-11 (03:00) — 13 fiches controlees

**TL;DR** — 13 fiches Draft pret + Controle vide ramassees : 3 du run 1h de cette nuit (energie x Fribourg) + 10 de rattrapage (batiment/bois x Val-de-Travers, run "sur demande" du 2026-06-10, jamais controlees, deja "Mail 1 envoye"). Verdicts : 3 x 🟠 A voir, 10 x 🟢 OK. Aucun 🔴. ~7 SERP live + 5 serp_locations, sous plafond (~0,6-0,8 CHF).

## Compteurs
- Controlees : 13 (toutes canal EMAIL/Draft pret).
- 🟢 OK : 10 (batiment/bois VdT).
- 🟠 A voir : 3 (energie x Fribourg) — motif UNIQUE : accents manquants dans le corps du mail.
- 🔴 A trancher : 0.
- Hors scope : 1 fiche "A appeler" (pas de draft) du lot VdT, ignoree comme prevu.

## Defaut dominant (-> ISS-001)
- Les 3 mails du run energie x Fribourg sont rediges SANS accents (e/a/o absents, seule la cedille survit) -> viole "ACCENTS OBLIGATOIRES" de CLAUDE.md. 3/3 fiches du run. Le reste de ces fiches est propre (C2 faits porteurs re-mesures = conformes, salutations neutres, hygiene OK), d'ou 🟠 et non 🔴.
- REGRESSION isolee : les 10 fiches VdT du 2026-06-10 (re-controlees ce soir) et le segment carreleur x Geneve avaient des accents complets (🟢). A surveiller au prochain run energie : si ca recidive -> ISS-001 passe en high.

## Verifs C2 (re-mesures, mobile, 2026-06-11)
- Energie : "installateur panneaux solaires" Fribourg (pack Swiss-instasolar/Prealpes/ProWatt) + Vaud canton (swissolaire.ch present p1 organique ~#5, conforme au contraste Vaud-present/Fribourg-absent) + "installateur pompe a chaleur" Fribourg (pack Solix/Vaillant/Swissthermic, conforme). Tous faits porteurs valides.
- Bois VdT : "menuisier Neuchatel" + "menuisier Yverdon" -> aucun artisan VdT en page 1 (absences confirmees). Electricien VdT : "electricien Neuchatel" + "electricien Yverdon" -> AR Electricite et ElectrOGControle absents p1 (conforme "page 4 / annuaires devant").
- Piege evite : a Lausanne-ville, c'est swissolar.ch (l'association) qui ressort, PAS swissolaire.ch (l'entreprise). La presence Vaud du prospect se confirme seulement au niveau CANTON Vaud. A retenir pour ne pas crier au faux fait porteur sur ce genre d'homonymie de domaine.

## Observations systeme
- RATTRAPAGE reel : un run "sur demande" (hors routine 1h nocturne) peut produire des fiches Draft pret jamais controlees ET deja envoyees par Thomas (les 10 VdT etaient "Mail 1 envoye" sans verdict). Le controle nocturne les ramasse correctement via le filtre Draft pret + Controle vide, mais le verdict arrive POST-envoi pour ces cas (valeur surtout pour la relance + l'apprentissage). Normal, pas un bug.
- Le dossier .story/issues/ n'existait pas -> 1er issue_create a echoue (io_error) jusqu'a creation du dossier. Cree ce soir ; ISS-001 ecrite ensuite. A noter pour les prochains runs (si le conteneur repart propre, recreer .story/issues/ avant issue_create).
- domain_rank_overview / SERP mutualisee : 2 requetes par segment ont suffi a couvrir tout un lot (4 SERP pour 10 fiches VdT, 3 pour 3 fiches energie).

## Suite
- Thomas : 3 fiches energie en 🟠 -> remettre les accents au copier-coller avant envoi (faits et salutations bons). Les 10 VdT sont 🟢 (deja envoyees).
- Session dev : trancher ISS-001 (regression accents) — si non reproduite au prochain run energie, peut rester ouverte/observation ; si reproduite, durcir ROUTINE_PROMPT.md (rappel accents a l'etape redaction).
