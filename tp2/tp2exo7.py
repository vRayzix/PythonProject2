import random
nb = random.randint(1, 3)
print("Nombre généré :", nb)
if nb < 2:
	print("Pile !")
else:
	print("Face !")
