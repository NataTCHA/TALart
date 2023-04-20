import json
import pandas as pd

def find_cate_verb(corpus, dico):

    #On cherche les lemmes des verbes dans le tsv des verbes
    with open (corpus, 'r') as f:
        df = pd.read_table(f)
    verbes_as = df["lemme"]

    # On initilaise nos listes et dico vides.
    verbes=[]
    domaines=[]
    dico_cate_verbe={}
    count={}
    tmp=[]

    # On cherche les verbes et leurs domaines dans le jsonl
    with open(dico, "r") as json_file:
        jsonObj = pd.read_json(path_or_buf=json_file, lines=True)

    dico_verbe = jsonObj["MOT"]
    dico_domaine = jsonObj["DOMAINE"]

    # On créé une liste de tous les verbes contenus dans ce jsonl
    for i, verbe in enumerate(dico_verbe):
        verbes.append(verbe['verbe'])

    # On créé une liste de tous les domaines(=catégorie) des verbes.
    for i, dom in enumerate(dico_domaine):
        domaine = dom['clair']
        domaines.append(domaine)
        # On ajoute également les catégories uniques au dico count
        if domaine not in count:
            count[domaine] = 0

    # On créé un dico qui lie les verbes et leur catégorie.
    for i in range(len(verbes)-1):
        if verbes[i] == verbes[i+1]:
            verbes[i] = f'{verbes[i]} {i}'
        dico_cate_verbe[verbes[i]] = domaines[i]


    
    for verbe in verbes_as:
        verbe = verbe.lower()
        if verbe in dico_cate_verbe:
            print(verbe, dico_cate_verbe[verbe])
            count[dico_cate_verbe[verbe]]+=1
        # else:
        #     print(verbe)
    print(count)
            
            


find_cate_verb('./lemma_verb_AS.tsv', '../../LVF_modif.jsonl')