import pandas as pd
import re
from tabulate import tabulate

def count_appellations(filename):
    df = pd.read_csv(filename, sep='\t')
    counts = []
    for balise, sub_df in df.groupby('balise'):
        sub_counts = sub_df['texte'].astype(str).apply(lambda x: re.findall(r'^\w+(?:\'\w+)?', x)).explode().value_counts().to_dict()
        for word, count in sub_counts.items():
            counts.append((balise, word, count))
    return counts

counts = count_appellations('concatenation.csv')

# Output  tsv file
with open('premiermot.tsv', 'w') as f:
    f.write('Balise\tMot\tNombre d\'occurrences\n')
    for row in counts:
        f.write(f"{row[0]}\t{row[1]}\t{row[2]}\n")

# Output text file
with open('premiermot.txt', 'w') as f:
    for balise, sub_counts in pd.DataFrame(counts, columns=['Balise', 'Mot', 'Nombre d\'occurrences']).groupby('Balise'):
        f.write(f"{balise}:\n")
        table = sub_counts[['Mot', 'Nombre d\'occurrences']].values.tolist()
        f.write(tabulate(table, headers=['Mot', 'Nombre d\'occurrences'], tablefmt='orgtbl'))
        f.write('\n\n')
