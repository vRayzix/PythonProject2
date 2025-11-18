n = int(input("Entrer un nombre entier : "))
somme = 0
for i in range(n + 1):
    somme += i
print("La somme des entiers de 0 à", n, "est :", somme)