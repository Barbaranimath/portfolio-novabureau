# NovaBureau : laboratoire de soutien TI et de conformité

> Simulation complète du service TI d'une PME montréalaise fictive de 20 employés : centre de soutien, gestion des accès, évaluation de conformité inspirée des **CIS Controls v8** et du **NIST CSF 2.0**, sensibilisation et base de connaissances.
>
> **Projet personnel, environnement entièrement fictif.** Ni audit officiel ni certification.

**Autrice** : Barbara Saroukou · [LinkedIn](https://linkedin.com/in/nimath-barbara-saroukou-906851207) · [Portfolio](https://portfolio-ashy-nine-41.vercel.app)

## En chiffres

| | |
|---|---|
| **120** billets fictifs analysés (T3 2026) | **93 %** pris en charge dans le délai cible, **86 %** résolus dans le SLA |
| **4,4/5** de satisfaction | **56 %** de résolution au premier contact |
| **5** incidents documentés de bout en bout | Hameçonnage contenu en **27 minutes** |
| **12** contrôles de sécurité évalués | Score de conformité : **63 % → 92 %** projeté avec le plan d'action |
| **23** comptes et **9** groupes révisés | **6** écarts trouvés, dont un compte orphelin actif depuis 54 jours |
| **7** guides utilisateurs | **3** scripts Python reproductibles |

## Ce que démontre ce projet

| Compétence | Où la voir |
|---|---|
| Diagnostic et résolution méthodiques | [Billets INC-001 à INC-005](03-soutien-utilisateurs/billets/) |
| Gestion des priorités et des SLA | [Catalogue et matrice de priorité](03-soutien-utilisateurs/catalogue-et-priorites.md) |
| Analyse de données du soutien | [Indicateurs T3](03-soutien-utilisateurs/indicateurs-T3-2026.md) · [`scripts/indicateurs.py`](scripts/indicateurs.py) |
| Cycle de vie des comptes (arrivées et départs) | [Arrivée](04-gestion-acces/procedure-arrivee.md) · [Départ](04-gestion-acces/procedure-depart.md) |
| Moindre privilège et RBAC | [Matrice des accès](04-gestion-acces/matrice-acces.md) · [Revue trimestrielle](04-gestion-acces/revue-acces-T4-2026.md) |
| Évaluation de conformité et gestion des risques | [Grille des contrôles](05-conformite/evaluation-conformite.md) · [Rapport d'audit](05-conformite/rapport-audit.md) |
| Continuité des activités | [Plan de sauvegarde et de continuité](05-conformite/plan-continuite-sauvegarde.md) |
| Communication et sensibilisation | [Campagne](06-sensibilisation/campagne-hameconnage-mfa.md) · [Affiche](06-sensibilisation/affiche-signaler.html) · [Quiz](06-sensibilisation/quiz-hameconnage-mfa.md) |
| Rédaction technique vulgarisée | [Base de connaissances](07-base-connaissances/) |
| Automatisation | [`scripts/comptes_inactifs.py`](scripts/comptes_inactifs.py) · [Ébauche PowerShell](08-ameliorations/feuille-de-route.md) |

## Structure du dépôt

```
portfolio-novabureau/
├── README.md
├── 01-description-entreprise/   Profil, organigramme, rôles
├── 02-environnement-ti/         Schéma réseau, principes, inventaire des actifs
├── 03-soutien-utilisateurs/     Catalogue, priorités, 5 billets, indicateurs
├── 04-gestion-acces/            Arrivée, départ, matrice RBAC, revue des accès
├── 05-conformite/               Grille CIS/NIST, rapport d'audit, continuité
├── 06-sensibilisation/          Courriel, procédure, affiche, quiz
├── 07-base-connaissances/       7 guides utilisateurs
├── 08-ameliorations/            Feuille de route et automatisation
├── donnees/                     Employés, registre des billets, export de l'annuaire (fictifs)
└── scripts/                     Génération des données, indicateurs, contrôle des comptes
```

## Reproduire les analyses

Python 3.10 ou plus, aucune dépendance externe.

```bash
python scripts/generer_billets.py      # régénère donnees/registre-billets.csv (graine fixe)
python scripts/indicateurs.py          # recalcule 03-soutien-utilisateurs/indicateurs-T3-2026.md
python scripts/comptes_inactifs.py     # contrôle mensuel des comptes (MFA, orphelins, groupes)
```

Exemple de sortie du contrôle des comptes :

```
Contrôle des comptes au 2026-10-15 — 24 comptes actifs analysés
Couverture MFA des employés : 16/20 (80 %)
6 constat(s) :
  [ÉLEVÉ] amina.diallo           MFA non inscrit
  ...
  [ÉLEVÉ] hugo.leblanc           Membre de GRP-Ventes, hors matrice et sans exception approuvée
  [ÉLEVÉ] stagiaire.ete2026      Compte actif sans employé correspondant aux RH (compte orphelin)
```

## Résumé du projet

J'ai créé un laboratoire de soutien TI et de conformité pour une PME fictive de 20 employés. J'ai conçu un catalogue de services et une matrice de priorité, documenté 5 incidents résolus et analysé un registre de 120 billets avec Python (93 % de prise en charge dans les délais, satisfaction de 4,4/5). J'ai rédigé les procédures d'arrivée et de départ, une matrice des accès fondée sur le moindre privilège, et mené une revue des accès qui a révélé 6 écarts. Mon évaluation de 12 contrôles inspirés des CIS Controls et du NIST CSF établit un score de 63 %, avec un plan d'action pour atteindre 92 %. Le projet comprend aussi une campagne de sensibilisation et 7 guides utilisateurs.

## Avertissement

Toutes les personnes, organisations, adresses (domaine réservé `.example`), incidents et données sont fictifs. Les références aux CIS Controls et au NIST CSF servent de cadre d'inspiration; elles n'impliquent aucune affiliation ni certification.
