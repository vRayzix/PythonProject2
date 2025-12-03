nombre_etudiants = int(input("Donnez le nombre d'etudiants: "))
notes = []
somme = 0.0

for i in range(nombre_etudiants):
    note = float(input(f"Note etudiant {i} : "))
    while note < 0 or note > 20:
        print("Note invalide (0-20).")
        note = float(input(f"Note etudiant {i} : "))
    notes.append(note)
    somme += note

moyenne = somme / nombre_etudiants
print(f"Moyenne de classe: {moyenne:.2f}")

print("Numéro de l'Etudiant | note | ecart a la moyenne")
for i in range(len(notes)):
    ecart = notes[i] - moyenne
    print(f"{i} | {notes[i]} | {ecart:.2f}")