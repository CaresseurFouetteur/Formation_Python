unDicoVide = {}
unDico = {"Nom":"Duduf", "Pr�nom":"Nicolas","Age":25 }

unDico["Pr�nom"] = "Bertrand"

reponse = "Bonjour {0} {1}, qui a {2} ans"
reponse = reponse.format(unDico["Pr�nom"],unDico["Nom"],str(unDico["Age"]))
print(reponse)

