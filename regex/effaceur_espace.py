"""
Un script effaceur des espaces dans un  fichier
Usage :
=======
    python effaceur_espace.py nom_fichier.txt
    nom_fichier.txt : est le nom du fichier dans lequel on veut effacer les espaces

"""
__authors__ = "Canisius Ronald Phesthus SOVIDE"
__contact__ = "ronald.sovide@gmail.com"
__version__ = "1.0.0"
__copyright__ = ""
__date__ = "22/09/2023"

import re
import sys

fichier = sys.argv[1]

with open(fichier, "r") as filin:
    contenu_fichier = filin.read()
pattern = "\s"
reg = re.compile(pattern)
resultat = reg.sub(" ", contenu_fichier)
with open(fichier, 'w') as filout:
    filout.write(resultat)
