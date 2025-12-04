def taille_chaine(T):
    t = 0
    try:
        while True:
            T[t]
            t += 1
    except IndexError:
        return t


def pourcentage_voyelles(T):
    voyelles = "aeiouyAEIOUY"
    t = taille_chaine(T)
    nb = 0
    for i in range(t):
        if T[i] in voyelles:
            nb += 1
    return (nb / t) * 100 if t > 0 else 0


def premier_wagon(T):
    mot = "wagon"
    t = taille_chaine(T)
    lm = 5

    for i in range(t - lm + 1):
        j = 0
        while j < lm and T[i + j] == mot[j]:
            j += 1
        if j == lm:
            return i

    return -1


def nb_occurrences_wagon(T):
    mot = "wagon"
    t = taille_chaine(T)
    lm = 5
    nb = 0

    for i in range(t - lm + 1):
        j = 0
        while j < lm and T[i + j] == mot[j]:
            j += 1
        if j == lm:
            nb += 1

    return nb

T = input("Entrez une phrase : ")

t = taille_chaine(T)
p = pourcentage_voyelles(T)
pos = premier_wagon(T)
occ = nb_occurrences_wagon(T)

print("\nTaille =", t)
print(f"Pourcentage de voyelles = {p:.2f}%")

if pos != -1:
    print(f"'wagon' trouvé à la position {pos}")
else:
    print("'wagon' n'est pas présent dans la chaîne.")

print(f"Nombre d'occurrences de 'wagon' = {occ}")
