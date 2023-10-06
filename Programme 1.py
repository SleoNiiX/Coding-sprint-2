# On cree une variable qui permet à l'utilisateur de convertir plusieurs nombre en chiffre romain
processus_en_cours = True

while processus_en_cours:
    # On demande à l'utilisateur un entier
    saisie_correct = False

    while saisie_correct == False: # Tant que la saisie n'est pas correct
        entier = int(input("\nQuel nombre souhaites-tu afficher en chiffre Romain ? "))

        if entier>0 and entier<4000: saisie_correct = True

    # On cree un dictionnaire contenant les chiffres romains et leur correspondance en entier
    chiffres_romains = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    chiffre_final = ''
    original = entier #Sauvegarde de l'entier pour l'ecrire après modification de celui-ci

    # Boucle qui parcours chaque puissance de 10 de l'entier
    while entier != 0:
        puissance = 10**(len(str(entier))-1) # 10**3 si 1000, 4 chiffres moins 1
        cp = entier//(puissance) # cp = chiffre_puissance
        puissance5 = puissance*5 # 5,50,500

        # Si c'est un multiple de 1,2ou3 
        # Alors ecrit cp fois le symbole correspondant à cette puissance de 10
        if cp == 1 or cp == 2 or cp == 3: 
            for chiffre in chiffres_romains.keys():
                if chiffres_romains[chiffre] == puissance:
                    chiffre_final += chiffre*cp

        # Si c'est un multiple de 5,6,7ou8 
        # Alors on ecrit le symbole correspondant a 5 fois la puissance de 10, puis on  ́ecrit l’ecriture de la diff ́erence restante.
        elif cp == 5 or cp == 6 or cp == 7 or cp == 8: 
            difference = (cp*puissance - puissance5)//puissance

            for chiffre in chiffres_romains.keys():
                if chiffres_romains[chiffre] == puissance5:
                    chiffre_final += chiffre
            for chiffre in chiffres_romains.keys():
                if chiffres_romains[chiffre] == puissance:
                    chiffre_final += chiffre*difference

        # Si c'est un multiple de 4
        # Alors on ecrit en faisant preceder le symbole correspondant a 5 fois la puissance de 10 par le symbole correspondant a la puissance de 10.
        elif cp == 4: 
            for chiffre in chiffres_romains.keys():
                if chiffres_romains[chiffre] == puissance:
                    chiffre_final += chiffre 
                if chiffres_romains[chiffre] == puissance5:
                    chiffre_final += chiffre

        # Si c'est un multiple de 9
        # Alors on ecrit en faisant preceder le symbole correspondant a la puissance de 10 superieure par le symbole correspondant a la puissance de 10 du nombre.
        elif cp == 9: 
            for chiffre in chiffres_romains.keys():
                if chiffres_romains[chiffre] == puissance:
                    chiffre_final += chiffre 
                if chiffres_romains[chiffre] == puissance*10:
                    chiffre_final += chiffre

        # On passe a la puissance de 10 suivante
        entier -= puissance*cp 

    # Affichage du résultat            
    print(f"\n{original} s'ecrit {chiffre_final} en chiffre Romain.")

    # Si  l'utilisateur le souhaite, on sort de la boucle while
    stop = input("\nEcrit 'stop' si tu souhaites arreter. ").lower()
    if stop == 'stop': processus_en_cours = False

print("\nFIN DU PROGRAMME !")