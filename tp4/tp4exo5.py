date_str = input("Entrez une date (jjmmaaaa): ")

if len(date_str) != 8:
    print("Format incorrect. Il faut 8 chiffres.")
else:
    jour = int(date_str[0:2])
    mois = int(date_str[2:4])
    annee = int(date_str[4:8])
    
    valide = True
    
    bissextile = (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)
    
    if mois < 1 or mois > 12:
        valide = False
    elif jour < 1:
        valide = False
    else:
  
        if mois in [1, 3, 5, 7, 8, 10, 12]:
            if jour > 31: valide = False
        elif mois in [4, 6, 9, 11]:
            if jour > 30: valide = False
        elif mois == 2:
            if bissextile:
                if jour > 29: valide = False
            else:
                if jour > 28: valide = False
                
    if valide:
        print("Date correcte.")
    else:
        print("Date incorrecte !")