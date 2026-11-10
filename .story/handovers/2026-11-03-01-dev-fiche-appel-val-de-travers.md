Session dev 2026-11-03 : fiche d'appel "Val-de-Travers" (suite de la session du 02.11).

FAIT : requete Notion Contacts sur le segment/communes Val-de-Travers (38 fiches) ; 21 entreprises retenues (18 artisans/PME + 3 comptes B2B), re-mesurees via DataForSEO business_listings (avis reels, site, horaires) + registre via Moneyhouse (dirigeants) par sous-agent ; PDF interne livre a Thomas (hors repo, PII). Cout API < 0.30 USD.

OBSERVATIONS SYSTEME (niveau meta, zero PII) :
- ISS-005 (avis = photos) : touche aussi les fiches VdT issues de la routine (ex. 29 'avis' = 29 photos, 0 avis reel ; 9 = 9 photos / 2 reels). Les fiches issues des AUDITS manuels de juin (session dev) ont des compteurs justes : le bug est bien dans la collecte routine, pas dans les audits.
- 13 fiches VdT en 'Relance preparee' depuis juillet-aout sans reponse : aucun statut 'Perdu/sans reponse' n'existe pour clore ; elles restent indefiniment en Relance preparee. Idee : statut 'Sans reponse' ou date de peremption pour permettre un re-contact (appel) propre.
- Dates 'Date mail 1' Notion non fiables (2 cas 'jamais envoye' deja corriges en juillet) : la fiche d'appel les cite avec reserve.
- Plusieurs entreprises de la vallee ont change de direction/structure recemment au registre (nouvelle gerante, passage en Sarl, nouvelle societe associee) : signal 'moment de decision' utile pour l'angle d'appel ; a envisager comme signal d'opportunite si le bras zefix/moneyhouse devient accessible a la routine.
- Un sous-agent WebFetch sur moneyhouse.ch (recherche puis fiche) donne les gerants de ~20 societes en 3 min : methode reutilisable pour la salutation nominative.

RESTE : Thomas appelle ; rien cote routine. Decision de rattrapage 'Avis Google' toujours ouverte (ISS-005 b).
