# INC-002 — Ordinateur lent

| Champ | Valeur |
|---|---|
| Ouvert le | 2026-09-22 13:10 (portail) |
| Demandeur | Amina Diallo (E07), analyste financière, Finance |
| Actif | PC-007 |
| Priorité | **P3 — Moyenne** (1 personne, contournement possible) |
| Assigné à | Barbara Saroukou |
| Pris en charge | 13:55 (45 min, cible 4 h) |
| Résolu | 15:20 (2 h 10, cible 8 h) |
| Statut | Fermé, confirmé par l'utilisateur |

## Description

Le démarrage prend plus de 6 minutes et Excel gèle lors de l'ouverture des classeurs de fin de mois.

## Diagnostic (prise en main à distance, avec l'accord de l'utilisatrice)

| Vérification | Constat |
|---|---|
| Espace disque | 9 Go libres sur 256 Go (**3,5 %**) |
| Processus actifs | Synchronisation OneDrive bloquée en boucle (40 % du processeur) |
| Mises à jour | Poste resté en Windows 11 **23H2**, 2 mises à jour cumulatives en attente |
| Antivirus | Defender actif, définitions à jour, aucune menace détectée |
| Programmes au démarrage | 11 programmes, dont 3 inutiles (outils d'imprimantes d'un ancien poste, lanceur de jeux) |

## Résolution

1. Nettoyage des fichiers temporaires et du dossier Téléchargements (avec l'accord de l'utilisatrice) : **+38 Go** libérés.
2. Activation de « Fichiers à la demande » dans OneDrive et correction du fichier en conflit qui bloquait la synchronisation.
3. Application des mises à jour en attente et passage en 24H2.
4. Désactivation de 3 programmes inutiles au démarrage.
5. Redémarrage et mesure : démarrage en **48 secondes**, ouverture du classeur de fin de mois sans gel.

## Résultat et suivi

- Performance confirmée avec l'utilisatrice le lendemain matin.
- Constat transmis à la revue de conformité : PC-007 était le seul poste en retard de mises à jour (voir [inventaire](../../02-environnement-ti/inventaire-actifs.csv)). Cause : poste éteint pendant les fenêtres de mise à jour. Action : alerte automatique pour tout poste qui n'a pas reçu de mise à jour depuis 21 jours.
