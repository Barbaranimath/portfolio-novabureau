"""Calcule les indicateurs de performance du centre de soutien NovaBureau.

Usage : python scripts/indicateurs.py
Produit 03-soutien-utilisateurs/indicateurs-T3-2026.md à partir de
donnees/registre-billets.csv (données fictives).
"""
import csv
from collections import Counter
from pathlib import Path
from statistics import median

RACINE = Path(__file__).resolve().parent.parent
billets = list(csv.DictReader(open(RACINE / "donnees" / "registre-billets.csv", encoding="utf-8")))
n = len(billets)


def pct(x, total):
    return f"{100 * x / total:.0f} %" if total else "s.o."


pec_ok = sum(int(b["prise_en_charge_min"]) <= int(b["cible_prise_en_charge_min"]) for b in billets)
res_ok = sum(int(b["resolution_min"]) <= int(b["cible_resolution_min"]) for b in billets)
fcr = sum(b["resolu_premier_contact"] == "Oui" for b in billets)
csat = sum(int(b["satisfaction_1a5"]) for b in billets) / n
csat_pos = sum(int(b["satisfaction_1a5"]) >= 4 for b in billets)
med_res = median(int(b["resolution_min"]) for b in billets)

out = [
    "# Indicateurs du centre de soutien — T3 2026 (1er juillet au 30 septembre)",
    "",
    "> Généré automatiquement par `scripts/indicateurs.py` à partir de `donnees/registre-billets.csv`. Données fictives.",
    "",
    "## Synthèse",
    "",
    "| Indicateur | Valeur | Cible |",
    "|---|---|---|",
    f"| Billets traités | {n} | — |",
    f"| Prise en charge dans le délai cible | {pct(pec_ok, n)} | ≥ 90 % |",
    f"| Résolution dans le délai cible (SLA) | {pct(res_ok, n)} | ≥ 85 % |",
    f"| Résolution au premier contact | {pct(fcr, n)} | ≥ 50 % |",
    f"| Satisfaction moyenne | {f'{csat:.1f}'.replace('.', ',')} / 5 | ≥ 4,2 |",
    f"| Utilisateurs satisfaits (4 ou 5) | {pct(csat_pos, n)} | ≥ 85 % |",
    f"| Délai médian de résolution | {med_res:.0f} min | — |",
    "",
    "## Répartition par catégorie",
    "",
    "| Catégorie | Billets | Part | SLA respecté |",
    "|---|---|---|---|",
]
for cat, c in Counter(b["categorie"] for b in billets).most_common():
    sous = [b for b in billets if b["categorie"] == cat]
    ok = sum(int(b["resolution_min"]) <= int(b["cible_resolution_min"]) for b in sous)
    out.append(f"| {cat} | {c} | {pct(c, n)} | {pct(ok, c)} |")

out += ["", "## Répartition par priorité", "", "| Priorité | Billets | Prise en charge dans la cible |", "|---|---|---|"]
for p in ["P1", "P2", "P3", "P4"]:
    sous = [b for b in billets if b["priorite"] == p]
    ok = sum(int(b["prise_en_charge_min"]) <= int(b["cible_prise_en_charge_min"]) for b in sous)
    out.append(f"| {p} | {len(sous)} | {pct(ok, len(sous))} |")

out += ["", "## Répartition par département", "", "| Département | Billets |", "|---|---|"]
for d, c in Counter(b["departement"] for b in billets).most_common():
    out.append(f"| {d} | {c} |")

top = Counter(b["categorie"] for b in billets).most_common(2)
out += [
    "",
    "## Lecture et actions",
    "",
    f"- Les deux catégories les plus fréquentes ({top[0][0].lower()} et {top[1][0].lower()}) représentent "
    f"{pct(top[0][1] + top[1][1], n)} du volume : un portail de réinitialisation libre-service réduirait directement la charge.",
    "- Les dépassements de SLA sont analysés dans la revue mensuelle; chaque dépassement P1/P2 fait l'objet d'un rapport après incident.",
    "- Les guides de la base de connaissances (dossier 07) ciblent en priorité les catégories les plus fréquentes.",
    "",
]
dest = RACINE / "03-soutien-utilisateurs" / "indicateurs-T3-2026.md"
dest.write_text("\n".join(out), encoding="utf-8")
print("\n".join(out[6:16]))
