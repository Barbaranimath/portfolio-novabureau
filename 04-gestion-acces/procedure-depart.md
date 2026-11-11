# Procédure de départ d'un employé (offboarding)

**Propriétaire** : Soutien et conformité TI · **Déclencheur** : confirmation officielle des RH · **Délai** : désactivation à l'heure exacte prévue · **Version** : 1.2 (2026-10)

## Pourquoi c'est critique

Un compte resté actif après un départ est l'une des failles les plus courantes dans les PME : il donne accès aux données clients sans que personne ne surveille son utilisation. L'objectif est **zéro accès résiduel** après l'heure de départ.

## Liste de contrôle — exemple : Marc Tremblay, analyste aux ventes (départ le 2026-11-14 à 16 h)

Billet `REQ-OFF-006` · Confirmation RH reçue le 2026-10-31 · Départ volontaire, en bons termes.

| # | Étape | Moment | Preuve conservée | ✓ |
|---|---|---|---|---|
| 1 | Recevoir la confirmation des RH (date, heure, type de départ, gestionnaire responsable des données) | J-14 | Formulaire RH joint au billet | ✅ |
| 2 | Planifier avec le gestionnaire le transfert des données (dossiers clients, boîte courriel) | J-7 | Courriel d'Émilie Fortin | ✅ |
| 3 | **Désactiver le compte** `marc.tremblay` à 16 h 00 | Jour J, 16 h | Journal d'audit (horodatage) | ☐ |
| 4 | Révoquer toutes les sessions actives (ordinateur, téléphone, navigateur) | Jour J, 16 h 01 | Journal d'audit | ☐ |
| 5 | Retirer l'accès VPN et tous les groupes (`GRP-Ventes`, `GRP-Tous`, CRM) | Jour J, 16 h 05 | Liste des groupes avant/après | ☐ |
| 6 | Supprimer les méthodes MFA enregistrées | Jour J, 16 h 05 | Rapport MFA | ☐ |
| 7 | Convertir la boîte courriel en boîte partagée, accès délégué à É. Fortin pour 90 jours; réponse automatique configurée | Jour J | Paramètres de la boîte | ☐ |
| 8 | Transférer le OneDrive professionnel au gestionnaire | Jour J | Confirmation du transfert | ☐ |
| 9 | Récupérer PC-010, le chargeur, la souris et la carte d'accès | Jour J | Formulaire de retour signé | ☐ |
| 10 | Vérifier l'état du matériel, puis effacer et réimager le poste | J+1 | Rapport d'effacement | ☐ |
| 11 | Retirer la licence Microsoft 365 (après la période de rétention de 30 jours) | J+30 | Rapport des licences | ☐ |
| 12 | Mettre à jour l'inventaire et la matrice des accès | J+1 | Fichiers mis à jour | ☐ |
| 13 | Faire valider la fermeture par le gestionnaire et les RH | J+1 | Approbation dans le billet | ☐ |

> Les étapes 3 à 13 seront cochées le jour du départ. Les étapes 1 et 2 sont terminées.

## Variante : départ non volontaire

- Désactivation **pendant** la rencontre de fin d'emploi, coordonnée avec les RH (heure convenue à la minute près).
- Revue des activités du compte sur les 30 derniers jours (téléchargements massifs, transferts de courriel vers l'externe).
- Changement des mots de passe des éventuels comptes de service connus de l'employé.

## Contrôle de détection

Chaque mois, le script [`scripts/comptes_inactifs.py`](../scripts/comptes_inactifs.py) compare la liste des comptes actifs à la liste RH et signale :
- les comptes actifs d'employés partis;
- les comptes sans connexion depuis plus de 45 jours.
