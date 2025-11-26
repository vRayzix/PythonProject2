import random

x = random.randint(0, 100)

print("J'ai choisi un nombre entre 0 et 100. À vous de le deviner !")

trouve = False
compteur = 0

while not trouve:
    n = int(input("Votre proposition : "))
    compteur += 1

    if n < x:
        print("C'est plus grand !")
    elif n > x:
        print("C'est plus petit !")
    else:
        print("Bravo ! Vous avez trouvé !")
        trouve = True

print("Vous avez trouvé en", compteur, "tentatives.")
