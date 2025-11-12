jour = int(input("Donne le jour :"))
heure = int(input("Donne l'heure :"))
minute = int(input("Donne les minutes :"))
minute = minute + jour * 1440
minute = minute + heure * 60
print(f"il y a {minute} mins")