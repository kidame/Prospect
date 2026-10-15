# Session dev 2026-10-15 : mails de prospection V3, ton chaleureux (decision Thomas)

## Decision
Thomas : « on balance des chiffres et des comparaisons ; je veux un mail humain qui me presente aux entreprises chaleureusement, en quete de collaboration / clients ». Changement RADICAL de ton du mail 1 (et de la relance) : mot de presentation chaleureux, ZERO chiffre, ZERO concurrent, ZERO comparaison, ZERO jargon. La mesure reste integrale pour SELECTIONNER et pour le « ## Diagnostic » Notion (internes) ; elle part dans les pistes APRES le « oui ».

## Fait (branche `claude/prospection-email-tone-ousuk3`, PR draft)
- CLAUDE.md : section « Angles d'email selon le cas mesure » remplacee par « Angle de l'email : une RENCONTRE, pas un diagnostic (V3) » ; section « Redaction de l'email » reecrite (blocs humains, 80-120 mots, zero chiffre, objet registre « premier contact ») ; « Probleme principal » redefini comme champ interne (plus l'accroche du mail) ; relance alignee.
- .claude/skills/writing/SKILL.md : V3 complete (6 lois, blocs, 4 squelettes humains H1-H4, interdits chiffres/jargon/bilan, passe de relecture, 2 exemples fictifs : version securisee et version audacieuse). V2 lisible dans l'historique git.
- ROUTINE_PROMPT.md etape 6 : ton V3 (plus d'angle « concurrent qui double > declencheur > manque-a-gagner »).
- CONTROLE_PROMPT.md : C2 devient « Observation » (re-mesure seulement si le mail observe quelque chose) ; C4 devient « Ton V3 » (flag chiffre / concurrent / jargon / compliment vague = 🟠, faux = 🔴) ; verdicts et exemple mis a jour.
- RELANCE_PROMPT.md etapes 4-5 : fait neuf et micro-valeur formules avec des mots, sans chiffre ni concurrent.

## Garde-fous conserves
Anti-invention (une observation qualitative, si presente, est verifiee ligne a ligne), CTA par mail (jamais d'appel a froid), pas de Diagnostic 1200 ni de tunnel en ouverture, signature canonique, accents comptes, salutation neutre si dirigeant non confirme, enveloppe texte simple.

## A mesurer (T-008 reste la bonne porte)
La V3 est une HYPOTHESE de Thomas, pas un fait mesure : le mail v6 du 03.08 (recette proche) n'a pas de resultat consigne dans Storybloq. Protocole inchange : baseline V1/V2 depuis Notion, decision a ~20 envois V3 sur le taux de reponse (cible >= 8 %). Si la V3 convertit moins que la V2, reintroduire au plus UNE observation qualitative (squelette H4), jamais les chiffres.

## Pour les prochaines runs
- La run de 1h applique la V3 des que la PR est mergee sur main (les prompts sont relus depuis le repo).
- La routine controle de 3h flaggera desormais tout chiffre / concurrent dans un mail (🟠) : attendu les premieres nuits, le temps que la V3 s'installe.
- Aucun couple metier x zone traite cette session (pas de collecte) : rotation inchangee.
- Detecteur de trou memoire : dernier commit .story/ du 2026-08-10, soit > 2 mois ; a verifier que les routines ont bien tourne / persiste depuis (T-007).