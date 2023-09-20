import math


def distance_3d(xa=1, ya=1, za=1, xb=0, yb=0, zb=0):
    return math.sqrt(math.pow(xa - xb, 2) + math.pow(ya - yb, 2) + math.pow(za - zb, 2))


print("La distance entre A(0,0,0) et B(1,1,1) est : {}".format(distance_3d()))
