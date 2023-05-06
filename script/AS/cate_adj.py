import json
import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt

def find_cate_adj(corpus, dico_dir):

    #On cherche les lemmes des adjectifs dans le tsv des adjectifs
    with open (corpus, 'r') as f:
        df = pd.read_table(f)
    adj_lemmes = df["lemme"] # ATTENTION à bien vérifier que le csv à une colonne nommée lemme

    # On initilaise les dico à remplir.
    dico_cat_adj={}
    dico_count={}


    # On cherche dans le csv les adjectif en fonction des catégories
    with open(f'{dico_dir}/dico_adj.csv', 'r') as file:
        df = pd.read_csv(file)

    column_headers = list(df.columns.values)

    for head in column_headers:
        dico_count[head]=''
        #On remplit le dico avec en key la catégorie et en valeur la liste de adjectifs.
        dico_cat_adj.update({head:list(df[head])})

    for cat, adjectif in dico_cat_adj.items():
        count=0
        #pour chaque adjectif dans la liste de adjectifs de chaque catégorie
        for adj in adjectif:
            #pour chaque lemme dans les appellations
            for lemme in adj_lemmes:
                if lemme == adj:
                    count+=1
        dico_count[cat]=count

    return dico_count
            
def make_piechart():
    dico_adj = find_cate_adj('./lemma_ADJ_T.csv', '../../dico_adj')
    mylabels=[]
    mydata=[]
    print(dico_adj)
    for k, v in dico_adj.items():
        mylabels.append(k)
        mydata.append(v)
    y = np.array(mydata)
    colors = [ 'green', 'pink', 'red', 'purple', 'brown', 'blue', 'blue', 
              'magenta', 'teal', 'navy', 'salmon', 'gold', 'indigo', 'lavender', 'tan', 'coral', 'lime']
    print(mylabels)
    print(y)
    plt.pie(y, labels = mylabels, colors = colors, autopct='%1.0f%%', startangle = 90)
    plt.title(label = "Les types d'adjectifs présents dans les Thèmes:")
    plt.legend(title = "Légende")
    plt.show() 



make_piechart()