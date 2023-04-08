def normalisation(mot):
    from unidecode import unidecode
    mot = mot.replace("-", '')
    mot = mot.replace("l'", '')
    mot = mot.replace("_", '')
    mot = mot.replace(".", '')
    mot = mot.replace("^", '')
    mot = mot.replace("(", '')
    mot = mot.replace(")", '')
    mot = mot.replace("?", '')
    mot = mot.replace("qu'", '')
    mot = mot.replace("'", '')
    mot = mot.replace("d'", '')
    mot = mot.replace(",", '')
    mot = mot.replace(",", "")
    mot_normalise = ""
    for i in range(len(mot)):
        if i ==0:
            mot_normalise+= mot[0]
        else:
            mot_normalise+= mot[i].lower()
    mot_normalise = unidecode(mot_normalise)
    return mot_normalise