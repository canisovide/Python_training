class Rectangle:
    """Ceci est la classe Rectangle."""

    def __init__(self, longueur=0.0, largeur=0.0, couleur="blanc"):
        """Initialisation d'un objet.

        Définition des attributs avec des valeurs par défaut.
        """
        self.longueur = longueur
        self.largeur = largeur
        self.couleur = couleur

    def calcule_surface(self):
        """Méthode qui calcule la surface."""
        return self.longueur * self.largeur

    def change_carre(self, cote):
        """Méthode qui transforme un rectangle en carré."""
        self.longueur = cote
        self.largeur = cote

    def calcul_perimetre(self):
        """Methode qui calcule le périmetre du rectangle"""
        return (self.longueur + self.largeur)*2


if __name__ == "__main__":
    # Insérez ici la suite de votre programme Python
    # qui va utiliser la classe Rectangle.
    rectangle1 = Rectangle()
    print("Longueur : {}".format(rectangle1.longueur))
    print("Largeur : {}\nCouleur : {}".format(rectangle1.largeur, rectangle1.couleur))
    print("L'aire de la surface : {}".format(rectangle1.calcule_surface()))
    rectangle1.change_carre(30)

    print("L'aire de la surface du carré est : {}".format(rectangle1.calcule_surface()))

    rectangle2 = Rectangle(longueur=20, largeur=10)
    print("Le périmetre du nouveau rectangle est de : {} m".format(rectangle2.calcul_perimetre()))