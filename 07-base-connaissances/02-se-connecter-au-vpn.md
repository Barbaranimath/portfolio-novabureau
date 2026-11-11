# Se connecter au VPN

**Objectif** : accéder au stockage partagé et aux ressources internes depuis la maison. · **Temps** : 2 min · **Pour qui** : télétravailleurs

> Le courriel, Teams et OneDrive fonctionnent **sans** VPN. Le VPN sert uniquement aux lecteurs réseau (`\\NAS-01`).

## Étapes

1. Vérifiez que votre connexion Internet fonctionne (ouvrez un site Web).
2. Ouvrez l'application **Client VPN** dans le menu Démarrer.
3. Vérifiez que le serveur est `vpn.novabureau.example`.
4. Cliquez sur **Connecter** et entrez votre adresse courriel et votre mot de passe NovaBureau.
5. Approuvez la demande dans votre application d'authentification.
6. Attendez l'icône verte « Connecté », puis ouvrez l'Explorateur de fichiers : vos lecteurs réseau doivent apparaître.
7. Déconnectez-vous à la fin de la journée.

## Erreurs fréquentes

| Message ou symptôme | Cause probable | Solution |
|---|---|---|
| « Échec de l'authentification » | Mot de passe changé récemment ou erreur de saisie | Vérifiez en vous connectant à Microsoft 365 avec le même mot de passe |
| Aucune notification MFA | Nouveau téléphone sans transfert du MFA | **Vous changez de téléphone ? Transférez d'abord votre MFA** (guide 03), sinon contactez le soutien |
| « Version du client non prise en charge » | Client VPN trop ancien | Ouvrez le **Portail d'entreprise** et installez la mise à jour du client VPN |
| Connecté, mais les lecteurs n'apparaissent pas | Lecteurs non reconnectés | Redémarrez l'Explorateur ou l'ordinateur, VPN connecté |
| Le Wi-Fi d'un hôtel ou d'un café bloque le VPN | Réseau public restrictif | Utilisez le partage de connexion de votre téléphone |

## Besoin d'aide ?

Portail de billets ou `soutien@novabureau.example` · Urgence : poste 2020 · Délai cible : 4 heures.
