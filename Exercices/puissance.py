# -*-coding:Latin-1 -*

# Demander le nombre
nombre = raw_input("Nombre ?")
nombre = int(nombre)
# Demander la puissance
puissance = raw_input("Puissance ?")
puissance = int(puissance)

resultat = 1 # une puissance 0 est �gale � un, donc le r�sultat minimum est 1

i = 0 #incr�ment pour compter le nombre de fois qu'on a multipli�

# multiplier le r�sultat par le nombre, autant de fois que la puissance
# tant que on n'a pas fait autant de multiplications que puissance
while i < puissance:
    resultat = resultat * nombre # la multiplication
    i = i + 1 # incr�mentation 

# afficher le r�sultat
print("La puissance " + str(puissance) + " de " + str(nombre) + " est " + str(resultat))
