import os
print("Répertoire courant :", os.getcwd())
import os.path
import datetime

f1 = input("Entrez le nom du premier fichier : ")
f2 = input("Entrez le nom du second fichier : ")

existe_f1 = os.path.isfile(f1)
existe_f2 = os.path.isfile(f2)

if not existe_f1:
    print(f"Le fichier {f1} n'existe pas.")
if not existe_f2:
    print(f"Le fichier {f2} n'existe pas.")

if existe_f1 and existe_f2:

    taille_f1 = os.path.getsize(f1)
    taille_f2 = os.path.getsize(f2)

    print(f"\nTaille de {f1} : {taille_f1} octets")
    print(f"Taille de {f2} : {taille_f2} octets")

    mtime_f1 = os.path.getmtime(f1)
    mtime_f2 = os.path.getmtime(f2)

    date_f1 = datetime.datetime.fromtimestamp(mtime_f1)
    date_f2 = datetime.datetime.fromtimestamp(mtime_f2)

    print(f"\nDate de dernière modification de {f1} : {date_f1}")
    print(f"Date de dernière modification de {f2} : {date_f2}")

    print()
    if mtime_f1 > mtime_f2:
        print(f"Le fichier le plus récent est : {f1}")
    elif mtime_f2 > mtime_f1:
        print(f"Le fichier le plus récent est : {f2}")
    else:
        print("Les deux fichiers ont la même date de modification.")
