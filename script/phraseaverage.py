import pandas as pd

def dictionnaire():
    # Importer les données du fichier tsv
    df = pd.read_csv("concatenation.tsv", delimiter="\t")

    # Initialiser les dictionnaires pour stocker les données
    dico_occurence = {}
    dico_longueur_moyenne_phrases = {}

    # Parcourir chaque ligne du dataframe
    for _, row in df.iterrows():
        balise = str(row['balise'])
        texte = str(row['texte'])
        occurrence = int(row['occurrence'])

        # Calculer la longueur moyenne des phrases pour chaque balise
        longueurs_phrases = [len(phrase.split()) for phrase in texte.split(".")]
        longueur_moyenne_phrases = sum(longueurs_phrases) / len(longueurs_phrases) if len(longueurs_phrases) > 0 else 0

        # Mettre à jour les dictionnaires
        if balise not in dico_occurence:
            dico_occurence[balise] = 0
            dico_longueur_moyenne_phrases[balise] = 0

        dico_occurence[balise] += occurrence
        dico_longueur_moyenne_phrases[balise] += longueur_moyenne_phrases * occurrence

    # Calculer les moyennes finales et les stocker dans une liste
    data = []
    for balise in dico_occurence.keys():
        occurrence = dico_occurence[balise]
        longueur_moyenne_phrases = dico_longueur_moyenne_phrases[balise] / occurrence if occurrence > 0 else 0

        data.append([balise, longueur_moyenne_phrases])

    # Écrire les résultats dans un nouveau fichier tsv
    with open("resultats_phrases.tsv", "w") as f:
        f.write("balise\tmoyenne_phrases\n")
        for row in data:
            f.write(f"{row[0]}\t{row[1]}\n")

dictionnaire()
