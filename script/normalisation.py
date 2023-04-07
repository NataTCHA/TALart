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
    mot_normalise = unidecode((mot.replace(",", "")).capitalize())
    return mot_normalise

normalisation("qu'Apollon")
