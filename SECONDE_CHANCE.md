# SECONDE CHANCE - un nouveau mail pour d'anciens contacts restes sans reponse
(decision Kidam, 2026-11-18)

## Pourquoi
54 fiches sont au statut "Relance préparée" : leur premier mail (ancienne redaction, chiffree)
est parti entre juin et aout 2026 et la relance n'a jamais ete envoyee. Il est trop tard pour
une relance. Decision de Kidam : "si je n'ai jamais envoye de mail ou jamais recu de reponse,
oui une seconde chance ; sinon non".

## Qui y a droit (TOUTES ces conditions)
- "Statut pipeline" = "Relance préparée" et "Email" rempli ;
- commune dans la zone de PISTES.md : rang 1 d'abord (Val-de-Travers), puis rang 2, puis
  rang 3. HORS ZONE : uniquement les fiches dont les Notes contiennent "SECONDE CHANCE HORS
  ZONE autorisee" (voir plus bas), et apres celles de la zone ;
- Notes ne contenant ni "NE PLUS CONTACTER" ni "SECONDE CHANCE - REDACTION V3" (= mail de
  seconde chance deja ecrit) ;
- LA BOITE FAIT FOI. Lance `python3 tools/boite_etat.py --historique` (toute la boite) :
  * AUCUNE reponse, jamais : ni l'adresse ni son domaine (hors domaines generiques) ne figure
    dans "expediteurs" / "domaines_expediteurs". Une reponse, meme polie -> PAS de seconde chance ;
  * 2 mails envoyes AU PLUS a cette adresse ("envois_par_adresse"). 3 ou plus -> jamais ;
  * le dernier envoi date de PLUS de 120 jours. Exception : aucun envoi du tout dans la boite
    (la fiche disait "envoye" a tort) -> pas d'attente, elle y a droit tout de suite.
- Fiche de la zone SANS Email mais avec telephone : pas de mail, elle entre dans les "TROIS
  APPELS DU JOUR" du mail du matin (BOITE.md).
Si la boite est illisible : aucune seconde chance cette nuit.

## Chaque nuit, 3 fiches au plus (routine de recherche, apres les corrections et la reprise)
1. Lis la fiche en entier. Visite le site s'il y en a un (1 requete). Site mort ou activite
   arretee -> statut "Ancien", Notes += "seconde chance : site inactif le AAAA-MM-JJ".
2. Avec site : prepare le bloc "### Portrait et idees" et choisis l'idee (skill writing, "Le
   paragraphe idee", regle du 2026-11-27 ; 3 a 5 pages). Sans site : UN detail vrai. Rien
   d'etaye -> Notes += "seconde chance : pas d'idee etayee" (ou "pas de detail verifiable"),
   pas de mail, fiche suivante.
3. Ecris en bas du corps une section "## Seconde chance (brouillon)" : un mail V3 complet
   (1re ligne "Objet : ...", corps, signature canonique), ecrit comme un PREMIER message. Il ne
   mentionne pas l'ancien mail, ne s'excuse pas, ne dit pas "je vous avais ecrit". Son objet
   est different de celui de l'ancien mail. Porte A si l'entreprise n'a pas de site, porte IDEE sinon.
4. Ne touche NI au bloc "## Email (brouillon)" (l'ancien mail : c'est la trace de ce qui est
   parti) NI au bloc "## Relance 1 (brouillon)" (jamais envoyee, elle reste la, inutilisee).
5. Champs : Notes += "SECONDE CHANCE - REDACTION V3 - mail ecrit le AAAA-MM-JJ" (suivi de
   " - IDEE : <l'idee en trois mots>" si le mail porte une idee) ; vide le champ
   "Controle" ; "Draft pret" coche ; statut INCHANGE ("Relance préparée").

## La suite, sans rien faire de plus
- Le controle relit le bloc "## Seconde chance (brouillon)" avec ses 7 controles.
- La relance le depose en brouillon s'il est au vert (BOITE.md section 3).
- Envoi constate dans la boite : la fiche passe en "Mail 2 envoyé" (BOITE.md 2b). Sans reponse
  apres 21 jours : "Perdu" (BOITE.md 2f). AUCUNE relance, plus aucun mail ensuite.
- Reponse : BOITE.md 2c.

## Hors zone : seulement un site a refaire (decision Kidam, 2026-11-18)
Hors zone, Thomas n'a ni l'avantage du voisin ni la possibilite de passer. Une seconde
chance n'y a de sens que si le site de l'entreprise est visiblement a l'abandon. Kidam a
autorise 5 fiches, marquees dans leurs Notes "SECONDE CHANCE HORS ZONE autorisee par Kidam".
N'en ajoute AUCUNE de toi-meme.
- Au moment d'ecrire, constate TOI-MEME sur le site au moins 2 signes concrets et visibles
  par n'importe qui (annonce perimee, pages vides ou nommees "blank", texte de gabarit,
  liens du menu qui ne menent nulle part, derniere actualite vieille de plusieurs annees).
  Moins de 2 signes, ou site illisible : pas de mail, Notes += "seconde chance : site en
  etat correct" (ou "site illisible"), statut "Perdu".
- Le mail suit la redaction V3, avec UNE phrase en plus, juste apres le detail sur leur
  travail : un seul de ces signes, dit simplement et sans jugement (exemple : "En passant
  sur votre site, j'ai vu qu'il annonce encore la fermeture des fetes 2021-2022."). Pas
  de liste de defauts, aucun mot sur Google ni sur leur classement, aucun chiffre hors
  l'annee citee. Porte A.
- Les autres regles de ce fichier s'appliquent (boite, 2 envois au plus, 120 jours).
Les autres fiches "Relance préparée" hors zone sont classees par la routine relance
(BOITE.md, 2h).

## Recap
Une ligne par seconde chance ecrite (nom, commune) et le nombre de fiches qui y ont encore droit.
