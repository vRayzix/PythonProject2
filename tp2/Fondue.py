BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbrConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))
fromage_final = fromage * nbrConvives / BASE
eau_final = eau * nbrConvives / BASE
ail_final = ail * nbrConvives / BASE
pain_final = pain * nbrConvives / BASE
print(f"Pour faire une fondue fribourgeoise pour {nbrConvives} personnes, il vous faut :\n - {fromage_final} gr de fromage")
print(f" - {eau_final} dl d'eau")
print(f" - {ail_final} gousse(s) d'ail")
print(f" - {pain_final} gr de pain")