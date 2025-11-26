import time

n = int(input("Veuillez entrer un nombre entier positif: "))

while n >= 0:
    print(n)
    time.sleep(1)
    n -= 1
