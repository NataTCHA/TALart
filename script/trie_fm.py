import pandas as pd

# Charger le fichier CSV contenant la liste des personnages grecs et romains
df = pd.read_csv("personnage_greco_romain.csv")

# Extraire les noms de personnages grecs et romains et leur genre
grecs = dict(zip(df["Grec"], df["Genre"]))
romains = dict(zip(df["Romain"], df["Genre"]))

# Parcourir chaque texte dans la colonne "texte" du fichier concatenation.tsv
df_concat = pd.read_csv("concatenation.tsv", delimiter='\t')
for text in df_concat["texte"]:
    # convertir la variable `text` en une chaîne de caractères
    text = str(text)
    genre_f = False
    genre_m = False
    for element, element_genre in grecs.items():
        # Vérification si le texte contient un nom grec
        if str(element) in text:
            if element_genre == 'F':
                genre_f = True
            elif element_genre == 'M':
                genre_m = True
    if not genre_f or not genre_m:
        for element, element_genre in romains.items():
            # Vérification si le texte contient un nom romain
            if str(element) in text:
                if element_genre == 'F':
                    genre_f = True
                elif element_genre == 'M':
                    genre_m = True
    if genre_f and genre_m:
        # Écriture dans le fichier mixte.txt si le texte contient à la fois un nom de genre masculin et féminin
        with open('mixte.txt', 'a') as f:
            f.write(text + '\n')
    elif genre_f:
        # Écriture dans le fichier f.txt si le texte contient un nom de genre féminin
        with open('f.txt', 'a') as f:
            f.write(text + '\n')
    elif genre_m:
        # Écriture dans le fichier m.txt si le texte contient un nom de genre masculin
        with open('m.txt', 'a') as f:
            f.write(text + '\n')
