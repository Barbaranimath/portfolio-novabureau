# Évaluation de conformité — grille des contrôles

> Évaluation **fictive**, inspirée des *CIS Critical Security Controls v8* (groupe de mise en œuvre IG1, adapté aux PME) et des fonctions du *NIST Cybersecurity Framework 2.0*. Elle ne constitue pas une certification officielle.

**Date** : 2026-10-15 · **Évaluatrice** : Barbara Saroukou · **Portée** : 20 employés, 25 actifs, Microsoft 365, réseau du bureau et VPN

## Échelle utilisée

| État | Signification |
|---|---|
| ✅ Conforme | Le contrôle est en place **et** une preuve le démontre |
| 🟡 Partiellement conforme | En place pour une partie du périmètre ou sans preuve complète |
| 🔴 Non conforme | Absent ou non appliqué |

Le **risque** combine la probabilité qu'une faille soit exploitée et son impact sur NovaBureau (Faible, Moyen, Élevé).

## Grille

| # | Contrôle | Réf. CIS v8 | Fonction NIST CSF | État | Constat mesuré | Preuve examinée | Risque | Recommandation |
|---|---|---|---|---|---|---|---|---|
| C1 | Inventaire des actifs à jour | 1.1 | Identifier | ✅ | 25/25 actifs inventoriés avec leur responsable | [inventaire-actifs.csv](../02-environnement-ti/inventaire-actifs.csv) | Faible | Revue trimestrielle |
| C2 | MFA activé pour tous les comptes | 6.3, 6.5 | Protéger | 🟡 | **16/20 employés (80 %)**; 100 % des comptes `adm-` | Rapport MFA, sortie de `comptes_inactifs.py` | Élevé | Activer le MFA des 4 comptes restants avant le 2026-11-15, puis bloquer l'accès sans MFA |
| C3 | Comptes inactifs ou orphelins désactivés | 5.3 | Protéger | 🔴 | 1 compte orphelin actif depuis 54 jours (stagiaire parti) | Export de l'annuaire comparé à la liste RH | Moyen | Contrôle mensuel automatisé; départ déclenché par les RH |
| C4 | Accès révisés périodiquement | 6.1, 6.2 | Protéger | 🔴 | Aucune revue documentée avant octobre 2026; 1 accès résiduel après un changement de poste | [revue-acces-T4-2026.md](../04-gestion-acces/revue-acces-T4-2026.md) | Élevé | Revue trimestrielle validée par les gestionnaires |
| C5 | Comptes administrateurs séparés | 5.4 | Protéger | ✅ | 2/2 membres TI ont un compte `adm-` distinct | Liste des comptes privilégiés | Faible | Maintenir |
| C6 | Antivirus actif et à jour | 10.1 | Détecter | ✅ | 20/20 postes protégés, définitions à moins de 24 h | Rapport de protection Defender | Moyen | Maintenir la surveillance |
| C7 | Mises à jour du système appliquées | 7.3 | Protéger | 🟡 | 19/20 postes à jour (**95 %**); PC-007 en retard de 35 jours | Rapport de conformité des postes | Moyen | Alerte à 21 jours sans mise à jour |
| C8 | Chiffrement des postes | 3.6 | Protéger | 🟡 | 19/20 postes chiffrés (**95 %**); PC-014 non chiffré | Rapport BitLocker | Élevé | Activer BitLocker sur PC-014 immédiatement |
| C9 | Sauvegardes testées | 11.2, 11.5 | Récupérer | 🟡 | Sauvegarde quotidienne en place, **dernier test de restauration il y a 7 mois** | Journal des sauvegardes, rapport de restauration de mars 2026 | Élevé | Test de restauration mensuel documenté |
| C10 | Formation anti-hameçonnage | 14.1 | Protéger | 🟡 | **14/20 employés formés (70 %)**; nouveaux employés non formés à l'arrivée | Registre de formation | Moyen | Former tous les employés; formation obligatoire dans les 30 jours suivant l'arrivée |
| C11 | Journaux de connexion conservés | 8.2, 8.3 | Détecter | ✅ | 90 jours de journaux Microsoft 365 | Paramètres de rétention | Moyen | Centraliser les journaux du pare-feu et du VPN |
| C12 | Wi-Fi Invités isolé | 12.2 | Protéger | ✅ | Aucun accès au réseau interne depuis le SSID Invités (test effectué) | Capture du test de connectivité | Faible | Maintenir |

## Synthèse

| État | Nombre | Part |
|---|---|---|
| ✅ Conforme | 5 | 42 % |
| 🟡 Partiellement conforme | 5 | 42 % |
| 🔴 Non conforme | 2 | 17 % |

**Score de conformité pondéré : 63 %** (Conforme = 1 point, Partiel = 0,5 point, Non conforme = 0 point → 7,5/12).

Les **4 contrôles à risque élevé** (C2, C4, C8 et C9) sont traités en priorité dans le [plan d'action](rapport-audit.md#7-plan-daction).
