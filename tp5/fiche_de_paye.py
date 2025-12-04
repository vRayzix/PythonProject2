heures = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

salaire = 0.0

if heures <= 160:
    salaire = heures * salaire_horaire

else:
    salaire = 160 * salaire_horaire
    heures_restantes = heures - 160

    if heures_restantes <= 40:
        salaire += heures_restantes * salaire_horaire * 1.25

    else:
        salaire += 40 * salaire_horaire * 1.25
        heures_restantes -= 40

        salaire += heures_restantes * salaire_horaire * 1.50

print(f"Le salaire total est de {salaire:.2f} euros.")
