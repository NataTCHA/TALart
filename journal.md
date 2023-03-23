23/03 (AS):
Concaténation des fichiers csv du dossier FR_Extractions annotations-20230323T194057Z-001 grâce à la commande bash cat *.csv > concatenation.csv
Il a ensuite fallu retirer les headers en trop directement sur libre office calc.
J'ai ensuite commencé un script python qui prend les balises. Il reste à l'organiser : faut-il faire un dictionnaire qui stocke les sources et les balises ?
