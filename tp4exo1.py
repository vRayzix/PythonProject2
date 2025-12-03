nb = float(input("Vous cherchez la table de multiplication de quel nombre ? "))
for i in range(10):
    res = round(nb * i, 1) 
    print(f"{nb}*{i}={res}")