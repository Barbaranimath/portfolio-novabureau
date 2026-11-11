# INC-004 — Connexion VPN impossible

| Champ | Valeur |
|---|---|
| Ouvert le | 2026-10-20 08:05 (téléphone) |
| Demandeur | Sarah Morin (E12), représentante commerciale, Ventes, en télétravail |
| Priorité | **P3 — Moyenne** (1 personne bloquée; P2 si plusieurs télétravailleurs étaient touchés) |
| Assigné à | Barbara Saroukou |
| Pris en charge | 08:12 (7 min, cible 4 h) |
| Résolu | 08:58 (53 min, cible 4 h) |
| Statut | Fermé |

## Description

Le client VPN affiche « Échec de l'authentification » puis « Délai d'attente dépassé ». Le courriel infonuagique fonctionne, mais pas l'accès au stockage partagé.

## Diagnostic (dans l'ordre, du plus simple au plus complexe)

| # | Vérification | Résultat |
|---|---|---|
| 1 | Connexion Internet | OK : navigation et Teams fonctionnent |
| 2 | État du service VPN | OK : 4 autres télétravailleurs connectés, donc pas de panne générale |
| 3 | Adresse du serveur | OK : `vpn.novabureau.example` |
| 4 | Identifiants | OK : connexion Microsoft 365 réussie avec les mêmes identifiants |
| 5 | MFA | **Problème** : nouveau téléphone, l'application d'authentification n'avait pas été transférée et la notification n'arrivait jamais |
| 6 | Version du client VPN | **Problème** : version 5.2, alors que la passerelle exige 5.4 ou plus depuis la mise à jour du 2026-10-18 |

## Résolution

1. Vérification d'identité (rappel au numéro du dossier RH), puis réinitialisation des méthodes MFA.
2. Inscription de l'application d'authentification sur le nouveau téléphone, avec l'utilisatrice au téléphone.
3. Mise à jour du client VPN vers 5.4.2 par le canal de déploiement.
4. Connexion VPN réussie, puis test d'accès à une ressource interne : ouverture de `\\NAS-01\Ventes`.

## Suivi et amélioration

- Une recherche dans le registre a montré que **4 autres postes** de télétravailleurs avaient encore un client antérieur à 5.4. Ils ont été mis à jour de façon proactive le jour même, ce qui a évité 4 billets.
- Ajout au guide [Se connecter au VPN](../../07-base-connaissances/02-se-connecter-au-vpn.md) : « Vous changez de téléphone ? Transférez d'abord votre MFA. »
- Recommandation au responsable TI : annoncer les changements de version minimale 5 jours à l'avance.
