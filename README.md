# Le compte est bon !

Ce programme est un résolveur automatique pour le jeu « Le compte est bon ! »

## Règles du jeu

Le joueur tire au hasard, sans remplacement, 6 plaques portant des numéros parmi un ensemble de 28 plaques ainsi constitué :

1. 20 plaques numérotées de 1 à 10 (2 par nombre)
2.  2 plaques de 25
3. 2 plaques de 50
4. 2 plaques de 75
5. 2 plaques de 100

On tire également au hasard un nombre N entre 100 et 999. Le but du jeu est de trouver une valeur aussi proche que possible de N, en utilisant les nombres inscrits sur les plaques, en respectant les règles suivantes :

1. Chaque plaque doit être utilisée au plus une fois (mais il n'est pas nécessaire d'utiliser toutes les plaques)
2. Les seules opérations autorisées sont les quatre opérations arithmétiques, +, -, * et /, restreintes aux entiers naturels positifs : ainsi, les divisions ne sont autorisées que si leur reste est nul et les nombres négatifs sont proscrits du calcul.

## Fonctionnement du programme

Le programme choisit automatiquement et aléatoirement les numéros des plaques et l'objectif, puis affiche la série d'opérations à effectuer pour avoir le meilleur résultat, la distance entre le résultat et l'objectif, et le temps qu'il lui a fallu pour trouver le résultat.