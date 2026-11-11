# INC-005 — Courriel suspect (tentative d'hameçonnage)

| Champ | Valeur |
|---|---|
| Ouvert le | 2026-10-28 10:31 (bouton « Signaler ») |
| Demandeur | Louis Pelletier (E08), commis comptable, Finance |
| Priorité | **P2 — Élevée** (message reçu par plusieurs personnes du service Finance; risque de fraude) |
| Assigné à | Barbara Saroukou, escaladé à Thomas Caron |
| Pris en charge | 10:36 (5 min, cible 1 h) |
| Contenu | 10:58 (27 min) |
| Statut | Fermé, rapport transmis à la direction |

## Description

Courriel fictif reçu : « Facture impayée — action requise avant 17 h », prétendument d'un fournisseur réel de NovaBureau, avec un lien « Consulter la facture ».

## Analyse

| Indicateur | Constat |
|---|---|
| Expéditeur affiché | « Service comptabilité — Fournitures Delta » |
| Domaine réel | `fournitures-delta-paiement.example` : **différent** du domaine habituel du fournisseur |
| Authentification | SPF : échec; DMARC : échec |
| Lien | Le texte affiche le portail du fournisseur, mais la cible réelle est une page imitant la connexion Microsoft 365 |
| Pièce jointe | Aucune |
| Signaux d'urgence | Délai de « 17 h », menace de pénalité, ton pressant |
| Destinataires | **4 employés** du service Finance (E05 à E08) |

## Actions

1. Consigne immédiate à l'utilisateur : ne pas cliquer, ne pas répondre, ne pas transférer.
2. Recherche du message dans toutes les boîtes : 4 destinataires trouvés, **suppression du message des 4 boîtes**.
3. Blocage du domaine expéditeur et de l'URL dans le filtre de messagerie.
4. Vérification des clics : une employée (E07) avait ouvert le lien, **sans saisir ses identifiants**. Par précaution : révocation de ses sessions, revue des connexions des 48 dernières heures (rien d'anormal) et **activation de son MFA**, qui n'était pas encore configuré (l'un des 4 comptes non conformes relevés dans l'[évaluation de conformité](../../05-conformite/evaluation-conformite.md)).
5. Appel au fournisseur, par le numéro connu (et non celui du courriel) : il confirme ne pas avoir envoyé ce message.
6. Avis au service Finance : rappel de la procédure de vérification de tout changement de coordonnées bancaires d'un fournisseur.

## Résultat

- Aucune compromission de compte, aucun paiement effectué.
- Temps entre le signalement et le confinement : **27 minutes**.
- Remerciement public (avec son accord) à l'employé qui a signalé le message, pour encourager les signalements.
- Le cas a servi d'exemple anonymisé dans la [campagne de sensibilisation](../../06-sensibilisation/).

## Leçon retenue

L'employée qui a cliqué n'avait pas encore suivi la formation anti-hameçonnage. Ce constat a fait passer la formation de « recommandée » à **obligatoire dans les 30 jours suivant l'arrivée**.
