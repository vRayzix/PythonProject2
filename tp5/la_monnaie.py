somme = int(input("Entrez une somme en euros : "))

billets100 = somme // 100
reste = somme % 100

billets50 = reste // 50
reste = reste % 50

billets10 = reste // 10
reste = reste % 10

piece2 = reste // 2
reste = reste % 2

piece1 = reste // 1
reste = reste % 1

print(f"{somme} euros, c’est donc {billets100} billets de 100, {billets50} de 50, "
      f"{billets10} de 10, {piece2} pièces de 2 et {piece1} pièce de 1.")
