import random


def cal_stat(liste=[1.0, 8.0, 0.0, 6.0, 7.0, 3.0]):
    a = min(liste)
    b = max(liste)
    c = sum(liste)/len(liste)
    return a, b, c


def gen_distrib(debut, fin, n):
    liste = []
    for i in range(n):
        liste.append(random.uniform(debut, fin))
    return liste


for i in range(20):
    # cal_stat(gen_distrib(1,10,10))
    a,b,c = cal_stat(gen_distrib(1, 10, 100))

    print("Liste {} : min = {:.2f} ; max = {:.2f} ; moyenne = {:.2f}".format(i+1,a, b, c))


