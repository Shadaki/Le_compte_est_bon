#!/usr/bin/env python3
# 14/03/2020

import random
import time

# définition aléatoire des plaques et de l'objectif
plaquesPossibles = list(range(1, 11)) * 2 + [25, 25, 50, 50, 75, 75, 100, 100]
plaques = random.sample(plaquesPossibles, 28)[:6]
objectif = random.randrange(100, 1000)
plusProche = float("inf")

print("Plaques :", " ".join(map(str, plaques)))
print("Objectif :", objectif, "\n")


def resolution(nb, restants, operations):
    global plusProche, solution
    for nb2 in restants:
        for op in "+-*/":
            restantsTemp = restants[:]
            operationsTemp = operations[:]
            resultat = eval(str(nb) + op + str(nb2))
            if resultat > 0 and resultat % 1 == 0:
                restantsTemp.remove(nb2)
                operationsTemp.append(op + str(nb2))
                if abs(objectif - resultat) < abs(objectif - plusProche):
                    plusProche = int(resultat)
                    solution = operationsTemp[:]
                resolution(resultat, restantsTemp[:], operationsTemp[:])

t1 = time.time()
for n in plaques:
    operations = [str(n)]
    resolution(n, list(set(plaques) - {n}), operations)
t2 = time.time()

n = int(solution[0])
for op in solution[1:]:
    suite = int(eval(str(n) + op))
    print(n, op[0], op[1:], "=", suite)
    n = suite

distance = abs(plusProche - objectif)
if distance > 0:
    print("Solution éloignée de", distance, "de l'objectif.")
else:
    print("Le compte est bon !")
print("\nSolution trouvée en", round(t2 - t1, 2), "s")
