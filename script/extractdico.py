import pandas as pd

def extract_csv_column(csv_file, column_name, output_file):
    # Charger le fichier CSV en tant que DataFrame pandas
    data = pd.read_csv(csv_file, delimiter="\t")

    # Extraire la colonne spécifiée
    column = data[column_name]

    # Créer un dictionnaire à partir de la colonne
    dictionary = column.to_dict()

    # Enregistrer le dictionnaire dans un fichier texte
    with open(output_file, 'a') as file:
        for key, value in dictionary.items():
            file.write(f"{value}\n")

    return dictionary

