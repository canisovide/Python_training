import os
import sys

if len(sys.argv) != 2:
    sys.exit(" ERREUR : il faut exactement un argument .")

nom_fichier = sys.argv[1]
if os.path.exists(nom_fichier):
    print(" le fichier est présent ")
else:
    sys.exit(" le fichier est absent ")
with open(nom_fichier, "r") as f_in:
    tail = len(f_in.readlines())
print("{} contient {} lignes .".format(nom_fichier, tail))
