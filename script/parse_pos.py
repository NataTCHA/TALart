import spacy
import csv

nlp = spacy.load("fr_core_news_lg")
c = open("./texte_appellation.txt", 'r')

text = str(c.read())
doc = nlp(text)

with open('output.csv', 'w', encoding='UTF8') as file:

    writer=csv.writer(file)

    header = ['token_spacy', 'lemma', 'pos', 'info pos']

    writer.writerow(header)

    for token in doc:
        data = [token.text, token.lemma_, token.pos_, spacy.explain(token.pos_)]
        writer.writerow(data)