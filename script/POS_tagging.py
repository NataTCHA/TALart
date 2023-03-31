import spacy

def POS_tagging(fichier):
    """fonction servant à annoter un fichier .txt passé en argument en POS avec Spacy"""
    texte = ""
    # Chargement du modéle d'annotation du français le plus précis de Spacy
    nlp = spacy.load("fr_dep_news_trf")
    
    doc = open(f"{fichier}","r")
    for line in doc:
        texte += line
    doc.close()

    # Tokenization et traitement de la str
    doc = nlp(texte)

    nv_doc = open("concatenation_POS.tsv","a")
    nv_doc[row].write(f"yo")
    for token in doc:
        # On ignore les caractères d'espacement ou de retour à la ligne
        if token.text == " " or token.text == "\n":
            continue
        else:
            # On récupère le mot-forme, le lemme et l'annotation POS du mot traité et on les ajoute au document de sortie
            a,b,c,d = token.text, token.lemma_, token.pos_, token.morph
            nv_doc.write(f"{a} {c}	{b}	{d} \n")
    nv_doc.close()

POS_tagging("./concatenation.tsv")