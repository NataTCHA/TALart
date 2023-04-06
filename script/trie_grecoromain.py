import pandas as pd

# Charger le fichier CSV contenant la liste des personnages grecs et romains
df = pd.read_csv("personnage_greco_romain.csv")

# Extraire les noms de personnages grecs et romains
grecs = list(df["Grec"])
romains = list(df["Romain"])

# Parcourir chaque texte dans la colonne "texte" du fichier concaténation.tsv
df_concat = pd.read_csv("concatenation.tsv", delimiter='\t')
for text in df_concat["texte"]:
    # convert the `text` variable to a string
    text = str(text)
    for element in grecs:
        element=str(element)


        # Vérification si le texte contient un nom grec ou romain
        if element in text:
            # Écriture dans le fichier grec.txt
            with open('grec.txt', 'a') as f:
                f.write(text + '\n')
                break
    for element in romains:
        element=str(element)
        # Vérification si le texte contient un nom grec ou romain
        if element in text:
            # Écriture dans le fichier romain.txt
            with open('romain.txt', 'a') as f:
                f.write(text + '\n')
                break
