
### 1. `DecisionTreeRegressor` (Arbre de décision)

* **Comment il fonctionne :** Il découpe récursivement l'espace des variables en règles binaires (`if feature <= seuil`) afin de regrouper des observations aux valeurs cibles proches. À chaque étape, il choisit la variable et le seuil qui minimisent le plus l'erreur quadratique moyenne (**MSE**) dans les sous-groupes créés. La prédiction finale dans une feuille correspond à la moyenne des `median_house_value` des exemples qui s'y trouvent.
* **Avantages :**
  * **Interprétabilité élevée :** On peut visualiser et suivre exactement les règles de décision (`plot_tree`).
  * **Peu de prétraitement :** Gère les relations non linéaires et les interactions entre variables sans mise à l'échelle.
* **Inconvénients :**
  * **Forte variance / surapprentissage :** Sans contraintes (`max_depth`, `min_samples_leaf`), un arbre mémorise le bruit des données d'entraînement et généralise mal.
  * **Instabilité :** De petites variations dans les données peuvent modifier complètement la structure de l'arbre.
  * **Découpages en escalier :** Produit des frontières constantes par morceaux, peu adaptées aux pentes continues.

---

### 2. `RandomForestRegressor` (Forêt aléatoire — *Bagging*)

* **Comment il fonctionne :** Il construit en parallèle un grand nombre d'arbres de décision indépendants. Chaque arbre est entraîné sur un échantillon *bootstrap* (tirage avec remise de même taille que le jeu d'entraînement) et, à chaque division de nœud, ne peut choisir que parmi un sous-ensemble aléatoire de variables (`max_features`). La prédiction finale est la **moyenne** des prédictions de tous les arbres.
* **Avantages :**
  * **Réduction drastique de la variance :** Moyenniser des arbres décorrélés limite fortement le surapprentissage par rapport à un arbre unique.
  * **Robustesse :** Supporte bien les valeurs aberrantes (*outliers*), le bruit et les relations non linéaires complexes.
  * **Facilité de réglage :** Donne souvent de très bons résultats dès les hyperparamètres par défaut.
* **Inconvénients :**
  * **Moins lisible :** Difficile d'inspecter individuellement des centaines d'arbres (on s'appuie plutôt sur l'importance des variables).
  * **Coût mémoire et calcul :** Plus lent à l'entraînement et à l'inférence qu'un seul arbre lorsque `n_estimators` est élevé.

---

### 3. `XGBRegressor` (*Extreme Gradient Boosting* — *Boosting*)

* **Comment il fonctionne :** Contrairement au Random Forest, les arbres sont construits **séquentiellement**. Le modèle commence par une prédiction initiale (souvent la moyenne), puis chaque nouvel arbre est entraîné pour prédire et corriger les erreurs résiduelles (liées au gradient de la fonction de perte) commises par l'ensemble précédent, multipliées par un taux d'apprentissage (`learning_rate`). XGBoost intègre explicitement une régularisation ($L_1$ et $L_2$) sur le poids des feuilles et la complexité de l'arbre.
* **Avantages :**
  * **Très haute précision prédictive :** Souvent parmi les meilleurs modèles sur données tabulaires structurées.
  * **Régularisation intégrée :** Contrôle finement la complexité des arbres pour limiter l'overfitting.
  * **Optimisations système :** Calcul parallélisé sur les splits, gestion native des valeurs manquantes et sous-échantillonnage (`subsample`, `colsample_bytree`).
* **Inconvénients :**
  * **Sensible aux hyperparamètres :** Demande un réglage rigoureux (`learning_rate`, `max_depth`, `n_estimators`, régularisations) pour éviter le surapprentissage.
  * **Temps d'optimisation :** Peut être plus long à ajuster sur un large espace de recherche (ex. avec Optuna).

---

### 4. `LGBMRegressor` (*LightGBM* — *Gradient Boosting* par feuilles)

* **Comment il fonctionne :** C'est une implémentation optimisée du *Gradient Boosting* qui regroupe les valeurs continues en **histogrammes** (discrétisation en *bins*) pour accélérer la recherche de seuils, et qui fait croître les arbres **par feuille (*leaf-wise*)** plutôt que par niveau (*depth-wise*) : à chaque étape, il divise la feuille qui réduit le plus la perte globale.
* **Avantages :**
  * **Rapidité et faible empreinte mémoire :** Les histogrammes et la gestion efficace des données rendent l'entraînement très rapide sur des dizaines de milliers de lignes.
  * **Précision élevée :** La croissance *leaf-wise* réduit souvent l'erreur plus vite qu'une croissance symétrique niveau par niveau à nombre de feuilles égal.
