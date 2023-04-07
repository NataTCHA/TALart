import spacy
import argparse


def POS_tagging(fichier:str, dest:str):
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

    nv_doc = open(dest,"a")
    for token in doc:
        # On ignore les caractères d'espacement ou de retour à la ligne
        if token.text == " ":
            continue
        if token.text == "\n":
            nv_doc.write(f"\n")
        else:
            # On récupère le mot-forme et l'annotation POS du mot traité et on les ajoute au document de sortie
            a,b,c = token.text, token.pos_, token.morph 
            nv_doc.write(f"/ {a} / {b} | {c} ")

    nv_doc.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("corpus_file", help="file.txt of the corpus data")
    parser.add_argument("output", help="output file")
    args = parser.parse_args()

    POS_tagging(args.corpus_file, args.output)