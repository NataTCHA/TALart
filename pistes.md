# Démarches et pistes pour le projet:
<br/>
1) explorer les données, les trier, si besoin nettoyage

# Annotation 
1. Balises d’annotation (Majuscules en début de mots) et abréviations de graphe :

Appellation Courte : AC
Appellation Structurée : AS
Appellation Enrichie : AE
Appellation Complexe : AX
Thème : TM


### To do list générale

- [ ] Comprendre le projet
- [x] Regrouper la totalité des appelations et les laisser trier pour faciliter les stats
- [ ] Se décider sur le type de calculs statitisques interessant dans le cadre de ce devoir. Ecart type et Moyenne obligés sur l ensemble du corpus!!
- [ ] Construire un script python le plus pratique et comprehensible pour bluffer Iris et ses potes. 
- [ ] Réflechir sur des representations visuelles claires et précises dès le premier coup d'oeil
- [ ] Suite aux données en tirer des conlusions sur le type de POS fréquent , la longueur des appelations , la richesse sémanticale au vue du thème de l'art( bo vocabulaire obligé)


### To do list Python / Stat

- [ ] Mesure interessante :moyenne/ frequence/ ecart type longueur des mots, moyenne/ frequence/ ecart type POS, moyenne/ frequence/ ecart type Structure Syntaxicale, moyenne/ frequence/ Sémantique
- [ ] penser à instaurer un calcul stat pour toutes les branches de la grammaire ! ( ne pas oublier la morphologie , rien est negligeable)
- [ ] Envisager une fonction python pour chaque type de calcul ( avec pandas peut être si on travail sur un sheet )
- [ ] si on fait une fonction pour chaque calcul il serait parfait de constituer une sorte de menu qui indique par ex ( 1 pour calculer la longueur des mots de votre data base )
- [ ] faire en sorte que nos scripts python soient universaux , privilégier les arguments à tapper dans l invit de commande
- [ ] faire des graphs trop beau et une analyse aux petits oïgnons pour le jour J

- [x] Faire moyenne et écart type par appelation  thème
2) faire des moyennes dans les appelations --> parser dans appelation
- Faire un fonction qui avec spacy trouve les pos dans les appelations et les met en relation avec le thème.
- [ ] voir le model toppic de spacy
