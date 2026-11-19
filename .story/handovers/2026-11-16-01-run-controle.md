# run-controle 2026-11-16

- Perimetre : fiches 'Draft pret' coche + 'Controle' vide. Ramasse : 4 fiches (toutes segment sanitaire x Yverdon, run 1h du 2026-11-13). Toutes canal EMAIL.
- Verdicts : 🟢 0 · 🟠 4 · 🔴 0. (Aucun 🔴 : salutations verifiees, faits porteurs confirmes, aucun controle incomplet.)
- Re-mesures C2 reussies : 2 SERP partages suffisent -> 'sanitaire yverdon' (Yverdon, mobile) couvre 3 fiches [pack 1.Sanitaire Yverdon 2.DAN 3.REGANELY, les 3 prospects absents pack+organique domaine propre = conforme], 'sanitaire orbe' (Orbe, mobile) pour la 4e [pack 1.Urba 2.Pro Sanitaire 3.Beney, prospect absent = conforme]. Concurrents nommes = in-canton, stables (pas de volatilite ISS-009).
- C1 : 1 salutation nominative ('Bonjour Monsieur Guillemin,') VERIFIEE independamment via WebFetch du site -> dirigeant actuel confirme. 3 autres en 'Bonjour,' neutre. OK.
- DEFAUT DOMINANT : accents. 4 corps de mail sur 4 sont 100% ASCII (zero accent) alors que les Diagnostics des memes fiches ont les accents -> l'etape de redaction du mail perd les accents (suspect : code-fence ```javascript + verif deterministe non executee). Issue ouverte ISS-011 (high).
- ISS-005 (photos GBP comptees comme 'Avis Google') : vu une 3e fois (n=3) mais ATTRAPE au controle cette fois (point (b) applique : compteur re-mesure comme la SERP). 'Avis Google'=99 = total_photos ; avis reels=41 a 5.0. Email restait envoyable (ne citait pas le nombre). ISS-005 mise a jour, severite inchangee (high). Point (a) cote routine 1h toujours non corrige.
- Cout estime : ~0.5-1 CHF (2 serp_organic_live_advanced + 1 business_data_business_listings_search payants ; 2 serp_locations + 1 WebFetch quasi gratuits). Sous plafond.
- Aucun mail envoye (conforme : le controle n'envoie rien). Filet = vue Notion 'A trancher' (4 fiches 🟠).
- Observation systeme : les 2 issues de redaction (accents ISS-011, compteur avis ISS-005 point a) visent la MEME routine 1h ; les deux se corrigeraient par une verif deterministe bloquante sur le bloc '## Email (brouillon)' avant ecriture Notion.
