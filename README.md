# Python Dashboard : ENDANGERED RAINBOW

## Sommaire

1. [Rapport d'analyse](#rapport-d'analyse)
2. [User Guide](#user-guide)
3. [Developper Guide](#developper-guide)

Trouvez toutes les données et sondages via ce lien :

[Open Data : FRA EU LGBT](https://fra.europa.eu/en/publications-and-resources/data-and-maps/survey-fundamental-rights-lesbian-gay-bisexual-and)

> Notes : Les deux sondages utilisés sont _"How many times did somebody physically/sexually attack or threaten you in the last 12 months ?"_ et _"Physically/sexually attacked or threatened with violence at home or elsewhere in the last 5 years for any reason"_ ; disponibles via le Topic _"Violence and harassment (47)"_.

---

# Rapport d'analyse

### Introduction

Actuellement, la place et la perception des personnes homosexuelles, transgenres, bisexuelles, etc., ne sont pas égalitaires partout dans le monde. Notamment dans l'Union Européenne, cette communauté a été soumise à de nombreuses discriminations, violences et persécutions. La communauté LGBTQ+ (Lesbian, Gay, Transgender, Queer, etc.) se combat dans le monde depuis le début du XXe siècle, pour aboutir à une égalité. Plusieurs mouvements et organisations ont vu le jour afin de faire place à la reconnaissance des droits des personnes LGBTQ+.

&nbsp;
Afin de comprendre les réalités de la communauté LGBTQ+, un dashboard a été conçu pour mettre en avant la qualité de vie que peuvent avoir ces personnes en fonction des pays de l'Union Européenne. Ce dashboard comprend une carte de l'UE (Union Européenne) montrant le pourcentage des violences physiques ou sexuelles visant les personnes LGBTQ+ durant ces 5 dernières années ainsi que trois histogrammes du nombre plus ou moins exacts des violences durant ces 12 derniers mois des pays de l'UE. En parcourant ce dashboard, nous nous demanderons :
**quels sont les pays et à quelle fréquence la communauté LGBTQ+ est le plus agressée physiquement ou verbalement ?**

&nbsp;
Premièrement, nous analyserons les pays les plus touchées par des agressions grâce à la carte interactive, montrant l'ensemble de l'UE
et des résultats du sondage des personnes LGBTQ+. Deuxièmement, nous verrons le nombre de fois où une personne LGBTQ+ a été menacé, ou agressé physiquement/sexuellement au cours de ces 12 derniers mois, dans l'UE.

## 1 - Les pays de l'UE les plus touchés

Partie de Léo

## 2 - Fréquence d'agression visant une personne LGBTQ+

En France, selon le premier histogramme, il y a un peu plus d'une chance sur deux qu'une personne LGBTQ+ se fasse agressée physiquement ou verbalement contre 3 à 4 % pour une fréquence allant de 4 à plus de dix fois. Les taux d'harcèlement quotidien est donc très bas comparé à une agression éventuelle.
![Image histogramme france](images/nombre_agressions_france.png)
En exploitant le deuxième et le dernier histogramme, on peut voir que les pays où le taux d'harcèlement est le plus élevé sont la Roumanie, la Lituanie et le Luxembourg. En effet, le pourcentage des fréquences s'équilibrent pour chacun des pays et les pourcentages des nombres d'agressions allant de 5 à plus de dix fois sont 2, voire 3 fois plus élevé que la plupart des pays.
![Image equilibre](images/equilibre_lituania_romania.png)
Nous avons un taux de 14% pour les agressions au Luxembourg de plus de dix fois (et 10%, 11% pour la Roumanie et la Lituanie), alors que la moyenne affiche un taux de 6% pour cette même catégorie (cf. _Average_). Ce qui prouve un taux d'harcèlement plus élevé pour ces trois pays. Sur l'image ci dessous, en rose, la moyenne de l'ensemble de l'UE concernant les agressions.
![Image comparaison avec moyenne](images/desequilibre.png)

### Conclusion

Ce dashboard nous a permis de découvrir les pays les plus touchés par les agressions visant la communauté LGBTQ+ ainsi que le nombre de fois où ces personnes ont été agressé dans les pays de l'UE. En effet, les pays les plus touchés sont : , , , ; où on peut apercevoir un pourcentage de %, pour le pays , ou encore un pourcentage de % pour le pays, avec un taux de % d'au moins une agression pour ce même pays.

&nbsp;
En parcourant ces données et en les analysant, on peut alors se demander si ces données reflètent de la qualité de vie des personnes LGBTQ+ dans ces pays, ou au minima, si elles sont un facteur qui reflèterait de la qualité de vie de la communauté. De plus, il serait intéressant d'établir une corrélation entre la qualité de vie d'une personne LGBTQ+ et les droits qu'elles possèdent dans son pays.

---

# User Guide

Bienvenue dans le guide de l'utilisateur de **Endangered Rainbow** !

&nbsp;
Ce guide de l'utilisateur est conçu pour fournir de la documentation aux personnes qui utiliseront le dashboard **Endangered Rainbow**, il est donc conçu pour être lu par tout utilisateur du dashboard.

## 1 - Explorer la carte interactive

Partie de Léo

## 2 - Découvrir les histogrammes interactifs

Le dashboard contient au total 3 histogrammes. Chaque histogramme a sa propre utilisation et fonctionnalités mais ces histogrammes ont quelques fonctionnalités communes.

#### Histogramme 1

Cet histogramme a pour but de montrer en détail, le taux d'agression selon un pays choisi. Le choix du pays se fait à l'aide de la sélection en cliquant sur le menu déroulant (dropdown). Le pays par défaut est la France. En cliquant sur un pays, un histogramme s'affiche. En passant la souris sur une des réponses _'Once'_, _'Twice'_, etc., on a le détail du pourcentage d'agression sur cette réponse.

#### Histogramme 2

Cet histogramme a pour but de voir l'ensemble des taux en fonction du pays de l'UE, et cela, en quelques secondes. L'animation permet un aperçu rapide des réponses. Cet histogramme n'a pas pour but d'entrer dans les détails. Pour cela, il faut se référer à l'histogramme 1. Le bouton Play est situé en bas à gauche du graphe, et permet de jouer l'animation. Le bouton Pause peut être activé pendant l'animation et permet d'arrêter l'animation afin de voir les réponses d'un pays. Ce bouton est situé à droite du bouton Play.

#### Histogramme 3

Cet histogramme a pour but de voir la globalité des réponses de chaque pays. Il peut être exploité de plusieurs manières. Par exemple, on peut chercher le taux le plus élevé en cherchant la barre la plus haute, et vice versa. De plus, nous pouvons l'utiliser pour comparer plusieurs pays ciblés, ce qui est utile quand on a un nombre de pays à comparer qui peut varier.

##### Sélectionner un ou plusieurs pays

Pour pouvoir sélectionner un ou plusieurs pays, il faut :

- Double-cliquer sur le pays en question, dans la barre `CountryCode` à droite du graphe,
- Après cette première sélection, on peut ajouter un pays, pour cela :
  - Cliquer une fois sur le deuxième pays choisi
  - Réitérer l'étape pour pouvoir en sélectionner un troisième, et ainsi de suite.

##### Désélectionner un pays

Pour pouvoir retirer un pays de la sélection totale, procéder ainsi :

- Cliquer une fois sur le pays à retirer, dans la barre `CountryCode`, à droite du graphe,
- Réitérer l'étape pour pouvoir en retirer d'autres.

##### Zoomer sur les catégories

Pour pouvoir zoomer sur les catégories de réponses des pays, procéder ainsi :

- Passer la souris en haut à droite du graphe pour afficher le `modebar`,
- Une fois le modebar violet apparu, cliquer sur `Box Select` (logo carré en pointillé),
- Sélectionner les catégories :
  - Cliquer enfoncé en prenant la zone des catégories voulues
  - Relaché le clic lorsque la zone a été choisie.
- Réitérer toutes les étapes ci-dessus pour zoomer davantage

> Notes : Pour revenir sur le mode d'origine, cliquer sur _Autoscale_ du modebar (logo flèches croisées en diagonale).

---

# Developper Guide

Bienvenue dans le guide du développeur de **Endangered Rainbow** !

&nbsp;
Ce guide du développeur est conçu pour fournir de la documentation aux personnes qui souhaiteront développer et approfondir les fonctionnalités du dashboard **Endangered Rainbow**, il est donc conçu pour être lu par tout développeur du dashboard.

## 1 - Programmer et améliorer la carte interactive

Partie de Léo

## 2 - Améliorer les histogrammes

- on effectue la division entière de `p` par `d`

  $ python ex03.py
  731 = 17 x 43 : False
  $ python ex03.py
  733 : True

- POUR chaque diviseur `d` parmi les valeurs `2` et les valeurs impaires inférieures à $`\sqrt{p}`$ (vérifier que ça suffit sur un exemple)
  - on effectue la division entière de `p` par `d`
  - SI le reste est nul, ALORS le nombre n’est pas premier et on interrompt le parcours de la boucle en affichant False
- FIN POUR
