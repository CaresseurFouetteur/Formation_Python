# -*-coding:Latin-1 -*

# Demander le nombre
nombre = raw_input("Nombre ?\n")
nombre = int(nombre)

# incr�ment
i = 0

# tant que l'incr�ment est inf�rieur � 10
while i <= 10:
    # calculer et afficher la table
    resultat  = i * nombre
    print(str(nombre) + " x " + str(i) + " = " + str(resultat))
    # incr�menter
    i = i + 1
