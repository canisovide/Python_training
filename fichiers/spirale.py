import math
import matplotlib.pyplot as plt
i = 0
teta = []
rayon = []
while i <= 4 * math.pi:
    teta.append(i)
    i += 0.1

i = 0.5

for j in range(len(teta)):
    rayon.append(i)
    i += 0.1
with open("spirale.dat", "w") as fillin:
    for j in range(len(teta)):
        xa = math.cos(teta[j]) * rayon[j]
        ya = math.sin(teta[j]) * rayon[j]
        fillin.write("{:10.5f}  {:10.5f} \n".format(xa, ya))

x = []
y = []
with open("spirale.dat", "r") as f_in:
    for line in f_in:
        coords = line.split()
        x.append(float(coords[0]))
        y.append(float(coords[1]))


plt.figure(figsize=(8, 8))
mini = min(x + y) * 1.2
maxi = max(x + y) * 1.2
plt.xlim(mini, maxi)
plt.ylim(mini, maxi)
plt.plot(x, y)
plt.savefig("spirale.png")
