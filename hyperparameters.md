
## Pré-Elagage
| Hyperparameter | description |
| - | - | 
| max_depth | Profondeur maximale de l'arbre. Limite le nombre de niveaux de décision autorisés afin de contrôler la complexité du modèle et stopper sa croissance pour éviter le surapprentissage (overfitting) |
| min_samples_split | Nombre minimum d'exemples pour diviser un nœud. Un nœud ne sera pas séparé si le nombre d'observations qu'il contient est inférieur à ce seuil (correspondant au $N_{min}$ de taille d'échantillon local du cours) |
| min_samples_leaf | Nombre minimum d'exemples dans une feuille. Impose qu'une feuille finale contienne au moins un certain nombre d'observations, évitant ainsi la création de règles isolées basées sur du bruit |
| min_impurity_decrease | Réduction minimale d'impureté ($\Delta I$). Un nœud ne sera divisé que si la séparation apporte un gain d'information (baisse de l'entropie, de l'indice de Gini ou de la variance) supérieur ou égal à ce seuil |
