import json
import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt

def find_cate_verb(corpus, dico_dir):

    #On cherche les lemmes des verbes dans le tsv des verbes
    with open (corpus, 'r') as f:
        df = pd.read_table(f)
    verbes_lemmes = df["lemme"] # ATTENTION à bien vérifier que le csv à une colonne nommée lemme

    # On initilaise les dico à remplir.
    dico_cat_verbe={}
    dico_count={}
    merde=[]
    bon=[]

    # On cherche dans le csv les verbe en fonction des catégories
    with open(f'{dico_dir}/categorie_verbes.csv', 'r') as file:
        df = pd.read_csv(file)

    column_headers = list(df.columns.values)

    for head in column_headers:
        dico_count[head]=''
        #On remplit le dico avec en key la catégorie et en valeur la liste de verbes.
        dico_cat_verbe.update({head:list(df[head])})

    for cat, verbe in dico_cat_verbe.items():
        count=0
        #pour chaque verbe dans la liste de verbes de chaque catégorie
        for v in verbe:
            #pour chaque lemme dans les appellations
            for lemme in verbes_lemmes:
                if lemme == v:
                    count+=1
        dico_count[cat]=count

    return dico_count
            
def make_piechart():
    dico_verbe = find_cate_verb('./lemma_verb_AE.tsv', '../../dico_vb')
    mylabels=[]
    mydata=[]
    print(dico_verbe)
    for k, v in dico_verbe.items():
        mylabels.append(k)
        mydata.append(v)
    y = np.array(mydata)
    colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'gray', 'olive', 'cyan', 
              'magenta', 'teal', 'navy', 'salmon', 'gold', 'indigo', 'lavender', 'tan', 'coral', 'lime']
    print(mylabels)
    print(y)
    plt.pie(y, labels = mylabels, colors = colors, autopct='%1.0f%%', startangle=90)
    plt.title(label = "Les catégories des verbes présents dans les Appellations Enrichies : 'verbe de ...'")
    plt.legend(title = "Légende")
    plt.show() 



make_piechart()