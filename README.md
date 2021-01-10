# Python Dashboard : Rapport d'analyse

## 1 - Le premier

L'exercice d'application ci dessous correspond au chapitre [Les dictionnaires](https://perso.esiee.fr/~courivad/Python/10-dict.html).

Le fichier `data/stations-meteo.csv` contient la liste des stations d’observation de Météo France et un certain nombre d’informations s’y rapportant. Ecrire la fonction `build_stations_dict()` prenant en argument le fichier `csv` précédent et retournant un dictionnaire dont la clé est le nom de la station et la valeur un `namedtuple()` contenant l’ID, la latitude, la longitude et l’altitude de la station. Les tuples nommés ont été présentés au chapitre [Les tuples](https://perso.esiee.fr/~courivad/Python/07-tuples.html).

Pour cet exercice, vous devez utiliser en priorité le squelette contenu dans le fichier `ex10.py`.

# Python Dashboard: User Guide

## 1 - Premier titre

"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

- POUR chaque diviseur `d` parmi les valeurs `2` et les valeurs impaires inférieures à $`\sqrt{p}`$ (vérifier que ça suffit sur un exemple)
  - on effectue la division entière de `p` par `d`
  - SI le reste est nul, ALORS le nombre n’est pas premier et on interrompt le parcours de la boucle en affichant False
- FIN POUR
- Sinon, il est premier et on affiche True

L’affichage doit ressembler à:

    $ python ex03.py
    731  =  17 x 43  : False
    $ python ex03.py
    733  : True

# Python Dashboard: Developper Guide

## 1 - The first

`"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."`

Vous devez écrire le code de la fonction `pal()` en utilisant éventuellement des `print()` intermédiaires pour observer les valeurs des variables au cours de l’exécution. Ces `print()` devront être retirés lorsque la fonction sera correcte.

> Note : ce problème peut être résolu à "bas niveau" en itérant sur les caractères ou à plus "haut niveau" en utilisant les méthodes spécifiques aux chaines de caractères. La deuxième approche, plus _pythonique_ est à privilégier.
