minutes_par_jour = 1440
minutes_ecoulees = int(input("Donne le nombre de minutes écoulées depuis le début du mois : "))


jour_du_mois = minutes_ecoulees // minutes_par_jour
minute_reste = minutes_ecoulees % minutes_par_jour

heure = minute_reste // 60


minute = minute_reste % 60

print(f"Date associée : Jour {jour_du_mois}, Heure {heure}, Minute {minute}")
