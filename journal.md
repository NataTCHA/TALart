## 23/03 (AS):

Concaténation des fichiers csv du dossier FR_Extractions annotations-20230323T194057Z-001 grâce à la commande bash cat *.csv > concatenation.csv
Il a ensuite fallu retirer les headers en trop directement sur libre office calc.
J'ai ensuite commencé un script python qui prend les balises. Il reste à l'organiser : faut-il faire un dictionnaire qui stocke les sources et les balises ?

## 26/03

Elaboration d'un script qui permet l extraction d'une colonne dans un fichier csv. Nous l'avons tout d'aord testé sur le csv des adj pour pouvoir après compter leur nombre par balise.

Elaboration d'un script qui compte le nombre de fois que l adj apparait par balise.

Elaboration d'un script qui extrait le premier mot de chaque appellation et compte le nombre de fois ou il apparait en first dans la colonne texte

Correction du fichier de concaténation car le csv est obsolète à cause de la présence de virugle dans la colonne "texte"


