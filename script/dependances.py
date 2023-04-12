
import spacy
from nltk import Tree
# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("fr_core_news_md")
c = open(f"../Corpus/AC.txt", 'r')
# Process whole documents
text = c.read()
doc = nlp(text)
# Analyze syntax


def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_


[to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
