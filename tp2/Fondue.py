BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))
fromage_final = fromage * nbConvives / BASE
eau_final = eau * nbConvives / BASE
ail_final = ail * nbConvives / BASE
pain_final = pain * nbConvives / BASE
print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {fromage_final} gr de fromage")
print(f"- {eau_final} dl d'eau")
print(f"- {ail_final} gousse(s) d'ail")
print(f"- {pain_final} gr de pain")