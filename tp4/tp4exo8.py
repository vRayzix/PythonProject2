moi = {"firstname": "Ismail", "name": "Bennis", "promo": 2025, "group": "RT1"}
print(f"votre nom est {moi['name']}, prénom est {moi['firstname']}, promo {moi['promo']}, groupe {moi['group']}")


print("Les clés :", list(moi.keys()))
print("Les valeurs :", list(moi.values()))
print("Les items :", list(moi.items()))

autre = {"firstname": "Jean", "name": "Dupont", "promo": 2025, "group": "RT2"}

groupe_binome = {
    101: moi,
    102: autre
}

print("Les étudiants formants le binôme sont :")
for id_poste, etudiant in groupe_binome.items():
    print(f"Poste {id_poste} : L'étudiant {etudiant['name']} {etudiant['firstname']} du groupe {etudiant['group']}")