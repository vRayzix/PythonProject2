debut = int(input("Donnez l’heure de début de la location (un entier) : "))
fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

if debut < 0 or debut > 24 or fin < 0 or fin > 24:
    print("Les heures doivent être comprises entre 0 et 24 !")
elif debut == fin:
    print("Attention ! l’heure de fin est identique à l’heure de début.")
elif debut > fin:
    print("Attention ! le début de la location est après la fin ...")
else:
    h1 = 0
    h2 = 0
    for h in range(debut, fin):
        if (0 <= h < 7) or (17 <= h < 24):
            h1 += 1
        else:
            h2 += 1

    total = h1 * 1.0 + h2 * 2.0

    print("Vous avez loué votre vélo pendant")
    if h1 > 0:
        print(h1, "heure(s) au tarif horaire de 1.0 euro(s)")
    if h2 > 0:
        print(h2, "heure(s) au tarif horaire de 2.0 euro(s)")
    print("Le montant total à payer est de", str(total) + " euro(s).")
