
def ecart_type_sur_moyenne_generale(dico, moyenne):
    import math
    #ecart_type à partir de la moyenne generale (sommes des occurences des balises / nb totals balises)
    carre_difference = []
    for cle, valeur in dico.items():
        x = ((valeur[0]-moyenne)**2)
        carre_difference.append(x)
        for i in range(len(carre_difference)-1):
            variance = (float(carre_difference[i]))+float(carre_difference[i+1])
    variance = variance/len(carre_difference)
    ecart_type = math.sqrt(variance)
    print("écart type à partir de moyenne générale", ecart_type)


def moyenne(dico, total_balise):
    moyenne = 0
    occurences = []
    for cle, valeur in dico.items():
        occurences.append(valeur[0])
        #part de cette balise sur le total
        valeur[1]=(valeur[0]/total_balise)
        #ajout de pourcentage
        valeur[2]=valeur[1]*100
    for i in range(len(occurences)-1):
        moyenne = occurences[i]+occurences[i+1]
    moyenne = moyenne / len(occurences)
    print(dico)
    print("moyenne", moyenne)
    ecart_type_sur_moyenne_generale(dico, moyenne)

def occurence():
    #ce programme compte les occurences et crée un dictionnaires (occurences, moyenne, pourcentage, écart-type)
    import pandas
    df = pandas.read_csv("concatenation.tsv",index_col = False, delimiter="\t") 
    df=df.astype(str)
    # converting column data to list
    dico_balise = {}
    balise = list(df['balise'])
    nombre = list(df['occurrence'])
    total_balise = 0
    for i in range(len(balise)):
        if balise[i] not in dico_balise:
            dico_balise[balise[i]]=[1, 0, 0]
            #la premiere valeur sera le nombre d'occurence, la deuxiemme la part de la balise sur le total, ensuite pourcentage
        elif balise[i] in dico_balise:
            for cle, valeur in dico_balise.items():
                if balise[i] == cle:
                    valeur[0]+=int(nombre[i])
    for e in nombre:
        total_balise += int(e)    
    moyenne(dico_balise, total_balise)
occurence()

