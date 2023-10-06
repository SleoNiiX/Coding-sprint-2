# Coding-sprint-2 : Sujet

#### Modalite :
Ce coding sprint, assorti d’un bonus pouvant aller jusqua 0,3
points sur la moyenne de l’examen TP 2, est facultatif.
Si vous souhaitez y participer, vous devez ecrire vos programmes entre
vendredi 6 octobre 2023 a 17h30 et lundi 9 octobre a 8h.

## 1 Ecriture en chiffres romains

Le systeme d’ecriture en chiffres romains utilise les symboles :
I, V, X, L, C, D et M
qui correspondent respectivement aux entiers :
1, 5, 10, 50, 100, 500 et 1000.
Pour ecrire un nombre en chiffres romains on juxtapose les ecritures des
milliers, des centaines, des dizaines et des unites de ce nombre.
Par exemple, l’ecriture de 2794 est la juxtaposition des ecritures de 2000,
de 700, de 90 et de 4.

On applique les regles suivantes :
- Lorsque le multiplicateur de la puissance de 10 est 1, 2 ou 3, on ecrit
autant de fois le symbole correspondant a cette puissance de 10.
Par exemple, 1000 s’ecrit ”M”, 2000 s’ecrit ”MM”, 3000 s’ecrit ”MMM”.
- Lorsque le multiplicateur de la puissance de 10 est 5, 6, 7 ou 8, on
commence par ecrire le symbole correspondant a 5 fois la puissance de
10, puis on ecrit l’ecriture de la difference restante.
Par exemple, 500 s’ecrit ”D”, 600 s’ecrit ”DC” (500+100), 700 s’ecrit
”DCC” (500+200) et 800 s’ecrit ”DCCC” (500+300).
- Lorsque le multiplicateur de la puissance de 10 est 4, on exprime que
le nombre est egal a 5 fois la puissance de 10 de quoi on retranche une
fois la puissance de 10.
Ceci s’ecrit en faisant preceder le symbole correspondant a 5 fois la
puissance de 10 par le symbole correspondant a la puissance de 10.
Par exemple, 4 s’ecrit ”IV” (5-1), 40 s’´ecrit ”XL” (50-10), 400 s’ecrit
”CD” (500-100), et il n’est pas possible d’ecrire 4000 car il n’existe pas
de symbole correspondant a 5000.
- Lorsque le multiplicateur de la puissance de 10 est 9, on exprime que le
nombre est egal a la puissance de 10 superieure de laquelle on retranche
une fois la puissance de 10 du nombre.
Ceci s’ecrit en faisant preceder le symbole correspondant a la puissance
de 10 superieure par le symbole correspondant a la puissance de 10 du
nombre.
Par exemple, 9 s’ecrit ”IX” (10-1), 90 s’ecrit ”XC” (100-10) et 900
s’ecrit ”CM” (1000-100)

De toutes ces regles il resulte que le nombre 2794 donne en exemple
ci-dessus s’ecrit ”MMDCCXCIV” en chiffres romains.
On remarque egalement que 3999 est le plus grand nombre possedant
une ecriture en chiffres romains en appliquant ces regles.

## 2 Programme n° 1

Ecrivez un programme qui demande a l’utilisateur de saisir un entier 
compris entre 1 et 3999 et qui affiche ce nombre en chiffres romains.
Par exemple si l’utilisateur saisit 1234, votre programme devra afficher :
Le nombre 1234 s’ecrit MCCXXXIV en chiffres romains.
Vous redemanderez repetitivement la saisie tant que le nombre saisi n’est
pas dans l’intervalle impose.
Tout ce processus devra etre repete jusqu’a ce que l’utilisateur dise qu’il
souhaite arreter.

## 3 Programme n° 2

Faites de votre conversion d’un entier en chiffres romains une fonction.
La fonction testera si l’entier recu est dans l’intervalle impose ([1, 3999]).
Si c’est le cas elle retournera une chaıne de caracteres correspondant a
l’ecriture en chiffres romains. Si ce n’est pas le cas, elle retournera une chaıne
vide.
Ecrivez un programme qui genere en boucle des entiers aleatoires compris 
entre 0 et 5000 (inclus). La fonction devra etre appelee pour chaque entier
et votre programme devra afficher soit une phrase comme :
Le nombre 768 s’´ecrit DCCLXVIII en chiffres romains.
soit une phrase comme :
Il n’existe pas d’ecriture en chiffres romains pour le nombre 4179.
La boucle devra s’arreter lorsque l’ecriture en chiffres romains du nombre
courant contient exactement une fois le caractere ”M” et exactement deux
fois le caractere ”X” **(1)**.
Remarque : Votre fonction de conversion en chiffres romains ne doit rien
afficher.

**(1)** *Ce n’est pas obligatoire, mais vous pourrez ecrire une fonction qui prend en entree
l’ecriture en chiffres romains et qui retourne un booleen indiquant si cette condition de
continuation de la boucle est verifiee ou non.*
