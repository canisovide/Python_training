import re

# Nom du fichier HTML à traiter
nom_fichier = "fichier_a_dehtmliser.html"


# Fonction pour extraire le texte d'un fichier HTML en utilisant une regex
def extraire_texte_html_avec_regex(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            contenu = fichier.read()
            texte_extrait = re.sub(r'<.*?>', '', contenu)  # Supprime toutes les balises HTML
            return texte_extrait
    except FileNotFoundError:
        print("Le fichier spécifié n'a pas été trouvé.")
        return ""


# Appel de la fonction pour extraire le texte HTML en utilisant une regex
texte_extrait = extraire_texte_html_avec_regex(nom_fichier)

# Affichage du texte extrait
print(texte_extrait)
