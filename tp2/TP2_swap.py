a = input("Entrez la première valeur : ")
b = input("Entrez la deuxième valeur : ")
c = input("Entrez la troisième valeur : ")

print(f"Les valeurs entrées sont : a = {a}, b = {b} et c = {c}")
print("Permutation : a ==> b, b ==> c, c ==> a")

temp = a
a = c
c = b
b = temp

print("Les valeurs permutées sont : a = " + a + ", b = " + b + " et c = " + c)
