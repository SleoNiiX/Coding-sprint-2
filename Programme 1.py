#On cree une variable qui permet à l'utilisateur de convertir plusieurs nombre en chiffre romain
processus_en_cours = True

while processus_en_cours:
    #On demande à l'utilisateur un entier
    saisie_correct = False

    while saisie_correct == False: #Tant que la saisie n'est pas correct
        entier = int(input("Quel nombre souhaites-tu afficher en chiffre Romain ? "))

        if entier>0 and entier<4000: saisie_correct = True

    #Si  l'utilisateur le souhaite, on sort de la boucle while
    stop = input("Ecrit 'stop' si tu souhaites arreter. ").lower()

    if stop == 'stop': processus_en_cours = False

print("FIN DU PROGRAMME !")