import math

import numpy as np
from matplotlib import pyplot as plt


def distance_2d(xa=1, ya=1, xb=0, yb=0):
    return math.sqrt(math.pow(xa - xb, 2) + math.pow(ya - yb, 2))


def calc_distance2ori(liste_x=None, liste_y=None):
    if liste_y is None:
        liste_y = [3, 2, 1]
    if liste_x is None:
        liste_x = [1, 2, 3]
    liste_dist = []
    for i in range(len(liste_x)):
        liste_dist.append(distance_2d(0, 0, liste_x[i], liste_y[i]))
    return liste_dist


liste_x = np.linspace(0, 2 * np.pi, 200)
liste_y = np.sin(liste_x)
with open('sin2ori.dat', "w") as fillout:
    for i in range(len(liste_x)):
        fillout.write("{:10.5f}  {:10.5f} \n".format(liste_x[i], liste_y[i]))

x = []
y = []
with open("sin2ori.dat", "r") as f_in:
    for line in f_in:
        coords = line.split()
        x.append(float(coords[0]))
        y.append(float(coords[1]))
plt.figure(figsize=(8, 8))
fig, ax = plt.subplots()
ax.plot(x, y)
plt.xlabel("x")
plt.ylabel(" Distance de sin (x)à l' origine ")
plt.savefig(" sin2ori.png")
