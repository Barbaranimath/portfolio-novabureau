# INC-003 — Accès refusé à un dossier partagé

| Champ | Valeur |
|---|---|
| Ouvert le | 2026-10-07 09:15 (courriel) |
| Demandeur | Sophie Martin (E15), adjointe administrative, Administration (arrivée le 2026-10-05) |
| Priorité | **P3 — Moyenne** |
| Assigné à | Barbara Saroukou |
| Pris en charge | 09:40 (25 min, cible 4 h) |
| Résolu | 11:05 (1 h 50, cible 1 jour) |
| Statut | Fermé |

## Description

« Accès refusé » en ouvrant `\\NAS-01\Ventes\Soumissions`. Son gestionnaire lui a demandé de mettre en forme des soumissions clients.

## Diagnostic

1. **Département et rôle** : Administration. Selon la [matrice des accès](../../04-gestion-acces/matrice-acces.md), le groupe Administration n'a **aucun accès** au dossier Ventes.
2. **Besoin professionnel** : confirmé auprès d'Antoine Lavoie (directeur des opérations) : besoin réel, mais limité au sous-dossier `Soumissions`, en lecture et en modification, pour une durée de 3 mois.
3. **Permissions actuelles** : membre de `GRP-Administration` et `GRP-Tous` seulement. Le refus est donc normal : aucune panne.

## Résolution

1. Approbation écrite reçue par courriel de la propriétaire du dossier, Émilie Fortin (directrice des ventes), jointe au billet.
2. Création du groupe `GRP-Ventes-Soumissions-Modif` (s'il n'existait pas), appliqué **seulement** au sous-dossier `Soumissions`.
3. Ajout de Sophie Martin au groupe, avec une **date d'expiration au 2027-01-07**.
4. Test avec l'utilisatrice : ouverture et modification réussies dans `Soumissions`, accès toujours refusé au reste du dossier Ventes (comportement attendu).
5. Mise à jour de la matrice des accès (exception temporaire consignée).

## Ce qui n'a pas été fait, et pourquoi

- **Aucun droit administrateur ni accès complet au dossier Ventes** n'a été accordé « pour aller plus vite ». Ce serait contraire au principe du moindre privilège et exposerait les données clients.
- Aucune permission n'a été donnée directement à l'utilisateur : tout passe par un groupe, ce qui facilite la revue trimestrielle et le départ.

## Suivi

Rappel automatique au 2026-12-20 pour demander au gestionnaire si l'accès doit être prolongé.
