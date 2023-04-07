def maker_corpus(file, designation, output):
    #cette fonction prend en argument un fichier source, une balise (appelation ou thème) et un fichier output
    import pandas as pd
    df = pd.read_csv(file, delimiter="\t")
    df=df.astype(str)
    # converting column data to list
    dico_balise = {}
    balise = list(df['balise'])
    nombre = list(df['occurrence'])
    texte = list(df['texte'])
    f = open(output, "w")
    for i in range(len(balise)):
        if balise[i] == designation:
            for ind in range(int(nombre[i])):
                print(texte[i])
                f.write(texte[i]+"\n")

    
maker_corpus("concatenation.tsv", "Appellation Complexe", "Corpus/ACM.txt")


