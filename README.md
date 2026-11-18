# la_bataille_des_flandres
Le projet de Mathys Sergent sur le sujet de la bataille. 

Avancement.
Séance 1 : J'ai commencé la préparation du jeu, donc globallemment mes étapes étaient créer la classe "Carte" dans l'objectif de pouvoir créer une carte et les comparer, ensuite créer la classe "Paquet" pour créer toutes les cartes du jeu(48) automatiquement, les mélanger puis les distribuer entre les paquets des 2 joueurs. Tout marche sauf la distribution qui témoigne encore un bug. Je note l'idée tant que je l'ai encore, je peux imaginer un jeu à plusieurs joueurs comme extension. 

Séance 2: Aujourd'hui j'ai résolu le bug de la distribution de la dernière fois. J'ai aussi mis à jour la classe "Paquet" pour une meilleure utilisation de la POO. J'ai un peu amélioré la classe Carte aussi. Mais surtout j'ai créé comparer() et jouer() pour pouvoi simuler un début de tour. ça marche. Ensuite, je me suis attaqué à la fonctionnalité de "bataille". Quand les deux cartes sont égales et qu'on rejoue l'affrontement. Mais c'est pas encore fonctionnel. 

Séance 3: J'ai corrigé le bug lié à la comparaison égale et j'ai entammé une restructuration du code pour améliorer le POO. Mais ducoup ça m'amène à revenir sur beaucoup de choses. C'est assez compliqué. Je suis à un point où je reçois des "Paquet object is not subscriptable" donc je dois utiliser un __get_item__ apparement. C'est encore un peu flou.

Séance 4 : J'ai terminé le projet en finissant d'abords le prototype avec le système de point puis j'ai migrer le système de point vers la version réaliste du jeu avec le transfert de carte. J'ai fait pas mal de truc ces dernières heures donc je vais essayer de bien résumer. Donc le système de point n'avait pas besoin de get item en fait, le site que j'avais consulté antécédent devait faire allusion à un autre problème lié à cette log. Je crois que le problème était que j'avais pas précisé ".cartes". Globalement, j'ai croisé plusieurs types de bug, du index out of range que j'ai réglé en augmentant l'indice minimum pour commencer un cas d'égalité à 2. C'était une petite erreur d’inattention en gros. Et enfin, je me souviens que j'avais aussi un léger bug d'indentation... Pour la migration vers le système de transfert, il a fallu rebouger un peu tout. Et d'ailleurs, j'en ai profité pour créé une troisième classe Partie pour réunir la grosse logique tant que j'y étais. J'ai l'impression que c'est plus simple comme ça parce qu'avant la fonction comparer() prenait beaucoup de responsabilités. Les difficultés que j'ai eu avec la migration étaient plutôt sur la conception, parce qu'il fallait tout repenser ducoup. Et quand c'est devenu fonctionnel, la partie durait très longtemps. Mais vraiment, parfois j'ai l'impression qu'elle ne se finissait pas. Donc j'ai adopté un système de défausse et de mélange de la défausse pour que la partie se bouge d'elle même, dirais-je, et qu'elle se finisse.

Fonctionnement global :

1. Création et préparation du paquet
Le programme commence par créer un paquet de 52 cartes.
-Les quatre symboles sont créés : carreau, pique, trèfle et cœur.
-Pour chaque symbole, les valeurs vont de 1 à 13.
-Les cartes sont mélangées aléatoirement grâce à random.shuffle().

2. Distribution des cartes
Une fois le paquet mélangé :
-Deux paquets vides sont créés pour représenter les mains des joueurs.
-Chaque joueur reçoit alternativement une carte.
-La distribution continue jusqu'à ce que chaque joueur possède 26 cartes.

3. Initialisation de la partie
Une instance de la classe Partie est créée.
Elle contient :
-La main du joueur 1.
-La main du joueur 2.
-Une zone de bataille pour stocker les cartes jouées.
-Une défausse pour chaque joueur, qui permet de conserver les cartes remportées.
La méthode jouer() est ensuite lancée pour commencer la partie.

4. Vérification des cartes disponibles
Avant chaque tour, le programme vérifie si les deux joueurs possèdent suffisamment de cartes pour jouer.
C'est le rôle de la méthode preparer().
-Si un joueur possède encore des cartes dans sa main, il peut continuer.
-Si sa main est vide, mais qu'il possède une défausse, celle ci est mélangée puis remise dans sa main.
-Si le joueur ne possède plus aucune carte disponible, il ne peut plus jouer.

5. Déroulement d'un tour classique
Lorsque les deux joueurs peuvent jouer, chaque joueur envoie la première carte de sa main dans la zone de bataille.
Les deux cartes sont comparées grâce à la méthode comparer().
Le programme détermine le résultat :
  -Si le joueur 1 possède la carte la plus forte, il remporte le tour.
  -Si le joueur 2 possède la carte la plus forte, il remporte le tour.
  -Si les deux cartes ont la même valeur, ça déclenche une bataille.

6. Déroulement d'une bataille
Lorsqu'il y a égalité entre les deux cartes :
-Le programme vérifie que chaque joueur possède suffisamment de cartes pour continuer.
-Chaque joueur dépose une carte face cachée.
-Chaque joueur dépose ensuite une carte face visible.
-Les deux nouvelles cartes visibles sont comparées.
Trois situations sont possibles :
-Un joueur gagne : il remporte toutes les cartes présentes dans la zone de bataille.
-Une nouvelle égalité apparaît : une nouvelle bataille est déclenchée.
-Un joueur ne possède plus assez de cartes : l'autre joueur remporte la bataille. Si aucun des deux ne peut continuer, la partie se termine par un match nul.

7. Récupération des cartes
Lorsqu'un gagnant est déterminé :
-Toutes les cartes de la zone de bataille sont transférées dans sa défausse.
-La zone de bataille est vidée.
-Le programme revient ensuite au début de la boucle principale pour préparer le tour suivant.

8. Fin de la partie
La partie continue jusqu'à ce qu'une des conditions suivantes soit remplie :
-Le joueur 1 ne peut plus jouer : le joueur 2 gagne.
-Le joueur 2 ne peut plus jouer : le joueur 1 gagne.
-Aucun des deux joueurs ne peut continuer : match nul.
