import matplotlib.pyplot as plt

with open('AE_verb.txt', 'r') as f:
    word_count = {}
    for line in f:
        words = line.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:20]
    x = [word[0] for word in top_words]
    y = [word[1] for word in top_words]

    # Définir les couleurs
    colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 
              'magenta', 'teal', 'navy', 'salmon', 'gold', 'indigo', 'lavender', 'tan', 'coral', 'lime']

    # Afficher le graphique avec les couleurs personnalisées
    plt.bar(x, y, color=colors[:len(x)])
    plt.xlabel('Mots')
    plt.ylabel('Nombre d\'occurrences')
    plt.title('Top 20 des verbes les plus fréquents pour AE')
    plt.show()
