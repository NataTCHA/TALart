import spacy

def POS_tagging(fichier):
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

    # nv_doc = open("./output/appelation_POS.tsv","a")
    lemma = open("./output/appelation_lemma.tsv", "a")
    # nv_doc[row].write(f"\n")
    for token in doc:
        # On ignore les caractères d'espacement ou de retour à la ligne
        if token.text == " ":
            continue
        if token.text == "\n":
            # nv_doc.write(f"\n")
            lemma.write(f"\n")
        else:
            # On récupère le mot-forme, le lemme et l'annotation POS du mot traité et on les ajoute au document de sortie
            a,b,c,d = token.text, token.pos_, token.morph, token.lemma_
            # nv_doc.write(f" / {a} / {b} , {c} , ")
            lemma.write(f"{a} : {d} / ")

    # nv_doc.close()
    lemma.close()

POS_tagging("./output/texte_appellation.txt")