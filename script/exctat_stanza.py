import stanza

# initialisation du pipeline stanza avec le modèle français
nlp = stanza.Pipeline('fr')

# ouverture des fichiers texte d'entrée et de sortie
with open('../Corpus/T_concat.txt', 'r') as f_in, open('output/lemma_PROPN_T.txt', 'w') as f_out:
    text = f_in.read()

    # traitement du texte avec stanza
    doc = nlp(text)

    # boucle sur les phrases du texte
    for sentence in doc.sentences:
        # boucle sur les mots de la phrase
        for word in sentence.words:
            # vérification si le mot est un verbe
            if word.upos == 'PROPN':
                # écriture du verbe et de son lemme dans le fichier de sortie
                f_out.write(f"{word.lemma}\n")
