## 23/03 (AS):

Concaténation des fichiers csv du dossier FR_Extractions annotations-20230323T194057Z-001 grâce à la commande bash cat *.csv > concatenation.csv
Il a ensuite fallu retirer les headers en trop directement sur libre office calc.
J'ai ensuite commencé un script python qui prend les balises. Il reste à l'organiser : faut-il faire un dictionnaire qui stocke les sources et les balises ?

## 26/03

Elaboration d'un script qui permet l'extraction d'une colonne dans un fichier csv. Nous l'avons tout d'abord testé sur le csv des adj pour pouvoir après compter leur nombre par balise.\

ÉLaboration d'un script qui compte le nombre de fois que l'adj apparait par balise.\

Elaboration d'un script qui compte le nombre de fois que l adj apparait par balise.\

Elaboration d'un script qui extrait le premier mot de chaque appellation et compte le nombre de fois ou il apparait en first dans la colonne texte.\

Correction du fichier de concaténation car le csv est obsolète à cause de la présence de virugle dans la colonne "texte".\

Réccupération de la colonne "texte" dans le fichier concatenation.csv afin de créer un corpus pour un script SpaCy qui sortira tous les pos utilisés.\
 
Problème: spacy tokenise et donc toutes les appellations sont atomisées en tokens. 

<br />

### TODO:
Un script pour concaténer les pos et lemma des appellations et les rajouter en fonction des balises au document d'origine.\

Prendre en compte le nombre d'occurence des titres!


## 31/03:

On détermine des hypothèses de recherche:

PERSO: GENRE, ORIGINE, TYPE:

1. Faire une typologie des perso : dieux, héros, ... aussi par genre (fem/masc) et par origine (grec ou latin)
2. Le genre: quel genre est dominant ? (masculin/féminin)
3. De quoi sont suivis les personnages ? Un outil, un support, un verbe... de quel type ? De quel genre ?
4. Recherche sur le comportement des adj et des verbes en fonction du type de perso.
5. Lexique affectif des verbes et adj.



