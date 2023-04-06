#!/usr/bin/env python3
import sys
import re
from termcolor import colored
from prettytable import PrettyTable

if len(sys.argv) < 3:
    print("ERREUR : manque d'arguments")
    sys.exit(1)

# Récupération des arguments
corpus = sys.argv[1]
longueur = 10
motifs = sys.argv[2:]

# Ouverture du corpus
with open(corpus, "r", encoding="utf-8") as input_file:
    fichier = input_file.read()

# Préparation de la concordance
concordance = []
compteurcontexte = 0
for motif in motifs:
    recherche = r"\b{}\b".format(motif)
    for match in re.finditer(recherche, fichier):
        compteurcontexte += 1
        # Comptage des mots à gauche et à droite du pôle
        contextegauche = " ".join(fichier[:match.start()].split()[-longueur:])
        contextedroit = " ".join(fichier[match.end():].split()[:longueur])
        pole = colored(match.group(), 'green', attrs=['bold'])  # Ajout de couleur au motif
        concordance.append((compteurcontexte, contextegauche, pole, contextedroit))

# Création du tableau de concordance
table = PrettyTable()
table.field_names = ["N°", "Contexte gauche", "Pôle", "Contexte droit"]
for num, cg, p, cd in concordance:
    table.add_row([num, cg, p, cd])

# Affichage de la concordance sous forme de tableau
print("Voici la concordance de : {} dans le fichier {} et de longueur {} ...\n".format(" ".join(motifs), corpus, longueur))
print(table)
