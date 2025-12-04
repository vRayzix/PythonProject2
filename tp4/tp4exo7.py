mon_login = "rt1"
voisin_login = "rt2"
binome = (mon_login, voisin_login)
print(f"L'étudiant {binome[0]} est en binome avec l'étudiant {binome[1]}")

binome = (mon_login, "nouveau_login")

trinome = binome + ("troisieme_login",)
print(trinome)