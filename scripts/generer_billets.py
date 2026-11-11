"""Génère un registre fictif de billets de soutien pour NovaBureau.

Données entièrement fictives. La graine aléatoire est fixe pour que le
registre soit reproductible : python scripts/generer_billets.py
"""
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
random.seed(2026)

# (catégorie, priorité par défaut, délai cible de résolution en heures, poids)
CATEGORIES = [
    ("Réinitialisation de mot de passe", "P3", 0.5, 22),
    ("Compte verrouillé", "P3", 0.5, 10),
    ("Installation de logiciel", "P4", 8, 14),
    ("Accès à un dossier partagé", "P3", 8, 12),
    ("Assistance VPN", "P3", 4, 11),
    ("Remplacement de matériel", "P4", 16, 6),
    ("Courriel suspect", "P2", 1, 9),
    ("Impression", "P3", 4, 8),
    ("Lenteur du poste", "P3", 8, 6),
    ("Stockage partagé indisponible", "P1", 2, 2),
]
PRISE_EN_CHARGE_H = {"P1": 0.25, "P2": 1, "P3": 4, "P4": 8}

employes = list(csv.DictReader(open(RACINE / "donnees" / "employes.csv", encoding="utf-8")))
techs = ["Barbara Saroukou", "Thomas Caron"]

debut = datetime(2026, 7, 1, 8, 0)
lignes = []
for i in range(1, 121):
    cat, prio, cible_h, _ = random.choices(CATEGORIES, weights=[c[3] for c in CATEGORIES])[0]
    jour = debut + timedelta(days=random.randint(0, 91))
    while jour.weekday() >= 5:
        jour += timedelta(days=1)
    ouverture = jour.replace(hour=random.randint(8, 16), minute=random.choice([0, 10, 20, 30, 40, 50]))

    # Cible de prise en charge = la plus courte entre la matrice de priorité et le catalogue.
    cible_pec = min(PRISE_EN_CHARGE_H[prio], cible_h)
    # Délai de résolution total : la plupart dans la cible, quelques dépassements.
    res_h = cible_h * random.uniform(0.3, 0.95) if random.random() < 0.9 else cible_h * random.uniform(1.1, 2.5)
    # Délai de prise en charge : une fraction du délai total.
    pec_h = min(res_h * random.uniform(0.1, 0.5), cible_pec * 0.95) if random.random() < 0.94 else cible_pec * random.uniform(1.1, 1.8)
    res_h = max(res_h, pec_h + 0.05)

    emp = random.choice([e for e in employes if e["departement"] != "Technologies de l'information"])
    lignes.append({
        "billet": f"REQ-{i:03d}",
        "date_ouverture": ouverture.strftime("%Y-%m-%d %H:%M"),
        "demandeur": emp["id"],
        "departement": emp["departement"],
        "categorie": cat,
        "priorite": prio,
        "technicien": random.choices(techs, weights=[7, 3])[0],
        "prise_en_charge_min": round(pec_h * 60),
        "resolution_min": round(res_h * 60),
        "cible_prise_en_charge_min": round(cible_pec * 60),
        "cible_resolution_min": round(cible_h * 60),
        "resolu_premier_contact": "Oui" if cat in {"Réinitialisation de mot de passe", "Compte verrouillé", "Impression"} and random.random() < 0.85 else ("Oui" if random.random() < 0.35 else "Non"),
        "satisfaction_1a5": random.choices([5, 4, 3, 2], weights=[55, 32, 10, 3])[0],
    })

lignes.sort(key=lambda r: r["date_ouverture"])
with open(RACINE / "donnees" / "registre-billets.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(lignes[0].keys()))
    w.writeheader()
    w.writerows(lignes)
print(f"{len(lignes)} billets générés dans donnees/registre-billets.csv")
