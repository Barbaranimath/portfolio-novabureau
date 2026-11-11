# Revue trimestrielle des accès — T4 2026

| Élément | Détail |
|---|---|
| Date | 2026-10-15 |
| Réalisée par | Barbara Saroukou |
| Validée par | Gestionnaires de chaque département, puis Thomas Caron |
| Portée | 20 comptes utilisateurs, 3 comptes privilégiés, 9 groupes de sécurité, 4 dossiers partagés |
| Méthode | Export des membres des groupes, comparaison avec la liste RH et la matrice des accès, validation ligne par ligne par chaque gestionnaire |

## Constats

| # | Constat | Gravité | Action | Statut |
|---|---|---|---|---|
| 1 | Hugo Leblanc (E18) est toujours membre de `GRP-Ventes` depuis son transfert des Ventes à l'Administration en juin 2026 | Élevée | Retrait du groupe; aucune activité dans le dossier Ventes depuis son transfert (journaux vérifiés) | ✅ Corrigé le 2026-10-15 |
| 2 | Le compte d'un stagiaire parti en août 2026 (`stagiaire.ete2026`) est encore actif | Élevée | Désactivation et revue des connexions : dernière connexion le 2026-08-22, aucune activité depuis | ✅ Corrigé le 2026-10-15 |
| 3 | 4 employés n'ont pas encore activé le MFA (E07, E13, E14, E17) | Élevée | Activation accompagnée planifiée; accès bloqué au 2026-11-15 sans MFA | 🔄 En cours (1 sur 4 au 2026-10-28) |
| 4 | Exception de lecture RH\Paie pour E05 sans date d'expiration | Moyenne | Date d'expiration fixée au 2027-03-31, approuvée par N. Benali | ✅ Corrigé |
| 5 | Le dossier `Projets-2021` est accessible à `GRP-Tous` alors qu'il contient d'anciens contrats | Moyenne | Restreint à Direction; archivage proposé | ✅ Corrigé |
| 6 | Le compte `break-glass-01` n'a jamais été testé | Faible | Test planifié le 2026-12-01 | ⏳ Planifié |

## Résultats chiffrés

- **23 comptes** et **9 groupes** révisés, **6 écarts** trouvés.
- 5 des 6 écarts corrigés ou en cours dans la journée.
- Après correction : **0 compte orphelin**, **0 accès résiduel** lié à un changement de poste, **100 %** des exceptions avec une date d'expiration.

## Approbations

| Département | Gestionnaire | Validation |
|---|---|---|
| Direction | Claire Bouchard | ✅ 2026-10-16 |
| Finance | Isabelle Roy | ✅ 2026-10-16 |
| RH | Nadia Benali | ✅ 2026-10-17 |
| Ventes | Émilie Fortin | ✅ 2026-10-16 |
| Administration | Antoine Lavoie | ✅ 2026-10-17 |
| TI | Thomas Caron | ✅ 2026-10-17 |
