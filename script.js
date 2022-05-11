/*

Bonjour à vous, qui regardez cette vidéo.
Aujourd'hui, nous allons vous présenter notre jeu du Pendu réalisé au cours des semaines précédentes
pendant nos heures d'Atelier Professionnalisé et aussi chez nous.
Avant de commencer à vous présenter ce que l'on a fait. Nous tenons à préciser que toutes les
fonctionnalités n'ont pu être terminées à temps.
Pour présenter notre jeu du Pendu, nous allons vous montrer comment on a construit le jeu étape par
étape

Nous pouvons préciser que nous avons fait le jeu avec l'IDE PyCharm et donc nous avons codé en
Python. 
Pour commencer, nous avons importé plusieurs bibliothèques comme nous pouvons le voir des lignes 1 à 6,
afin d'avoir de nouvelles fonctionnalités telles que l'interface graphique avec Tkinter ou le choix 
aléatoire du mot à deviner avec random.

La bibliothèque Tkinter est facile d'utilisation. Il suffit de savoir comment créer un élément puis le
placer. Pour déclarer la fenêtre de base, il faut ajouter la ligne de code suivante: 
pagePrincipale = Tk()
Ensuite, pour la faire apparaître lors du lancement du programme, on ajoute: 
pagePrincipale.mainloop()
A cette fenêtre, on peut lui ajouter les caractéristiques que l'on souhaite comme une couleur de fond,
ses dimensions, le titre de la fenêtre, etc... Par exemple, ligne 39, on modifie la couleur du fond 
de la fenêtre "aide" et ligne 40, on met la fenêtre en plein écran.

Pour intégrer des éléments avec lesquels l'utilisateur va intéragir, il faut impérativement placer tous
les éléments ENTRE la déclaration de la fenêtre ET sa génération.
Pour créer un élément, on prend un nom de variable ex: objet_01 et on lui attribue son type:
Label pour un texte, Entry pour une valeur à entrer par l'utilisateur, Button pour un bouton cliquable,
etc... Ces éléments doivent être suivis de parenthèses, qui permettront de lui donner des
caractéristiques telles que ses dimensions, la police d'écriture, etc...
Il est aussi impératif de définir dans quelle fenêtre va apparaître l'élément. Le nom de la fenêtre doit
impérativement être au début des parenthèses, avant les caractéristiques tel que:
objet_01 = Button(pagePrincipale, caractéristiques)
On peut prendre la fenêtre d'aide par exemple. Sa déclaration se fait à la ligne 33, les différents 
éléments vont de la ligne 42 à la ligne 57. Et enfin, on génère la page aide à la ligne 59.

Nous venons de créer ici un texte. Il faut donc maintenant le placer dans notre fenêtre. Pour cela, il
existe plusieurs fonctions telles que "pack" ou "place". Nous verrons le "place". Il s'utilise de la
manière suivante: 
objet_01.place(relx= , rely= , anchor=)
relx et rely correspondent à des coordonnées. Leurs valeurs doivent être comprises entre 0 et 1.
Pour ce qui est de l'anchor, on doit mettre son emplacement de reférence en fonction des points
cardinaux (Nord/Sud/Ouest/Est) et doivent être indiqués en lettres comme N, S, SE, etc... Le plus
simple reste d'utiliser la valeur "CENTER".
On peut prendre par exemple le "titre" de la page d'aide que l'on crée ligne 42, on le place 
directement ligne 43 avec ses coordonnées.

Grâce à la création de différents éléments, nous avons pu faire notre page principale, comprennant
plusieurs boutons, du texte, une zone à compléter par l'utilisateur et une liste déroulante.
Chaque bouton de cette page fait appel à une fonction. Les indications des boutons sont inscrites dessus.
Les boutons "Aide", "Gestion Mots" et "Classement" permettent d'afficher de nouvelles pages, qui sont
générées comme notre page principale.

La page d'aide affiche les règles du jeu, comment jouer et aussi ce que fait le choix de difficulté.
Elle contient seulement des éléments de type "Label" et un bouton pour retourner à la page principale.

La page classement , elle, était censée afficher le classement des meilleurs joueurs du pendu, avec 
leur pseudo, leur niveau de difficulté, leur score et la durée de leur partie. Par manque de temps, cette
page n'a pu être crée.

La page de gestion des mots sert quant à elle, à ajouter/supprimer des mots de la liste de mots. C'est
aussi sur cette page que l'on peut voir tous les mots présents dans la liste. [DESCRIPTION XML]

Le bouton quitter sert à quitter le jeu grâce à l'instruction: pagePrincipale.destroy()

Enfin, il nous reste la page de jeu. Lorsque l'on clique sur le bouton jouer de la page principale, 
la page vérifie que l'on a bien entré un pseudo ainsi qu'un niveau de difficulté. Si ce n'ets pas le cas, 
l'utilisateur ne peut pas jouer. A l'inverse, si les champs sont correctement remplis, la partie commence.
Cela génère une nouvelle page avec un clavier numérique AZERTY, que l'utilisateur devra utiliser 
pour jouer. Le niveau de difficulté choisi sera affiché et influera sur le score final de l'utilisateur.
On affiche aussi le nombre d'erreurs commises par l'utilisateur, un timer qui s'incrémente tant que la 
partie n'est pas terminée. Le timer influe aussi sur le score final de l'utilisateur.
Enfin, on affiche aussi, de manière cachée, le mot que l'utilisateur doit trouver. Le mot aura été choisi
aléatoirement dans le fichier XML grâce à la bibliothèque random.

Pour jouer, l'utilisateur clique sur la lettre qu'il veut. Chaque lettre fait appel à la même fonction
grâce à la ligne de code que l'on retrouve par exemple à la ligne 326. Cette ligne permet d'appeler la
fonction lorsque l'on clique sur le bouton. La fonction appelée récupère la valeur "text" du bouton puis
fait appel à une autre fonction. La fonction appelée permet de vérifier si la lettre choisie est présente
dans le mot à trouver. Si c'est le cas, l'affichage change. Enfin, la fonction principale appelle une 
autre fonction, qui elle, gère la fin de partie. Elle vérifie elle aussi si la lettre choisie est 
présente dans le mot. Si ce n'est pas le cas, elle ajoute 1 au compteur d'erreurs. Elle vérifie aussi
lorsque ce compteur dépasse ou égalisé la limite autorisée (la limite change en fonction du choix de la
difficulté). Si c'est le cas, la partie s'arrête et l'utilisateur a perdu. Elle rend utilisable les
boutons "Rejouer" et "Quitter" et désactive tous les boutons du clavier. Enfin, cette fonction appelée
fait une dernière vérification, si le mot à découvrir est totalement découvert, la partie s'arrête.
Si c'est le cas, elle fait elle aussi les actions citées précédemment mais au lieu de mettre un message
de défaite, il met un message de victoire.

*/