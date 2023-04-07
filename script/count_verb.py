import jsonlines
import json
import re
import argparse

def count_verb_occurrences(file:str, output_file:str):
    # Charger le corpus d'appellation
    text=""
    with open(f"../Corpus/{file}", 'r') as f:
        for line in f:
            text += line.strip()
     
    list_verb = re.findall(r"/ \w+ / VERB|/ \w+ / AUX", text)


    print(list_verb)
    print(len(list_verb))

    
    # Écrire les résultats dans un fichier texte
    with open(f"./output/{output_file}", 'w') as f:
        f.write(f"Il y a {len(list_verb)} verbes dans les {file} : \n")
        for verb in list_verb:
            f.write(f"{verb[2:-6]}\n")
        # for balise, counts in results.items():
        #     f.write(f"Occurrences des adjectifs pour la balise '{balise}':\n")
        #     for adj, count in counts.items():
        #         f.write(f"{adj} est présent {count} fois\n")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("corpus", help="file.txt of the corpus data")
    parser.add_argument("output", help="output file")
    args = parser.parse_args()

    count_verb_occurrences(args.corpus, args.output)
