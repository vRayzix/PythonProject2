x = float(input("Entrez un nombre décimal : "))
appartient_I = (
	((x == 2 or x > 2) and x < 3)
	or
	(x > 0 and (x == 1 or x < 1))
	or
	((x == -10 or x > -10) and (x == -2 or x < -2))
)
if appartient_I:
	print("x appartient à I")
else:
	print("x n'appartient pas à I")
