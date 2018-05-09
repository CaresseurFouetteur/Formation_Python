from random import choice

#une liste de questions/r�ponses
# chaque question est un dico {"question":"laquestion", "reponses":["rep1","rep2","rep3"],"bonneReponse":1}
# une liste de tous les dicos questions
# on va "hardcoder" les questions
questionQuestion1 = "Actuellement, combien d'esp�ces de fourmis peut-on trouver en France ?"
reponseQuestion1 = ["57","216","331","1540"]
question1 = {"question":questionQuestion1,"reponses":reponseQuestion1,"bonne":2}

questionQuestion2 = "Le cloporte fait partie des..."
reponseQuestion2 = ["Molusques","Arachnides","Insectes","Crustac�s"]
question2 = {"question":questionQuestion2,"reponses":reponseQuestion2,"bonne":4}

questionQuestion3 = "Que mange la baleine bleue ?"
reponseQuestion3 = ["Du Krill","Du Skill","Des bananes","Du poisson"]
question3 = {"question":questionQuestion3,"reponses":reponseQuestion3,"bonne":1}

questionQuestion4 = "Quelle est la couleur de Darth Maul ?"
reponseQuestion4 = ["Rouge et noir","Noire tatou�e de rouge","Rouge tatou�e de noir","Blanche tatou�e de rouge et de noir"]
question4 = {"question":questionQuestion4,"reponses":reponseQuestion4,"bonne":3}

questions = [question1,question2,question3,question4]

# initialiser le score � 0
score  = 0
# initialiser le nombre de questions pos�es � 0
questionsPosees = 0

# savoir si on continue � jouer
continuer = True

# tant que on continue a jouer
while continuer:
    #le programme pose une question
    # choisir une question au hasard
    question = choice(questions)
    # pose la question
    print(question["question"])
    #propose les r�ponses
    for i,reponse in enumerate(question["reponses"]):
        print(str(i+1) + " - " + reponse)
    reponseJoueur = raw_input("Ta r�ponse : ")
    # le joueur choisit une r�ponse
    # si il a bon, il gagne un point
    if int(reponseJoueur) == question["bonne"]:
        score = score + 1
        print("Bravo !")
    else:
        print("Gros nul !")
    # incr�menter le nombre de questions pos�es
    questionsPosees = questionsPosees + 1
    # demander si le joueur veut continuer
    continuerJoueur = raw_input("Veux-tu continuer (O/N) ?\n")
    # si il veut pas continuer, on met la var sur False
    continuer = continuerJoueur in "Oo"

#si il arrete de jouer : on donne un pourcentage de r�ussite
resultat = float(score) / float(questionsPosees) * 100.0

print("Ton score est de " + str(resultat) + "%")


