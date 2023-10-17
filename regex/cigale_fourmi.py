import re

with open("cigale_fourmi.txt", "r") as fichier:
    contenu = fichier.read()
contenu = contenu.strip()

regex = re.compile(r" {2,}", re.IGNORECASE)
#
#
texte_corrigé = regex.sub(" ", contenu)
#
#
with open("cigale_fourmi_propre.txt", "w") as filout :
    filout.write(texte_corrigé)

