# Améliorations et feuille de route

Ce qui pourrait rendre le service TI de NovaBureau plus fiable, plus rapide et moins dépendant de tâches manuelles.

## Priorisation

| # | Amélioration | Problème résolu | Gain estimé | Effort | Priorité |
|---|---|---|---|---|---|
| 1 | **Désactivation automatique des comptes** à partir du système RH | Comptes orphelins (constat F2) | 0 compte actif après un départ; environ 30 min gagnées par départ | Moyen | 🔴 Haute |
| 2 | **Accès conditionnel** : bloquer toute connexion sans MFA ou depuis un appareil non géré | MFA incomplet (F1) | 100 % des connexions protégées | Faible | 🔴 Haute |
| 3 | **Gestion des appareils (MDM, ex. Intune)** : chiffrement, mises à jour et applications imposés par politique | Postes non chiffrés ou en retard (F4, F6) | Conformité des postes vérifiée en continu | Moyen | 🔴 Haute |
| 4 | **Tests de restauration automatisés et mensuels** avec rapport | Sauvegardes non testées (F3) | Preuve mensuelle prête pour les clients | Faible | 🟠 Moyenne |
| 5 | **Centralisation des journaux** (pare-feu, VPN, Microsoft 365) avec alertes | Détection lente des anomalies | Alerte en moins de 15 min sur une connexion inhabituelle | Élevé | 🟠 Moyenne |
| 6 | **Réinitialisation de mot de passe en libre-service** promue activement | 30 % des billets sont des mots de passe ou des comptes verrouillés | Environ 25 billets en moins par trimestre | Faible | 🟠 Moyenne |
| 7 | **Tableau de bord des indicateurs** (Power BI ou Streamlit) alimenté par le registre des billets | Indicateurs calculés à la main | Suivi hebdomadaire en temps réel | Moyen | 🟢 Basse |
| 8 | **Revues des accès avec attestation en ligne** par les gestionnaires | Revue trimestrielle manuelle (4 h) | Revue réduite à environ 1 h | Moyen | 🟢 Basse |

## Ébauche : automatisation du départ (amélioration 1)

Exemple de logique en PowerShell avec Microsoft Graph, à titre de **démonstration** (non exécuté sur un vrai locataire) :

```powershell
# Désactivation d'un compte au départ — démonstration
param([Parameter(Mandatory)] [string] $Utilisateur)

Connect-MgGraph -Scopes "User.ReadWrite.All","GroupMember.ReadWrite.All"
$u = Get-MgUser -UserId $Utilisateur

Update-MgUser -UserId $u.Id -AccountEnabled:$false            # 1. Désactiver
Revoke-MgUserSignInSession -UserId $u.Id                      # 2. Révoquer les sessions
Get-MgUserMemberOf -UserId $u.Id | ForEach-Object {           # 3. Retirer les groupes
    Remove-MgGroupMemberByRef -GroupId $_.Id -DirectoryObjectId $u.Id -ErrorAction SilentlyContinue
}
Get-MgUserAuthenticationMethod -UserId $u.Id | Out-File "preuves/$Utilisateur-mfa-avant.txt"
"$(Get-Date -Format s) | $Utilisateur | désactivé, sessions révoquées, groupes retirés" |
    Add-Content "preuves/journal-departs.log"                 # 4. Conserver la preuve
```

## Leçons apprises du projet

- **La documentation est un contrôle de sécurité** : sans billet ni preuve, impossible de démontrer qu'un accès a été retiré.
- **Les données du soutien orientent la prévention** : l'analyse du registre a guidé quels guides écrire en premier.
- **Le moindre privilège se maintient, il ne se configure pas une seule fois** : la première revue des accès a révélé 6 écarts en seulement quelques mois.
