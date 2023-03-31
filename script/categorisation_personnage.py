import pandas
import csv
from unidecode import unidecode

def categorisation_personnage(texte, nombre):
    #creer des listes pour les personnages romains et grecs + leurs occurence et leur genre + autres
    #read other doc
    df = pandas.read_csv("personnage_greco_romain.csv")
    df=df.astype(str)
    romain = list(df['Romain'])
    romain_normal = []
    for e in romain:
        e = unidecode(e)
        e = e.lower()
        romain_normal.append(e)
    romain = romain_normal
    grec_normal = []
    grec = list(df['Grec'])
    for e in grec:
        e = unidecode(e)
        e = e.lower()
        grec_normal.append(e)
    grec = grec_normal
    genre = list(df['Genre'])
    personnage_romains = {}
    personnage_grecs = {}
    autres_personnages = {}
    for i in range(len(texte)):
        mots = texte[i].split(' ')
        for mot in mots:
            if mot in romain and mot not in personnage_romains:
                personnage_romains[mot]=[int(nombre[i])]
            elif mot in romain and mot in personnage_romains:
                for key, value in personnage_romains.items():
                    if key == mot:
                        value[0] += int(nombre[i])
            elif mot in grec and mot not in personnage_grecs:
                personnage_grecs[mot]=[int(nombre[i])]
            elif mot in grec and mot in personnage_grecs:
                for key, value in personnage_grecs.items():
                    if key == mot:
                        value[0] += int(nombre[i])
            else:
                autres_personnages[mot]=[int(nombre[i])]
    print(personnage_romains)

    #create new tsv
    with open('personnages_romains.tsv', 'w', encoding='UTF8') as file:
        writer=csv.writer(file)
        header = ['personnage', 'occurence', 'genre']
        writer.writerow(header)
        for cle, valeur in personnage_romains.items():
            data = [cle, valeur[0]]
            writer.writerow(data)
    with open('personnages_grecs.tsv', 'w', encoding='UTF8') as file:
        writer=csv.writer(file)
        header = ['personnage', 'occurence', 'genre']
        writer.writerow(header)
        for cle, valeur in personnage_grecs.items():
            data = [cle, valeur[0]]
            writer.writerow(data)
    with open('autres_personnages.tsv', 'w', encoding='UTF8') as file:
        writer=csv.writer(file)
        header = ['personnage', 'occurence', 'genre']
        writer.writerow(header)
        for cle, valeur in autres_personnages.items():
            data = [cle, valeur[0]]
            writer.writerow(data)


#il faut normaliser et tout mettre en minuscule! retirer les accents ! et retirer les points et les tirets


def normalisation(texte, nombre):
    texte_normal = []
    for e in texte:
        e = unidecode(e)
        e = e.lower()
        texte_normal.append(e)
    categorisation_personnage(texte_normal, nombre)  

#cette fonction reprend celle du programme (dico_balise) mais en ajoutant la variable texte et sans lancer les autres fonctions
#Piste : il serait interessant de les merge en une seule et meme fonction eventuellement
def dictionnaire():
    #ce programme compte les occurences et crée un dictionnaires (occurences, moyenne, pourcentage, écart-type)
    df = pandas.read_csv("concatenation.tsv",index_col = False, delimiter="\t") 
    df=df.astype(str)
    # converting column data to list
    dico_balise = {}
    balise = list(df['balise'])
    nombre = list(df['occurrence'])
    texte = list(df['texte'])
    total_balise = 0
    for i in range(len(balise)):
        if balise[i] not in dico_balise:
            dico_balise[balise[i]]=[1, 0, 0, 0]
            #la premiere valeur sera le nombre d'occurence, la deuxiemme la part de la balise sur le total, ensuite pourcentage
        elif balise[i] in dico_balise:
            for cle, valeur in dico_balise.items():
                if balise[i] == cle:
                    valeur[0]+=int(nombre[i])
    for e in nombre:
        total_balise += int(e)  
    normalisation(texte, nombre)    
dictionnaire()

