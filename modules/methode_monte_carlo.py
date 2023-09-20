import math
import random


N = [100, 1000, 10000]
for j in N:
    n = 0
    for i in range(j):
        xa = random.uniform(-1, 1)
        ya = random.uniform(-1, 1)
        dist = math.sqrt(math.pow(xa, 2) + math.pow(ya, 2))
        if dist < 1:
            n += 1
    pi = 4 * (n / j)
    print("Pour {} itérations, la valeur de pi obtenue est : {}".format(j,pi))
    if pi < math.pi:
        print("pi est inférieur à math.pi", end="")
    else:
        print("pi est supérieur à math.pi", end="")
    print(" l'écart est de {:.10f}".format(math.fabs(math.pi - pi)))
