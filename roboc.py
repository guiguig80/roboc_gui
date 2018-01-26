# -*-coding:Latin-1 -*

"""Ce fichier contient le code principal du jeu.
Ex�cutez-le avec Python pour lancer le jeu.
"""

import os

from carte import Carte

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Cr�ation d'une carte, � compl�ter

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

# Si il y a une partie sauvegard�e, on l'affiche, � compl�ter

# ... Compl�tez le programme ...
