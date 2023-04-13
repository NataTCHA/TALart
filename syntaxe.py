import spacy
from collections import Counter
from prettytable import PrettyTable
from termcolor import colored

# Charger le modèle de langue français de spaCy
nlp = spacy.load("fr_core_news_sm")

# Ouvrir le fichier texte en lecture
with open("T.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Traiter le texte avec spaCy
doc = nlp(text)

# Initialiser un compteur pour les structures syntaxiques
counter = Counter()

# Parcourir les tokens du document
for i, token in enumerate(doc):

    # Si le token est un nom commun ou un adjectif
    if token.pos_ == "ADJ":
        tokencible=token.text
        # Parcourir les tokens autour du token courant
        for j in range(i-3, i+4):
            if j != i and j >= 0 and j < len(doc) and not doc[j].is_space:
                # Construire la structure syntaxique autour du token
                context = " ".join([tok.pos_ for tok in doc[j:i]] + ["*" + token.pos_.upper() + "*"] + [tok.pos_ for tok in doc[i+1:j+1]])
                # Ajouter la structure syntaxique au compteur
                counter[context] += 1

# Afficher les résultats dans un tableau avec PrettyTable
table = PrettyTable(["Structure syntaxique", "Fréquence"])
for context, freq in counter.most_common(20):
    context = context.replace("SPACE", "").replace(" ", " | ")
    token_cible = "*" + tokencible.upper() + "*"
    context = context.replace(token_cible, colored(token_cible, 'green'))
    table.add_row([context, freq])
table.align = "l"
table.sortby = "Fréquence"
table.reversesort = True
print(table)

# Sélectionner une structure syntaxique et afficher ses tokens
selected_context = input("Entrez une structure syntaxique pour afficher ses tokens : ")
for i, token in enumerate(doc):
    if token.pos_ == "ADJ":
        for j in range(i-3, i+4):
            if j != i and j >= 0 and j < len(doc) and not doc[j].is_space:
                context = " ".join([tok.pos_ for tok in doc[j:i]] + ["*" + token.pos_.upper() + "*"] + [tok.pos_ for tok in doc[i+1:j+1]])
                
                if context == selected_context:
                    print("Tokens correspondants :")
                    print([tok.text for tok in doc[j:i]] + [token.text.strip()] + [tok.text for tok in doc[i+1:j+1]])
                    break
