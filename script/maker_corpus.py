from normalisation import *

def maker_corpus(file, output):
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

def normalisation_corpus(file, output):
    f = open(file).readlines()
    f_output = open(output, 'w')
    for line in f:
        l = line.split(" ")
        for e in l:
            e.strip()
            e = normalisation(e)
            f_output.write(e+" ")

    
normalisation_corpus("Corpus/TL.txt", "Corpus/Normalisation/TL_N.txt" )

