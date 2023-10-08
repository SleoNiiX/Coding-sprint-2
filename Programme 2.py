import random as r



def conversion_chiffres_romains(entier):
    #On vérifie que l'entier soit bien compris dans l'intervalle
    if entier > 3999 or entier < 1:
        return ''
    
    else :
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
        return chiffre_final


mauvais_caractere = True

while mauvais_caractere:
    nombre_aleatoire = r.randint(0,5000)
    converti = conversion_chiffres_romains(nombre_aleatoire)
    compteur_M,compteur_X = 0,0

    if converti == '':
        print(f"il n'existe pas d'ecriture en chiffres romains pour le nombre {nombre_aleatoire}")
    else:
        print(f"Le nombre {nombre_aleatoire} s’ ecrit {converti} en chiffres romains.")

        for car in converti:
            if car == 'M': 
                compteur_M += 1
            elif car == 'X': 
                compteur_X += 1
    
    if compteur_M == 1 and compteur_X == 2:
        mauvais_caractere = False

print("\nFIN DU PROGRAMME !")