* **Inconvénients :**
  * **Risque d'overfitting sur petits jeux de données :** Diviser la feuille la plus prometteuse peut créer des arbres profonds et asymétriques sur des sous-groupes restreints ; il faut encadrer `num_leaves` et `min_child_samples`.
  * **Réglage plus délicat :** Requiert souvent plus de prudence sur les paramètres de régularisation que `RandomForestRegressor`.

---

### Récapitulatif comparatif rapide

| Modèle | Mécanisme central | Point fort majeur | Risque principal |
| :--- | :--- | :--- | :--- |
| **Decision Tree** | Règles hiérarchiques uniques | Interprétabilité visuelle | Surapprentissage (*overfitting*) |
| **Random Forest** | Moyenne d'arbres indépendants (*Bagging*) | Réduction de la variance et robustesse | Coût calcul/mémoire si beaucoup d'arbres |
| **XGBoost** | Correction séquentielle des erreurs + régularisation | Performance tabulaire et contrôle fin | Réglage des hyperparamètres plus exigeant |
| **LightGBM** | Boosting par histogrammes et croissance *leaf-wise* | Vitesse d'exécution et efficacité | Overfitting si `num_leaves` est trop grand |



| Catégorie / Modèle | Hyperparamètre | Rôle concret | Effet / Compromis (Biais vs Variance) |
| :--- | :--- | :--- | :--- |
| **Prétraitement** (`KNNImputer`) | `n_neighbors` | Nombre de districts voisins utilisés pour imputer les valeurs manquantes (`total_bedrooms`). | Trop petit = sensible au bruit ; trop grand = lisse trop les spécificités locales. |
| **Arbres & Random Forest** | `n_estimators` *(RF)* | Nombre d'arbres indépendants dans la forêt. | Plus élevé = réduit la variance et stabilise le score (plus lent, sans risque d'overfitting). |
| **Arbres & Random Forest** | `max_depth` | Profondeur maximale autorisée pour un arbre. | Plus élevé = capture des règles complexes, mais augmente fortement l'overfitting. |
| **Arbres & Random Forest** | `min_samples_split` | Nombre minimum d'échantillons requis pour diviser un nœud. | Plus élevé = freine la croissance de l'arbre (régularisation, réduit l'overfitting). |
| **Arbres & Random Forest** | `min_samples_leaf` | Nombre minimum d'échantillons requis dans une feuille finale. | Plus élevé = lisse les prédictions et évite les feuilles isolées sur des outliers. |
| **Random Forest** | `max_features` | Nombre de variables tirées aléatoirement à chaque division. | Plus faible = décorrèle les arbres entre eux et réduit la variance globale. |
| **Gradient Boosting** (`XGBoost` / `LightGBM`) | `learning_rate` (`eta`) | Poids accordé à la correction apportée par chaque nouvel arbre. | Plus faible (`0.01`–`0.1`) = apprentissage plus précis et robuste, nécessite plus d'arbres. |
| **Gradient Boosting** (`XGBoost` / `LightGBM`) | `n_estimators` | Nombre d'itérations séquentielles (arbres ajoutés). | Trop élevé = le modèle finit par mémoriser le bruit (overfitting), contrairement au RF. |
| **Gradient Boosting** (`XGBoost` / `LightGBM`) | `subsample` | Fraction des lignes échantillonnées aléatoirement pour chaque arbre. | `< 1.0` (ex. `0.8`) introduit du hasard pour réduire la variance et accélérer le calcul. |
| **Gradient Boosting** (`XGBoost` / `LightGBM`) | `colsample_bytree` | Fraction des colonnes (features) utilisées pour construire chaque arbre. | Évite qu'une variable dominante (ex. `median_income`) monopolise tous les arbres. |
| **Gradient Boosting** (`XGBoost` / `LightGBM`) | `reg_alpha` / `reg_lambda` | Pénalités de régularisation $L_1$ (Lasso) et $L_2$ (Ridge) sur les poids des feuilles. | Plus élevé = limite les prédictions extrêmes et réduit le surapprentissage. |
| **LightGBM** | `num_leaves` | Nombre maximal de feuilles par arbre (croissance *leaf-wise*). | Contrôle directement la complexité ; doit rester `< 2^max_depth` pour éviter l'overfitting. |







