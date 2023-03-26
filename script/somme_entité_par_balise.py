import pandas as pd

def count_adj_occurrences(adj_file, csv_file, output_file):
    # Charger le fichier texte contenant les adjectifs
    with open(adj_file, 'r') as f:
        adjs = f.read().splitlines()

    # Charger le fichier CSV contenant les balises et les textes
    df = pd.read_csv(csv_file, delimiter="\t")

    # Initialiser un dictionnaire pour stocker les résultats
    results = {}

    # Pour chaque balise, compter le nombre total d'occurrences d'adjectifs
    for balise in df['balise'].unique():
        # Filtrer le DataFrame pour ne garder que les lignes avec la balise actuelle
        df_balise = df[df['balise'] == balise]

        # Compter le nombre total d'occurrences d'adjectifs dans le texte
        total_adj_count = df_balise['texte'].str.count('|'.join(adjs)).sum()

        # Ajouter le résultat au dictionnaire
        results[balise] = total_adj_count

    # Écrire les résultats dans un fichier texte
    with open(output_file, 'w') as f:
        for balise, count in results.items():
            f.write(f"Nombre total d'adjectifs pour la balise '{balise}': {count}\n")

count_adj_occurrences("output_adj.txt","concatenation.csv","num_dadj.txt")