Infa10 = 0
Supa10EtInf15 = 0
SupOuEgala15 = 0
for i in range(10):
    nombre = float(input(f"Entrez un nombre {i+1} compris entre 0 et 20 :"))
    while nombre < 0 or nombre > 20:
        print(f"Réessayez)
        nombre = float(input(f"Entrez la valeur "))
