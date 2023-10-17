"""
Ce fichier contient le programme du dehtmliseur mais
avec le package BeautifulSoup de python
"""
from bs4 import BeautifulSoup

# Nom du fichier HTML à traiter
nom_fichier = "fichier_a_dehtmliser.html"


# Fonction pour extraire le texte d'un fichier HTML
def extraire_texte_html(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            contenu = fichier.read()
            soup = BeautifulSoup(contenu, "html.parser")
            texte = soup.get_text()
            return texte
    except FileNotFoundError:
        print("Le fichier spécifié n'a pas été trouvé.")
        return ""


# Appel de la fonction pour extraire le texte HTML
texte_extrait = extraire_texte_html(nom_fichier)

# Affichage du texte extrait
print(texte_extrait)
