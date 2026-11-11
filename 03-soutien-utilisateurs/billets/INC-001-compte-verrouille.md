# INC-001 — Compte verrouillé

| Champ | Valeur |
|---|---|
| Ouvert le | 2026-09-14 08:42 (téléphone) |
| Demandeur | Kevin Nguyen (E11), représentant commercial, Ventes, en télétravail |
| Catégorie | Compte verrouillé |
| Priorité | **P3 — Moyenne** (1 personne, travail bloqué, aucun indice de compromission au départ) |
| Assigné à | Barbara Saroukou |
| Pris en charge | 08:47 (5 min, cible 30 min) |
| Résolu | 09:04 (22 min, cible 30 min) |
| Statut | Fermé, confirmé par l'utilisateur |

## Description

L'utilisateur ne peut plus ouvrir de session Microsoft 365 après plusieurs tentatives. Message affiché : « Votre compte a été verrouillé ». Il a un appel client à 10 h.

## Diagnostic

1. **Vérification d'identité** : rappel au numéro inscrit au dossier RH (et non à celui de l'appel entrant), puis confirmation du code envoyé à son gestionnaire Émilie Fortin par Teams.
2. **Confirmation du verrouillage** : statut « verrouillé » dans la console d'administration, 10 échecs entre 08:21 et 08:38.
3. **Recherche d'activité suspecte** : les 10 échecs viennent de l'adresse IP résidentielle habituelle de l'utilisateur, à Laval, depuis son poste PC-011.
4. **Journaux de connexion des 7 derniers jours** : aucune connexion depuis un pays ou un appareil inhabituel, aucune approbation MFA refusée.
5. **Cause identifiée** : l'utilisateur avait changé son mot de passe la veille sur son ordinateur, mais son téléphone tentait encore de synchroniser le courriel avec l'ancien mot de passe.

## Résolution

1. Déverrouillage du compte.
2. Réinitialisation avec un mot de passe temporaire transmis par un canal distinct et changement obligatoire à la connexion.
3. Vérification que la méthode MFA (application d'authentification) est toujours enregistrée et fonctionnelle.
4. Mise à jour du mot de passe dans l'application courriel du téléphone, avec l'utilisateur au téléphone.
5. Nouvelle connexion réussie et accès au courriel, à Teams et au CRM confirmé.

## Résultat et suivi

- Accès rétabli en 22 minutes, avant l'appel client.
- Rappel envoyé : ne jamais communiquer son mot de passe, y compris au soutien TI.
- Lien vers le guide [Réinitialiser son mot de passe](../../07-base-connaissances/01-reinitialiser-mot-de-passe.md), mis à jour avec une section « Après un changement, mettez aussi à jour votre téléphone ».

## Leçon retenue

Une cause fréquente : 3 des 9 comptes verrouillés au T3 proviennent d'un appareil mobile qui garde l'ancien mot de passe. La section a été ajoutée au guide.
