"""Contrôle mensuel des comptes : orphelins, inactifs, sans MFA, groupes hors matrice.

Usage : python scripts/comptes_inactifs.py [AAAA-MM-JJ]
Compare l'export de l'annuaire (donnees/export-comptes-annuaire.csv) à la
liste RH (donnees/employes.csv). Données fictives.
"""
import csv
import sys
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
JOUR = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date(2026, 10, 15)
SEUIL_INACTIVITE = 45  # jours

GROUPE_ATTENDU = {
    "Direction": "GRP-Direction",
    "Ressources humaines": "GRP-RH",
    "Finance": "GRP-Finance",
    "Ventes": "GRP-Ventes",
    "Administration": "GRP-Administration",
    "Technologies de l'information": "GRP-TI",
}
EXCEPTIONS_APPROUVEES = {("isabelle.roy", "GRP-RH-Paie-Lecture")}
COMPTES_SPECIAUX = {"break-glass-01"}  # surveillés à part (test semestriel)

rh = {e["id"]: e for e in csv.DictReader(open(RACINE / "donnees" / "employes.csv", encoding="utf-8"))}
comptes = list(csv.DictReader(open(RACINE / "donnees" / "export-comptes-annuaire.csv", encoding="utf-8")))

constats = []
for c in comptes:
    if c["active"] != "Oui" or c["compte"] in COMPTES_SPECIAUX:
        continue
    emp = rh.get(c["id_employe"])
    if emp is None:
        constats.append((c["compte"], "ÉLEVÉ", "Compte actif sans employé correspondant aux RH (compte orphelin)"))
        continue
    if c["derniere_connexion"]:
        jours = (JOUR - date.fromisoformat(c["derniere_connexion"])).days
        if jours > SEUIL_INACTIVITE:
            constats.append((c["compte"], "MOYEN", f"Aucune connexion depuis {jours} jours"))
    if c["mfa_inscrit"] != "Oui":
        constats.append((c["compte"], "ÉLEVÉ", "MFA non inscrit"))
    if c["type"] == "Standard":
        attendu = {"GRP-Tous", GROUPE_ATTENDU[emp["departement"]]}
        for g in c["groupes"].split(";"):
            if g not in attendu and (c["compte"], g) not in EXCEPTIONS_APPROUVEES:
                constats.append((c["compte"], "ÉLEVÉ", f"Membre de {g}, hors matrice et sans exception approuvée"))

actifs = sum(c["active"] == "Oui" for c in comptes)
mfa = sum(c["active"] == "Oui" and c["mfa_inscrit"] == "Oui" for c in comptes if c["type"] == "Standard" and c["id_employe"] in rh)
utilisateurs = sum(c["active"] == "Oui" for c in comptes if c["type"] == "Standard" and c["id_employe"] in rh)

print(f"Contrôle des comptes au {JOUR} — {actifs} comptes actifs analysés")
print(f"Couverture MFA des employés : {mfa}/{utilisateurs} ({100 * mfa / utilisateurs:.0f} %)")
print(f"{len(constats)} constat(s) :")
for compte, gravite, texte in sorted(constats, key=lambda x: x[1] != "ÉLEVÉ"):
    print(f"  [{gravite:5}] {compte:22} {texte}")
