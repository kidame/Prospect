Session dev 2026-11-02 : fiche d'appel "prospects sans site" (hors routine).

FAIT : requete Notion Contacts (56 fiches Offre=Creation, 35 sans domaine) ; re-mesure de 19 fiches via DataForSEO business_listings + Apify compass (cout < 0.20 USD) ; registre Zefix/Moneyhouse pour les dirigeants ; PDF interne livre a Thomas (hors repo, PII).

DECOUVERTES SYSTEME :
- ISS-005 CONFIRMEE a 100 % sur 19 fiches : Notion 'Avis Google' == total_photos GBP (jamais votes_count). Issue mise a jour (n=19, cause : mapping enckay a l'etape COLLECTE). Tout tri par 'Avis Google' sur la base est faux depuis juin ; proposition de script de rattrapage dans l'issue.
- 6 fiches 'pas de site' ont en fait un site aujourd'hui (fiches datees de juin-aout) : la peremption ~120 j joue aussi sur l'etat du site, pas seulement sur le rejet.
- 2 fiches TechnoWatts en doublon (Place ID identique ? a verifier) + fiche test 'ZZ TEST relance' toujours en base.
- 1 raison individuelle 'en cours de radiation' au registre (Zefix statut BEING_CANCELLED) retenue comme prospect : ajouter le statut Zefix au pre-filtre quand le bras est dispo.

RESTE : Thomas appelle demain ; rien a relancer cote routine. Prochaine session dev : decider du rattrapage 'Avis Google' (ISS-005 b) et nettoyer les doublons.
