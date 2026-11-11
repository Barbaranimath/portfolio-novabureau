# Plan de sauvegarde et de continuité

## 1. Stratégie de sauvegarde (règle 3-2-1)

3 copies des données, sur 2 supports différents, dont 1 hors site.

| Données | Fréquence | Rétention | Destination | Responsable | Test de restauration |
|---|---|---|---|---|---|
| Stockage partagé (NAS-01) | Quotidienne à 22 h, incrémentale | 30 jours quotidiens, 12 mois mensuels | Disque local + infonuagique chiffré (Canada) | T. Caron | **Mensuel** (1 dossier au hasard) |
| Microsoft 365 (courriel, OneDrive, Teams) | Quotidienne, par outil de sauvegarde tiers | 1 an | Infonuagique, autre fournisseur | T. Caron | **Mensuel** (1 boîte courriel) |
| Configuration du pare-feu | À chaque changement + mensuelle | 12 versions | Coffre TI chiffré | T. Caron | Semestriel |
| Documentation TI (ce dépôt) | À chaque modification | Historique Git | Dépôt Git privé | B. Saroukou | s.o. |

**Objectifs de reprise** : RTO (temps maximal d'interruption) de 4 heures pour le stockage partagé; RPO (perte de données maximale) de 24 heures.

## 2. Scénario : le stockage partagé devient indisponible

**Contexte fictif** : le 2026-09-09 à 9 h 12, plusieurs employés signalent que les lecteurs réseau sont inaccessibles.

| # | Étape | Heure | Détail |
|---|---|---|---|
| 1 | Ouvrir un incident | 9 h 15 | `INC-P1-003`, **P1**, car toute l'entreprise est touchée |
| 2 | Informer les utilisateurs | 9 h 20 | Message Teams et courriel : symptôme, contournement (travailler dans OneDrive), prochaine mise à jour à 9 h 50 |
| 3 | Déterminer la cause : réseau ou appareil | 9 h 25 | Le NAS ne répond pas au ping; le reste du réseau fonctionne. Témoin d'erreur : 1 disque en panne, volume RAID dégradé puis démonté |
| 4 | Contacter le fournisseur | 9 h 40 | Remplacement de disque sous garantie, livraison le jour même |
| 5 | Restaurer les données | 10 h 30 | Les dossiers Finance et Ventes, critiques, sont restaurés depuis la sauvegarde de la veille vers un espace temporaire OneDrive |
| 6 | Tester l'accès | 11 h 45 | Un utilisateur par département confirme l'accès à ses fichiers |
| 7 | Remise en état | 15 h 30 | Nouveau disque installé, RAID reconstruit, données synchronisées |
| 8 | Documenter | 16 h 00 | Cause, chronologie, décisions dans le billet |
| 9 | Rapport après incident | J+2 | Voir ci-dessous |

**Résultat** : interruption de **2 h 30** pour les données critiques (RTO de 4 h respecté), aucune perte de données (RPO de 24 h respecté).

## 3. Rapport après incident (résumé)

- **Cause** : panne d'un disque non détectée, car les alertes du NAS étaient envoyées à une ancienne adresse courriel.
- **Ce qui a bien fonctionné** : sauvegarde de la veille intacte; communication régulière aux 30 minutes.
- **Ce qui doit s'améliorer** : 5 indisponibilités du stockage au T3 montrent une fragilité. Le dernier test de restauration complet datait de 7 mois, d'où le constat F3 du [rapport](rapport-audit.md).
- **Actions** : alertes redirigées vers `soutien@`; test de restauration mensuel; remplacement du NAS budgété pour 2027.

## 4. Liste des contacts d'urgence (fictifs)

| Rôle | Contact |
|---|---|
| Responsable TI | Thomas Caron, poste 2020 |
| Soutien TI | Barbara Saroukou, poste 2021 |
| Fournisseur NAS | Ligne de soutien fictive, contrat n° NB-2024-118 |
| Fournisseur Internet | Ligne de soutien fictive, compte n° 55-0192 |
