# Handover - Run controle - 2026-11-27 (Europe/Zurich), sprint jour 4

## Resume
- 11 fiches controlees (vue "Machine - Mails V3", champ Controle vide ; 0 SQL, 1 vue). 11 🟢 / 0 🟠 / 0 🔴.
- Dont 4 corrections apres controle (3 salutations nominatives hors registre passees en "Bonjour," ; 1 seconde chance hors zone : signe cache remplace par un signe visible, verifie au navigateur).
- Dont 5 ZONE LARGE (reserve hors zone, VS x2, FR x3) : variante Services ZONE LARGE bien utilisee sur les 5, objets sans "voisin/couvet/val-de-travers".
- Dont 2 mails V3 reecrits le 26.11 jamais controles (anciens controles V2 remplaces).
- Detail verifie sur le site pour les 11 (curl ou navigateur). Aucun appel DataForSEO ni Apify.

## Observations systeme
- 4 sites sur 11 refusent curl (403 Wix ou 502 ponctuel) : il faut le navigateur Playwright ou un 2e essai pour ne pas tomber en "controle incomplet".
- Aucun defaut recurrent nouveau : pas d'issue creee. Le trou "ZONE LARGE sans variante Services" signale par la relance du 26.11 n'apparait plus.
- Restes V2 dans les fiches (ancien mail, ancien controle) : deja couvert par ISS-017.

## Prochain run
- Controler les reecritures de la nuit (seconde chance rang 1 des le 28.11, reserve hors zone FR/GE/VD).
