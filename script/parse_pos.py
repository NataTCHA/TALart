import spacy
import csv
# from extractdico import extract_csv_column


def spacy_parse_pos_lemma(corpus):
    # On load ce qu'il faut pour spacy (ici, large!)
    nlp = spacy.load("fr_core_news_lg")
    # On donne le chemin vers le corpus en paramètre
    c = open(corpus, 'r')

    text = str(c.read())
    doc = nlp(text)


    #Écrit l'output dans un csv
    with open('./output/pos_lemma.sv', 'w', encoding='UTF8') as file:

        writer=csv.writer(file)

        header = ['token_spacy', 'lemma', 'pos', "morph"]

        writer.writerow(header)

        for token in doc:
            if token.pos_=="SPACE":
                continue
            else:
                data = [token.text, token.lemma_, token.pos_, token.morph]
                writer.writerow(data)

spacy_parse_pos_lemma("./output/texte_appellation.txt")