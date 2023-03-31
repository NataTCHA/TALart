import pandas as pd


def count_adj_occurrences(adj_file, csv_file, output_file):
    # Charger le fichier texte contenant les adjectifs
    with open(adj_file, 'r') as f:
        adjs = f.read().splitlines()
    
    # Charger le fichier CSV contenant les balises et les textes
    df = pd.read_csv(csv_file, delimiter="\t")
    
    # Initialiser un dictionnaire pour stocker les résultats
    results = {}
    
    # Pour chaque balise, compter le nombre d'occurrences de chaque adjectif
    for balise in df['balise'].unique():
        # Filtrer le DataFrame pour ne garder que les lignes avec la balise actuelle
        df_balise = df[df['balise'] == balise]
        
        # Compter le nombre d'occurrences de chaque adjectif dans le texte
        adj_counts = {}
        for adj in adjs:
            adj_counts[adj] = df_balise['texte'].str.count(adj).sum()
        
        # Ajouter les résultats au dictionnaire
        results[balise] = adj_counts
    
    # Écrire les résultats dans un fichier texte
    with open(output_file, 'w') as f:
        for balise, counts in results.items():
            f.write(f"Occurrences des adjectifs pour la balise '{balise}':\n")
            for adj, count in counts.items():
                f.write(f"{adj} est présent {count} fois\n")
    


count_adj_occurrences('output_pos.txt', './output/concat_pos_lemma.tsv',"output_count_pos_test.txt")
