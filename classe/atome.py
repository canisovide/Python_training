"""
Ce code est un code concernant un exercice sur la POO
Il est question de créer une classe nommé Atome.
Ce code sert à représenter un atome.
Voici les spécificité de la classe:
    * Attributs :
        - x,y,z
    * Methodes :


"""
__authors__ = "Canisius Ronald Phesthus SOVIDE"
__contact__ = "ronald.sovide@gmail.com"
__version__ = "1.0.0"
__copyright__ = ""
__date__ = "27/09/2023"

import math


class Atome:
    """
    Ceci est la classe Atome
    """

    def __init__(self, nom="Oxygène", symbole="O", masse=2.65634e-26, x=1.0, y=1.0, z=1.0):
        """Initialisation d'un objet.

            Définition des attributs avec des valeurs par défaut.
        """
        self.x = x
        self.y = y
        self.z = z
        self.masse = masse
        self.nom = nom
        self.symbole = symbole

    def calcul_distance(self, x_other, y_other, z_other):
        """Calcul la distance exacte entre deux atomes"""

        return math.sqrt(
            math.pow(x_other - self.x, 2) +
            math.pow(y_other - self.y, 2) +
            math.pow(z_other - self.z, 2)
        )

    def calcul_masse(self):
        """Calcul de la masse du noyau d'un atome"""
        return "La formule n'est pas disponible monsieur"

    def __str__(self):
        return "Cet atome s'appelle {} son symbole est {} sa masse {} Kg".format(
            self.nom,self.symbole, self.masse
        )


if __name__ == "__main__":
    calcium = Atome(x=23, y=2, z=0)
    hydrogene = Atome(x=2, y=3, z=5)
    distance = calcium.calcul_distance(hydrogene.x, hydrogene.y, hydrogene.z)
    print("La distance entre les deux atomes est de : {}".format(distance))

    atome = Atome()
    print(atome)
