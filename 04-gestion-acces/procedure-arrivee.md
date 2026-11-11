# Procédure d'arrivée d'un employé (onboarding)

**Propriétaire** : Soutien et conformité TI · **Déclencheur** : demande officielle des RH · **Délai** : poste prêt 1 jour ouvrable avant l'arrivée · **Version** : 1.2 (2026-10)

## Principe

Le **moindre privilège** : chaque personne reçoit uniquement les permissions nécessaires à son travail, attribuées par groupe de département selon la [matrice des accès](matrice-acces.md). Tout accès supplémentaire suit la procédure de demande d'accès, avec l'approbation du gestionnaire.

## Déroulement

```mermaid
graph LR
    RH[Demande RH] --> C[Compte + licence] --> G[Groupes] --> P[Poste préparé] --> M[MFA] --> R[Remise + tests] --> F[Fermeture]
```

## Liste de contrôle — exemple : Sophie Martin, adjointe administrative (arrivée le 2026-10-05)

Billet `REQ-ONB-014` · Demande RH reçue le 2026-09-24 de Nadia Benali.

| # | Étape | Fait par | Date | Preuve conservée | ✓ |
|---|---|---|---|---|---|
| 1 | Recevoir l'autorisation officielle des RH (nom, poste, département, gestionnaire, date d'arrivée) | B. Saroukou | 2026-09-24 | Formulaire RH joint au billet | ✅ |
| 2 | Créer le compte `sophie.martin` (aucun compte administrateur) | B. Saroukou | 2026-09-29 | Capture de la console | ✅ |
| 3 | Attribuer la licence Microsoft 365 Business Premium | B. Saroukou | 2026-09-29 | Rapport des licences | ✅ |
| 4 | Ajouter au groupe `GRP-Administration` et `GRP-Tous` **seulement** | B. Saroukou | 2026-09-29 | Liste des membres du groupe | ✅ |
| 5 | Préparer PC-015 : image standard, mises à jour, chiffrement BitLocker | B. Saroukou | 2026-09-30 | Rapport de conformité du poste | ✅ |
| 6 | Installer et vérifier l'antivirus (définitions à jour, analyse complète) | B. Saroukou | 2026-09-30 | Rapport Defender | ✅ |
| 7 | Préparer l'inscription MFA (activée lors de la première connexion, en présence du TI) | B. Saroukou | 2026-10-05 | Rapport d'inscription MFA | ✅ |
| 8 | Vérifier que seuls les accès nécessaires sont actifs (aucun accès Finance, RH ou Ventes) | B. Saroukou | 2026-10-05 | Rapport des permissions effectives | ✅ |
| 9 | Remettre le matériel et les consignes de sécurité (politique d'utilisation acceptable signée) | B. Saroukou | 2026-10-05 | Formulaire de remise signé | ✅ |
| 10 | Tester avec l'employée : connexion, courriel, Teams, dossier Administration, imprimante | B. Saroukou | 2026-10-05 | Notes de test dans le billet | ✅ |
| 11 | Inscrire l'actif PC-015 à son nom dans l'inventaire | B. Saroukou | 2026-10-05 | [inventaire-actifs.csv](../02-environnement-ti/inventaire-actifs.csv) | ✅ |
| 12 | Inscrire à la formation anti-hameçonnage (à suivre dans les 30 jours) | B. Saroukou | 2026-10-05 | Registre de formation | ✅ |
| 13 | Fermer la demande et informer les RH et le gestionnaire | B. Saroukou | 2026-10-05 | Courriel de fermeture | ✅ |

**Résultat** : poste prêt le 2026-09-30, soit 3 jours ouvrables avant l'arrivée; employée productive dès 10 h le premier jour.

## Contrôles qualité

- Un compte n'est **jamais** créé sans demande RH écrite (même à la demande d'un gestionnaire).
- Aucun accès « copié » sur un collègue : on part de la matrice, pas d'un profil existant qui pourrait avoir accumulé des exceptions.
- Le mot de passe initial est temporaire, transmis séparément, et doit être changé à la première connexion.
