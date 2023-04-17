import matplotlib.pyplot as plt
from categorisation_personnage import *
def graph_maker():
    with open('output/ACM_noun.txt', 'r') as f:
        word_count = {}
        for line in f:
            words = line.split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:20]
        x = [word[0] for word in top_words]
        y = [word[1] for word in top_words]

        # Définir les couleurs
        colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 
              'magenta', 'teal', 'navy', 'salmon', 'gold', 'indigo', 'lavender', 'tan', 'coral', 'lime']

        # Afficher le graphique avec les couleurs personnalisées
        plt.bar(x, y, color=colors[:len(x)])
        plt.xlabel('Mots')
        plt.ylabel('Nombre d\'occurrences')
        plt.title('Top 20 des noms communs les plus fréquents pour ACM')
        plt.show()


def piechart_AC_gender(array_women, array_men):
    import pandas
    import numpy as np
    y = np.array([array_women, array_men])
    mylabels = ["Femmes", "Hommes"]
    plt.pie(y, labels = mylabels)
    plt.legend(title = "Genre dans les Appelations Courtes")
    plt.show() 

def piechart_AC_origin(array_romain, array_grec, array_egyptiens, array_gaulois):
    import pandas
    import numpy as np
    y = np.array([array_romain, array_grec, array_egyptiens, array_gaulois])
    mylabels = ["Romains", "Grecs", "Egyptiens", "Gaulois"]
    plt.pie(y, labels = mylabels)
    plt.legend(title = "Origines des personnages Appelations Courtes")
    plt.show() 

def dictionnary_gender():
    #cette fonction fait un dictionnaire des personnages et de leur genre
    df = pandas.read_csv("../dictionnaires_personnages/personnage_greco_romain.csv")
    df=df.astype(str)
    romain = list(df['Romain'])
    normal_romain = normalisation(romain, 0)
    grec = list(df['Grec'])
    normal_grec = normalisation(grec, 0)
    genre = list(df['Genre'])
    personnage_romains = {}
    personnage_grecs = {}
    for i in range(len(normal_romain)):
        personnage_romains[normal_romain[i]]=[genre[i]]
    for i in range(len(normal_grec)):
        personnage_grecs[normal_grec[i]]=[genre[i]]
    #concatenation des deux dictionnaires
    personnage_total = personnage_romains | personnage_grecs
    return personnage_total





def get_gender():
    texte = open("../Corpus/AC.txt").readlines()
    normalized_texte = normalisation(texte, 0)
    #nb sera le nombre d'occurence pour chaque perso
    femmes = 0
    hommes = 0
    personnage_total = dictionnary_gender()
    for word in normalized_texte:
        word = word.replace("l'", " ")
        new_list = word.split( )
        for e in new_list:
            for cle, valeur in personnage_total.items():
                valeur = valeur[0]
                if e == cle and valeur == 'F':
                    femmes +=1
                elif e == cle and valeur == 'M':
                    hommes += 1
                #ajout de la gestion du y avant le mot
                if e[1:] == cle and valeur == 'F':
                    femmes +=1
                elif e[1:] == cle and valeur == 'M':
                    hommes += 1
    print("femmes: ", femmes," hommes:", hommes)
    piechart_AC_gender(femmes, hommes)

def get_origin():
    texte = open("../Corpus/AC.txt").readlines()
    normalized_texte = normalisation(texte, 0)
    #nb sera le nombre d'occurence pour chaque perso
    grecs = 0
    romains = 0
    egyptiens = 0
    gaulois = 0
    origines = dico_origin()
    for word in normalized_texte:
        word = ((((word.replace("l'", " ")).replace('/', ' ')).replace('.', ' ')).replace('-', ' ')).replace('?', '')
        new_list = word.split( )
        for e in new_list:
            for cle, valeur in origines.items():
                for i in range(len(valeur)):
                    print(valeur[i])
                    if e == valeur[i] and cle == "romains" or e[1:] == valeur[i] and cle == "romains":
                        romains += 1
                    elif e == valeur[i] and cle == "grecs"  or e[1:] == valeur[i] and cle == "grecs":
                        grecs += 1
                    elif e == valeur[i] and cle == "egyptiens":
                        egyptiens += 1
                    elif e == valeur[i] and cle == "gaulois":
                        gaulois += 1
    print("romains: ", romains," grecs:", grecs, " egyptiens", egyptiens, " gaulois:", gaulois)
    piechart_AC_origin(romains, grecs, egyptiens, gaulois)

def dico_origin():
    #cette fonction fait un dictionnaire des personnages et de leur genre
    df = pandas.read_csv("../dictionnaires_personnages/personnage_greco_romain.csv")
    df=df.astype(str)
    romain = list(df['Romain'])
    normal_romain = normalisation(romain, 0)
    print(normal_romain)
    grec = list(df['Grec'])
    normal_grec = normalisation(grec, 0)
    f = open('../dictionnaires_personnages/gaulois.txt').readlines()
    f2 = open('../dictionnaires_personnages/egyptiens.txt').readlines()
    liste_egyptiens = []
    liste_gaulois = []
    dico_origin = {}
    for name in f:
        name = (name.strip()).split(',')
        liste_gaulois.append(name[0])
    for name in f2:
        name = (name.strip()).split(',')
        liste_egyptiens.append(name[0])
    dico_origin["romains"]=normal_romain
    dico_origin["grecs"]=normal_grec
    dico_origin["egyptiens"]=liste_egyptiens
    dico_origin["gaulois"]=liste_gaulois
    print(dico_origin)
    return dico_origin
    

get_origin()