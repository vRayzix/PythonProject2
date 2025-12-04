nom1 = input("Entrer le nom de la première personne : ")
prenom1 = input("Entrer le prénom de la première personne : ")


nom2 = input("Entrer le nom de la deuxième personne : ")
prenom2 = input("Entrer le prénom de la deuxième personne : ")

p1_affiche = prenom1.capitalize() + " " + nom1.upper()
p2_affiche = prenom2.capitalize() + " " + nom2.upper()


personne1 = (nom1.lower(), prenom1.lower(), p1_affiche)
personne2 = (nom2.lower(), prenom2.lower(), p2_affiche)

liste_personnes = [personne1, personne2]
liste_personnes.sort()

print("\nRésultat :")
print(liste_personnes[0][2])
print(liste_personnes[1][2])
