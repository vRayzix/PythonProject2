
nb = int(input("Entrez un nombre entier: "))
if nb > 0:
	signe = "positif"
elif nb < 0:
	signe = "négatif"
else:
	signe = "zéro"
if nb % 2 == 0:
	parite = "pair"
else:
	parite = "impair"
if nb == 0:
	print("Le nombre est zéro (et il est pair)")
else:
	print(f"Le nombre est {signe} et {parite}")
