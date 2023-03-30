import csv

# Ouvrir le fichier d'entrée
with open('concatenation.tsv', mode='r', encoding='utf-8') as input_file:
    reader = csv.reader(input_file, delimiter='\t')
    next(reader) # passer la première ligne des en-têtes
    data = {}
    for row in reader:
        balise = row[1]
        textes = row[3].split('.') # Séparer le texte en phrases
        occurence = int(row[2])
        longueurs_mots = []
        for texte in textes:
            mots = texte.split()
            longueurs_mots += [len(mot) for mot in mots]
        moyenne_mots = sum(longueurs_mots) / len(longueurs_mots) if longueurs_mots else 0
        if balise not in data:
            data[balise] = [moyenne_mots * occurence, occurence]
        else:
            data[balise][0] += moyenne_mots * occurence
            data[balise][1] += occurence

# Calculer la moyenne finale
moyennes_finales = {balise: round(data[balise][0] / data[balise][1], 2) for balise in data}

# Écrire les résultats dans un nouveau fichier tsv
with open('output_file.tsv', mode='w', encoding='utf-8') as output_file:
    fieldnames = ['balise', 'moyenne_mots']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    for balise in moyennes_finales:
        writer.writerow({'balise': balise, 'moyenne_mots': moyennes_finales[balise]})
