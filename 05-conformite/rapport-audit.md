# Rapport d'évaluation de la sécurité TI — NovaBureau

> Rapport **fictif**, produit dans le cadre d'un projet de portfolio. Il ne constitue ni un audit officiel ni une certification.

| | |
|---|---|
| **Destinataires** | Claire Bouchard (directrice générale), Thomas Caron (responsable TI) |
| **Préparé par** | Barbara Saroukou, agente soutien et conformité TI |
| **Période évaluée** | 1er juillet au 15 octobre 2026 |
| **Date du rapport** | 2026-10-20 |

## 1. Résumé pour la direction

NovaBureau a de bonnes bases (antivirus, inventaire, comptes administrateurs séparés, Wi-Fi Invités isolé), mais **4 lacunes exposent directement les données clients** : MFA incomplet, accès jamais révisés avant octobre, un poste non chiffré et des sauvegardes non testées depuis 7 mois.

**Score de conformité actuel : 63 %. Objectif réaliste au 2027-01-31 : 92 %**, sans achat de logiciel supplémentaire, en appliquant le plan d'action de la section 7 (environ 24 heures de travail TI sur 3 mois).

## 2. Objectif

Mesurer l'état des contrôles de sécurité essentiels, identifier les risques prioritaires et proposer un plan d'action réaliste pour une PME de 20 employés, en réponse aux demandes de preuves de deux clients.

## 3. Portée

- **Inclus** : 20 comptes employés et 3 comptes privilégiés, 20 portables, Microsoft 365, réseau du bureau, VPN, stockage partagé et sauvegardes, formation des employés.
- **Exclus** : sécurité physique des locaux, fournisseurs tiers (hors sauvegarde), développement logiciel.

## 4. Méthode

1. Sélection de 12 contrôles tirés des *CIS Controls v8* (IG1) et classés selon les fonctions du *NIST CSF 2.0*.
2. Collecte des preuves : exports de l'annuaire, rapports Defender et BitLocker, journaux de sauvegarde, registre de formation.
3. Analyse automatisée des comptes avec [`scripts/comptes_inactifs.py`](../scripts/comptes_inactifs.py).
4. Entrevues avec les 6 gestionnaires pour valider les accès de leur équipe.
5. Cotation de chaque contrôle (conforme, partiel, non conforme) et du risque.

## 5. Constats principaux

Le détail des 12 contrôles se trouve dans la [grille d'évaluation](evaluation-conformite.md).

| # | Constat | Risque | Pourquoi c'est important |
|---|---|---|---|
| F1 | 4 employés sur 20 sans MFA, dont 2 en Ventes et 1 en Finance | **Élevé** | Un mot de passe volé par hameçonnage suffit pour accéder au courriel et aux fichiers. L'incident [INC-005](../03-soutien-utilisateurs/billets/INC-005-courriel-suspect.md) l'a démontré : l'employée qui a cliqué n'avait pas de MFA. |
| F2 | Aucune revue des accès avant octobre 2026 | **Élevé** | La première revue a révélé 6 écarts, dont un compte de stagiaire actif 54 jours après son départ. |
| F3 | Dernier test de restauration il y a 7 mois | **Élevé** | 5 indisponibilités du stockage partagé au T3 : une sauvegarde jamais testée pourrait échouer le jour où on en a besoin. |
| F4 | 1 portable sur 20 non chiffré (PC-014, Ventes) | **Élevé** | En cas de vol, les données clients seraient lisibles. |
| F5 | 30 % des employés non formés à l'hameçonnage | Moyen | L'hameçonnage est le premier vecteur d'attaque contre les PME. |
| F6 | 1 poste en retard de mises à jour de 35 jours | Moyen | Vulnérabilités connues non corrigées. |

## 6. Points forts

- 100 % des postes protégés par un antivirus à jour.
- Inventaire complet et attribué.
- Comptes administrateurs séparés et protégés par MFA.
- Centre de soutien efficace : **93 %** des billets pris en charge dans le délai cible et **4,4/5** de satisfaction au T3 (voir les [indicateurs](../03-soutien-utilisateurs/indicateurs-T3-2026.md)).

## 7. Plan d'action

| # | Action | Constat | Responsable | Effort | Échéance | Statut au 2026-11-10 |
|---|---|---|---|---|---|---|
| A1 | Accompagner l'inscription MFA des 4 comptes, puis bloquer l'accès sans MFA (accès conditionnel) | F1 | B. Saroukou | 3 h | 2026-11-15 | 🔄 1 sur 4 fait |
| A2 | Activer BitLocker sur PC-014 et vérifier la clé de récupération | F4 | B. Saroukou | 1 h | 2026-10-24 | ✅ Fait |
| A3 | Désactiver le compte orphelin et corriger l'accès résiduel | F2 | B. Saroukou | 1 h | 2026-10-15 | ✅ Fait |
| A4 | Instaurer la revue trimestrielle des accès, validée par les gestionnaires | F2 | B. Saroukou | 4 h / trimestre | 2027-01-15 | ⏳ Planifié |
| A5 | Exécuter `comptes_inactifs.py` chaque mois et consigner le résultat | F2 | B. Saroukou | 30 min / mois | Mensuel | 🔄 En place |
| A6 | Test de restauration mensuel (1 dossier, 1 boîte courriel), avec rapport | F3 | T. Caron | 2 h / mois | 2026-11-30 | ⏳ Planifié |
| A7 | Former les 6 employés restants; formation obligatoire dans les 30 jours suivant l'arrivée | F5 | B. Saroukou | 4 h | 2026-12-15 | 🔄 Campagne lancée |
| A8 | Alerte pour tout poste sans mise à jour depuis 21 jours | F6 | T. Caron | 2 h | 2026-11-30 | ⏳ Planifié |
| A9 | Tester le compte d'urgence `break-glass-01` | — | T. Caron | 1 h | 2026-12-01 | ⏳ Planifié |

## 8. Projection

| Étape | Contrôles conformes | Score |
|---|---|---|
| 2026-10-15 (évaluation) | 5/12 | 63 % |
| Après A1 à A3 (2026-11-15) | 8/12 (C2, C3, C8 corrigés) | 79 % |
| Après le plan complet (2027-01-31) | 10/12 conformes; C9 et C10 restent partiels (3 tests de restauration consécutifs et 100 % de formation exigés) | **92 %** |

## 9. Conclusion

Les risques les plus graves se corrigent avec la configuration existante de Microsoft 365 et une discipline de documentation, sans investissement majeur. La priorité absolue est le **MFA à 100 %**, suivi de la **revue des accès** et des **tests de restauration**. Une réévaluation complète est recommandée en avril 2027.
