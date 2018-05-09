from random import choice

# mode deboggage
is_debug = True;
def debug(message):
    if is_debug:
        print("DEBUG::: " + str(message))




# liste de mots
les_mots = ["Shawarma","Falafel","Burritos","Waterzooie"]
continuer = True

# tant que on continue � jouer
while continuer:
    # DEBUG
    debug("debut du cycle de jeu")
        
    # initialisation :
    # on met le score � 10
    score = 10
    # choisir un mot au hasard
    le_mot = choice(les_mots)
    # le convertir en majuscules
    le_mot = le_mot.upper()
    # liste des lettres trouv�es
    les_trouvailles = ""
    # liste des lettres fausses demand�es
    les_erreurs = ""
    # liste des lettres demand�es
    les_lettres = ""

    # DEBUG
    debug(le_mot)

    gagne = False
    perdu = False

    # tant que il a pas gagn� ou il a plus de 0
    while not gagne and not perdu:

        # DEBUG
        debug("debut du cycle choix de mot")
        debug(score)

        # affichage sympa
        print("Nombre d'essais restant : " + str(score))
        print("Lettres d�j� demand�es : " + les_lettres)
        
        # afficher le mot avec des tirets pour toutes les lettres pas encotre trouv�es
        affiche = ""
        for caractere in le_mot:
            if caractere in les_lettres:
                affiche = affiche + caractere
            else:
                affiche = affiche + "-"
        print("Voici le mot � trouver : " + affiche)

        # si toutes les lettres sont trouv�es
        if not ("-" in affiche):  
            # gagn�
            gagne = True
            break
        
        # demande une lettre
        lettre_joueur = raw_input("Choisis une lettre !\n")
        lettre_joueur = lettre_joueur.upper()
        # utilsateur choisit une lettre

        # si il en demande plusieurs ce gros con
        if len(lettre_joueur) > 1:
            print("Une seule, gros con !")
            continue

        # si il en demande aucune ce d�bile
        if len(lettre_joueur) == 0:
            print("On t'a demand� une lettre, abrutti!")
            continue

        # si la lettre a d�j� �t� demand�e
        if lettre_joueur in les_lettres:
            print("Esp�ce de gros con, tu as d�j� demand� cette lettre !")
            continue

        # ajouter � la liste des lettres demand�es
        les_lettres = les_lettres + lettre_joueur
        # trier la liste
        les_lettres = sorted(les_lettres)
        les_lettres = ''.join(les_lettres)
        
        # si elle est dans le mot
        if lettre_joueur in le_mot:
            # on dit bravo
            print("Youhou !")
        # sinon
        else:
            # on diminue le score de 1
            score = score - 1
            debug(score)
            # si le score est � 0
            if score == 0:
                # perdu
                perdu = True

    # si gagn�
    if gagne:
        # bravo
        print("Bravo !")
    # sinon
    else:
        # gros nul
        print("Gros naze!")

    # continuer ?
    reponse = raw_input("Veux tu continuer � jouer ? [O/N]\n")
    if reponse in "Nn":
        continuer = False
        
# au revoir
print("Bye bye !")
