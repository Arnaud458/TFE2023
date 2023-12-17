# Notions théoriques

un signal => moyen de transport pour de l'info

signal peut se déplacer dans les airs, comment ? besoin de modulation ! 

(SIGNAL RADIO) la modulation permet en gros de le convertir le signal initial (on l'appelle baseband ou bande de base) en une version haute fréquence (qu'on appelle maintenant carrier singal) qui permet une meilleur propagation (distance, nécessité de puissance réduite pour les antennes, etc)
les plus connus c'est :
- la modulation en fréquence (FM lol ça vient de la), 
- en amplitude (AM) 
- ou encore en phase.

Pour lora c'est un truc différent qu'on appelle CSS (*chirp spread spectrum*) mais l'idée est la même.

c'est pas la seule étape pour pouvoir normalement faire voyager un signal, on peut aussi rajouter du codage, du filtrage, du multiplexage bref plein de truc entre l'émission et la réception.

dans un system Lora classique on va dire, on retrouve un truc a peu près comme ça :


|   | Etape | Description |
| - | ----- | ----------- |
| 1 | **Emission** | (mon beau singal lora) -----> (mon beau signal lora blanchi) ----> (mon beau singal signal Lora blanchi encodé) ---> (mon beau singal lora blanchi encodé modulé) |
| 2 | **Channel** | --------------- mon beau signal lora passe dans les air vers sa destination ----------- |
| 3 | **Reception** | (mon beau signal lora encore modulé encodé blanchi) ----> (mon beau signal lora encodé banchi) ----> (mon beau signal lora blanchi) ---> (mon beau singal lora) |

---


voila en gros chaque étape pour améliorer la qualité de la transmission (blanchiment, encodage,etc) doit être inversément faite à la réception pour récup le signal.

ça c'est le topo de base. Maintenant le but c'est quand je fais tout ça, je devrais être capable avec ce que je récupère à la réception (qui devrait être essentiellement le même signal qu'à l'émission) de trouver dans les infos de mon signal de quoi identifier le noeud qui l'a émis.

## Expérience

Déja, comment on replique un machin pareil dans gnu radio ? askip on peut ajouter des add on dans GNU radio, et MAGIE il en existe un pour LORA ! ducoup ya une page gihtub c'est la que tu intervient on regardera à ça comment l'ajouter. Avec cet addon, je devrais avoir de nouveau bloc dispo pour répliquer un bête scénario comme celui au dessus, on peut même tej des étapes ce qui compte c'est la modulation.

si ça marche (aucune chance mdr mais bon on y croit) alors faudra essayer de faire une autre emssion du même signal en rajoutant des imperfections (la déja plus avancée jpense). Si ça marche, alors on a fini la partie expérimentale. Il faut passer à l'analyse

## Analyse

la première technique (la seule que j'ai pigée) c'est en regardant la "constellation trace". je suis en train de lire le papier dessus mais en gros c'est assez bidon. Dans gnu quand j'ai passé l'étape de démodulation, je récup des "symboles I/Q" ce qui veut dire "in-phase (I) and quadrature (Q) components" du signal démodulé. Ces symboles bah suffit de les balancer dans matplotlib (c'est des complexe donc faut un plan complexe, les axe c'est honrizontal pour les réel et vertical pour les imaginaire) et on devrait observer des des points. Si on a fait deux fois le même signal mais avec des transmission un peu changée, et beh les "constellation", le tas de points dans le plot en gros sera différent. Ducoup on peut identifier qui est qui à partir de la 

la seconde technique c'est d'utiliser un spectrogram pour récupérer d'autre informations sur le signal. Ensuite faut utiliser un classificateur et faire du maching learning (dans l'exemple c'est un CNN) pour dénicher des pattern dans infos récupérée depuis le spectogram, je vais pas en détailes psk j'ai pas encore tout pigé et bon ça jpense même dans 2 semaine sje suis pas sur d'y être arrivé alors ça attendra mdr.
