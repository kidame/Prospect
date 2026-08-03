# Session dev 2026-08-03 : test humanisation mail 1 (avec Thomas)

## Fait
- **Test humanisation LANCE** : mail 1 entierement reecrit en session avec Thomas (v1 du 10.06 -> v6) sur un prospect du segment **menuisier x Val-de-Travers** (Place ID 0x478dc11ad90a95a1:0x761ea461cf193d14, fiche Notion = source unique). **ENVOYE le 03.08 par Thomas** (webmail). Statut "Mail 1 envoye" + Date mail 1 poses -> relance auto J+7 (nuit du 10-11.08) si pas de reponse.
- **Recette v6 a mesurer** (si reponse -> generaliser, enrichir le skill writing) :
  1. Objet registre "premier contact" (« petit mot d'un voisin de couvet »), derogation assumee a "l'objet porte le fait".
  2. Ouverture = reconnaissance dans LES MOTS du prospect (site lu : « 4 generations », histoire familiale) + metier explique en 1 phrase concrete (« regarder ce que les gens tapent, faire en sorte que vous soyez la meilleure reponse ») + rarete locale + intention region.
  3. Fait porteur QUALITATIF (fiche GBP #1 du pack mais sans lien vers le site), hedge, zero chiffre de donnee.
  4. Micro-offre par mail + cloture reprenant la formule du site du prospect (« au plaisir que nos chemins se croisent »).
  5. 108 mots, squelette D, 1 question.
- Verifications avant envoi : SERP re-mesuree 2x le jour meme (2 requetes), compteur d'avis re-verifie via business listings, dossiers Envoyes/Brouillons Infomaniak passes en revue.

## Decouvertes systeme (issues ouvertes, a reviser en session /story)
- **ISS-005** (high) : champ "Avis Google" = 67 alors que la fiche GBP n'affiche AUCUN avis ; 67 = nb de PHOTOS. Fait porteur faux valide 🟢 par le controle 3h (qui re-verifie la SERP, pas les compteurs).
- **ISS-006** (high) : refus recu par email (15.06) jamais enregistre dans Notion + dedup Place ID aveugle aux doublons d'entreprise (2 fiches GBP) -> 2e mail a froid parti apres refus (22.07) + relance preparee a tort (brouillon intercepte). 2 fiches de la meme entreprise passees en Perdu, verrou pose.
- Pattern bonus : une entreprise peut avoir PLUSIEURS fiches GBP (2 cas reels le meme jour sur ce segment) — piege de mesure ET angle de vente.

## Etat / suivi
- PR #88 (draft) : .story/ ISS-005 + ISS-006 + ce handover. Check-in horaire arme jusqu'a merge.
- A surveiller : reponse au mail test (le taux de reponse est le juge de paix de la recette v6).
- Deux vieux brouillons Infomaniak a supprimer par Thomas si pas deja fait (mail v1 du 10.06 au fait faux ; relance du 31.07 vers l'entreprise qui a refuse).
- Prochain couple rotation : inchange par cette session (pas un run de collecte).