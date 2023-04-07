def normalisation(mot):
    from unidecode import unidecode
    mot_normalise = unidecode(mot.capitalize())
    return mot_normalise

normalisation(mot)