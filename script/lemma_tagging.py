import spacy
import argparse


"""Ce code permet d'annoter les lemmes d'un corpus en format txt stocker dans le dossier script/output/txtCorpus.
Il suffit de donner en premier argument le nom du corpus existant.
Il sort, dans le même dossier, un fichier au format voulu donné en deuxième argument
ex : python3 lemma_tagging.py AC.txt AC_lemma_ann.txt """


def lemma_tagging(fichier:str, destination:str):
    """fonction servant à annoter un fichier .txt passé en argument en POS avec Spacy"""
    texte = ""
    # Chargement du modéle d'annotation du français le plus précis de Spacy
    nlp = spacy.load("fr_core_news_lg")
    
    c = open(f"{fichier}","r")
    for line in c:
        texte += line.strip()+"\n"
    c.close()

    # Tokenization et traitement de la str
    doc = nlp(texte)

    lemma = open(f"./output/{destination}", "a")
    for token in doc:
        # On ignore les caractères d'espacement ou de retour à la ligne
        if token.text == " ":
            continue
        if token.text == "\n":
            lemma.write(f"\n")
        else:
            # On récupère le mot-forme, le lemme du mot traité et on les ajoute au document de sortie
            a,b = token.text, token.lemma_
            lemma.write(f"{a} : {b} / ")

    lemma.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("corpus_file", help="file.txt of the corpus data")
    parser.add_argument("output", help="output file")
    args = parser.parse_args()

    lemma_tagging(args.corpus_file, args.output)