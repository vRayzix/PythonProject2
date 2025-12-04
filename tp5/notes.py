notes = []
coeffs = []

print("Programme de calcul de moyenne pondérée\n")

for i in range(1, 6):
    saisie = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")

    elements = saisie.split()
    note = float(elements[0])
    coeff = int(elements[1])

    notes.append(note)
    coeffs.append(coeff)

total = 0
coef_total = 0

for n, c in zip(notes, coeffs):
    total += n * c
    coef_total += c

moyenne = total / coef_total

admis = True
if moyenne <= 10:
    admis = False
if min(notes) < 8:
    admis = False

print("\n--- Résultats ---")
print(f"Moyenne générale : {moyenne:.2f}")

if admis:
    print("L'étudiant est ADMIS.")
else:
    print("L'étudiant n'est PAS admis.")
