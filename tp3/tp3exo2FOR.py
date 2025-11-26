import time

n = int(input("Veuillez entrer un nombre entier positif: "))

for i in range(n, -1, -1):
    print(i)
    time.sleep(1)
