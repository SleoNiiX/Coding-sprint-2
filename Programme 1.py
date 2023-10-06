#On cree une variable qui permet à l'utilisateur de convertir plusieurs nombre en chiffre romain
processus_en_cours = True

while processus_en_cours:
    #On demande à l'utilisateur un entier
    saisie_correct = False

    while saisie_correct == False: #Tant que la saisie n'est pas correct
        entier = int(input("\nQuel nombre souhaites-tu afficher en chiffre Romain ? "))

        if entier>0 and entier<4000: saisie_correct = True

    #On cree un dictionnaire contenant les chiffres romains et leur correspondance en entier
    chiffres_romains = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    chiffre_final = ''

    while entier != 0:
        puissance = 10**(len(str(entier))-1)
        cp = entier//(puissance) #cp = chiffre_puissance

        if cp == 1 or cp == 2 or cp == 3:
            for chiffre in chiffres_romains.keys():
                if chiffres_romains[chiffre] == puissance:
                    chiffre_final += chiffre*cp
        elif cp == 5 or cp == 6 or cp == 7 or cp == 8:
            puissance5 = puissance*5
            difference = (cp*puissance - puissance5)//puissance

            for chiffre in chiffres_romains.keys():
                if chiffres_romains[chiffre] == puissance5:
                    chiffre_final += chiffre
                elif chiffres_romains[chiffre] == puissance:
                    chiffre_final += chiffre*difference
        elif cp == 4:
            ...

        entier -= puissance*cp 
                

    print(chiffre_final)

    #Si  l'utilisateur le souhaite, on sort de la boucle while
    stop = input("\nEcrit 'stop' si tu souhaites arreter. ").lower()

    if stop == 'stop': processus_en_cours = False

print("\nFIN DU PROGRAMME !")