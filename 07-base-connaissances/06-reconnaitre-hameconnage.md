# Reconnaître une tentative d'hameçonnage

**Objectif** : repérer en 30 secondes les signes d'un courriel, d'un texto ou d'un appel frauduleux. · **Temps de lecture** : 4 min

## La méthode en 4 questions

1. **Est-ce que je l'attendais ?** Une facture d'un fournisseur avec qui vous ne faites pas affaire, un colis que vous n'avez pas commandé…
2. **Me presse-t-on ?** Délai court, menace de suspension, pénalité : l'urgence est l'outil préféré des fraudeurs.
3. **Qui l'envoie vraiment ?** Regardez l'adresse complète, pas seulement le nom affiché.
4. **Où mène le lien ?** Survolez-le (ou appuyez longuement sur mobile) **sans cliquer**.

## Comment lire une adresse Web

Le vrai domaine est ce qui se trouve juste avant le premier `/` et se termine par l'extension (`.com`, `.ca`, `.example`…).

| Adresse | Domaine réel | Fiable ? |
|---|---|---|
| `https://portail.novabureau.example/factures` | `novabureau.example` | ✅ |
| `https://novabureau.example.connexion-securisee.com` | `connexion-securisee.com` | ❌ |
| `https://n0vabureau.example` (zéro au lieu du o) | `n0vabureau.example` | ❌ |

## Autres signaux

- Demande de mot de passe, de code MFA ou d'informations bancaires.
- Pièce jointe inattendue (`.zip`, `.html`, `.exe`, document Office qui demande d'« activer le contenu »).
- Changement des coordonnées bancaires d'un fournisseur.
- Fautes inhabituelles ou formule générique (« Cher client »).
- Demande MFA sur votre téléphone que vous n'avez pas déclenchée.

## Exemple fictif annoté

> **De** : Service comptabilité — Fournitures Delta `<facturation@fournitures-delta-paiement.example>` ⬅️ *domaine différent de celui du fournisseur*
> **Objet** : Facture impayée — action requise avant 17 h ⬅️ *urgence*
> Votre compte sera suspendu et des frais de 250 $ seront appliqués. ⬅️ *menace*
> [Consulter la facture] ⬅️ *le lien mène à une fausse page de connexion*

## Erreurs fréquentes

- Se fier au nom affiché de l'expéditeur, qui peut être choisi librement.
- Penser qu'un message bien écrit, avec un logo, est forcément légitime.
- Croire qu'on « n'a rien d'intéressant à voler » : votre compte donne accès aux données clients.

## Besoin d'aide ?

Un doute ? Signalez (guide 04) · `soutien@novabureau.example` · poste 2020.
