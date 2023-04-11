import spacy
import pandas

def count_noun_occurrences(file, sortie, sortie2):
    # Charger le corpus d'appellation
    texte=""

    # Chargement du modéle d'annotation du français le plus précis de Spacy
    nlp = spacy.load("fr_core_news_lg")
    c = open(f"../Corpus/{file}", 'r')
    pos_noun = open(sortie, "w")
    pos_propn = open(sortie2, "w")
    liste_noun = []
    liste_propn = []
    for line in c:
        texte += line.strip()+"\n"
    c.close()

    # Tokenization et traitement de la str
    doc = nlp(texte)
    # nv_doc = open("./output/appelation_POS.tsv","a")
    # nv_doc[row].write(f"\n")
    count_noun = 0
    count_propn = 0
    df = pandas.read_csv("../dictionnaires_personnages/personnage_greco_romain.csv")
    df=df.astype(str)
    romain = list(df['Romain'])
    grec = list(df['Grec'])
    for token in doc:
            # On récupère le mot-forme, le lemme et l'annotation POS du mot traité et on les ajoute au document de sortie
            a,b, c = token.text, token.pos_, token.morph
            d = token.lemma_
            # nv_doc.write(f" / {a} / {b} , {c} , ")
            if b == "NOUN" and a not in romain and a not in grec and a != "-":
                count_noun+=1
                print(a, b)
                liste_noun.append(a.lower())
            elif b=="PROPN" and a != "-":
                count_propn+=1
                print(a, b)
                liste_propn.append(a)
            for e in romain:
                if a == e and b != "PROPN":
                    liste_propn.append(a)

    pos_noun.write("Il y a "+str(count_noun)+" noms communs dans les "+ file+"\n")
    pos_propn.write("Il y a "+str(count_propn)+" noms communs dans les "+ file+"\n")
    for noun in liste_noun:
            pos_noun.write(noun+"\n")
    for propn in liste_propn:
            pos_propn.write(propn+"\n")

    print(count_noun)
    print(count_propn)


count_noun_occurrences("TL.txt", "output/TL_noun.txt", "output/TL_propn.txt")