def main():
    valeurs = []


    while len(valeurs) < 10:
        try:
            valeur = float(input(f"Entrez la valeur #{len(valeurs) + 1} (entre 0 et 20) : "))
            if 0 <= valeur <= 20:
                valeurs.append(valeur)
            else:
                print("Valeur non valide, veuillez entrer un nombre entre 0 et 20.")
        except ValueError:
            print("Entrée non valide, veuillez entrer un nombre réel.")

    compteur_inferieur_10 = sum(1 for v in valeurs if v < 10)
    compteur_10_a_15 = sum(1 for v in valeurs if 10 <= v < 15)
    compteur_superieur_15 = sum(1 for v in valeurs if v >= 15)

    print(f"Nombre de valeurs strictement inférieures à 10 : {compteur_inferieur_10}")
    print(f"Nombre de valeurs supérieures ou égales à 10 et inférieures strictement à 15 : {compteur_10_a_15}")
    print(f"Nombre de valeurs supérieures ou égales à 15 : {compteur_superieur_15}")

if __name__ == "__main__":
    main()
