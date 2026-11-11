# Matrice des accès (RBAC)

Les permissions sont attribuées **par groupe**, jamais directement à une personne. Version en vigueur : 2026-10-15. Prochaine revue : 2027-01-15.

## Matrice standard

| Groupe | Courriel / Teams | Dossier général | Finance | RH | Ventes / CRM | Administration | Consoles TI |
|---|---|---|---|---|---|---|---|
| Direction | Oui | Oui | Lecture | Lecture | Lecture | Oui | Non |
| Finance | Oui | Oui | **Modification** | Non | Non | Non | Non |
| RH | Oui | Oui | Non | **Modification** | Non | Non | Non |
| Ventes | Oui | Oui | Non | Non | **Modification** | Limité (lecture du calendrier des salles) | Non |
| Administration | Oui | Oui | Non | Non | Non | **Modification** | Non |
| TI | Oui | Oui | Selon le besoin, sur billet approuvé | Selon le besoin, sur billet approuvé | Selon le besoin, sur billet approuvé | Oui | Oui, **avec compte `adm-` séparé** |

## Exceptions approuvées en vigueur

| Employé | Accès supplémentaire | Justification | Approbateur | Expiration |
|---|---|---|---|---|
| Sophie Martin (E15) | `Ventes\Soumissions`, modification | Mise en forme des soumissions ([INC-003](../03-soutien-utilisateurs/billets/INC-003-acces-dossier-partage.md)) | É. Fortin | 2027-01-07 |
| Isabelle Roy (E05) | RH\Paie, lecture | Rapprochement de la paie | N. Benali | 2027-03-31 |

## Comptes privilégiés

| Compte | Titulaire | Usage autorisé | MFA | Revue |
|---|---|---|---|---|
| `adm-thomas.caron` | Responsable TI | Administration complète | Oui (clé matérielle) | Mensuelle |
| `adm-barbara.saroukou` | Agente soutien et conformité TI | Gestion des utilisateurs et des groupes; aucun accès aux paramètres globaux | Oui | Mensuelle |
| `break-glass-01` | Coffre-fort scellé | Urgence seulement, si les deux comptes ci-dessus sont inaccessibles | Oui | Test semestriel |

## Règles

1. Toute demande d'accès hors matrice exige l'approbation **écrite** du propriétaire des données.
2. Les exceptions ont **toujours** une date d'expiration (12 mois au maximum).
3. Les permissions sont révisées chaque trimestre, et après tout changement de poste ou départ (voir [revue-acces-T4-2026.md](revue-acces-T4-2026.md)).
4. Les comptes `adm-` ne servent ni à lire le courriel ni à naviguer sur Internet.
