#!/usr/bin/env python3
import sys
import re

# mode d'emploi :
# python3 concordance-2022-v2.py CORPUS MOTIF1 MOTIF2 MOTIF3 MOTIF4 MOTIF5 etc.
# le corpus devra déjà être encodé en utf8

if len(sys.argv) < 3:
    print("ERREUR : manque d'arguments")
    sys.exit()

# ------------------------------------------------
corpus = sys.argv[1]
longueur = 10
MOTIFS = sys.argv[2:]


# -----------------------------------------
# ouverture du corpus
with open(corpus, "r", encoding="utf-8") as f:
    fichier = f.read()

# préparation du fichier de sortie au format html contenant un tableau intégrant la concordance
with open("concordance.html", "w", encoding="utf-8") as output:
    output.write("<html>\n")
    output.write("<head>\n")
    output.write("<meta charset=\"utf-8\">\n")
    output.write("</head>\n")
    output.write("<body>\n")
    output.write(f"<p>Voici la concordance de : {' '.join(MOTIFS)} dans le fichier {corpus} et de longueur {longueur}...</p>\n")

    output.write("<table align=\"center\" border=\"2\" bordercolor=\"pink\">\n")
    output.write("<tr><th>N°</th><th align=\"right\">Contexte gauche</th><th align=\"center\">Pole</th><th align=\"left\">Contexte droit</th></tr>")

    # supprimer les retours à la ligne
    fichier = fichier.replace("\n", " ")
    # parcours de la chaine complete à la recherche du pôle
    # opérateur global important 'g'
    compteurcontexte = 0

    recherche = "\\b|\\b".join(MOTIFS)
    # print("<", recherche, ">")

    for match in re.finditer(rf"\b({recherche})\b", fichier):
        compteurcontexte += 1
        # compte les mots à droite et à gauche du pôle
        contextegauche = " ".join(match.string[:match.start()].split()[-(longueur+1):])
        contextedroit = " ".join(match.string[match.end():].split()[:longueur+1])
        output.write(f"<tr><td>{compteurcontexte}</td><td align=\"right\">{contextegauche}</td><td align=\"center\">{match.group()}</td><td align=\"left\">{contextedroit}</td></tr>\n")

    output.write("</table>\n")
    output.write("</body>\n")
    output.write("</html>\n")
