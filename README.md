# Projet Machine Learning : Arbres de Décision & Analyse Exploratoire

<img src="assets/dataset-cover.png" alt="Dataset Cover" width="400" style="display: block; margin-left: auto; margin-right: auto;"/>

Ce projet s'inscrit dans le cadre du cours d'**Algorithmes Avancés de Machine Learning** (Master 2 ASI / Ingénieur Industriel - Année 2026-2027).

---

## Objectif du Projet

L'objectif principal de ce projet est de réaliser une **Analyse Exploratoire des Données (EDA)** sur un dataset de notre choix, puis d'entraîner et d'évaluer un modèle basé sur un **Arbre de Décision** (classification ou régression) afin de prédire des données futures.

### Subdivisions & Enjeux :
1. **Exploration des données (EDA) :** Nettoyage, compréhension, prétraitement et visualisation des données.
2. **Modélisation par Arbre de Décision :** Mise en place d'un modèle de classification ou de régression.
3. **Hyperparamétrage & Optimisation :** 
   - Variation fine des hyperparamètres clés du modèle (`max_depth`, `min_samples_split`, `max_leaf_nodes`, critères d'impureté `gini`/`entropy` ou `MSE`/`MAE`).
   - *(Bonus)* Recherche automatique et optimisée des meilleurs hyperparamètres (optimisation bayésienne, métaheuristiques, etc. au-delà de la recherche exhaustive `GridSearchCV`).
4. **Évaluation & Analyse des performances :** Calcul et interprétation des métriques d'évaluation pertinentes (Accuracy, F1-score, Confusion Matrix, RMSE/MAE, R², etc.) pour mesurer la solidité du modèle.

---

## Informations sur le Dataset

- **Taille minimale requise :** 1 000 lignes × 10 colonnes.
- **Type de problème :** Classification / Régression.
- **Source :** [Kaggle Datasets](https://www.kaggle.com/datasets/camnugent/california-housing-prices).
- [Parameter description](https://github.com/justinFransolet/MASI5_PROJET1_ALGO/tree/clement/data#parameter-description)

---

## Installation et Utilisation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/justinFransolet/MASI5_PROJET1_ALGO.git
   cd MASI5_PROJET1_ALGO
   ```

2. **Créer et activer un environnement virtuel :**
   ```bash
   python -m venv venv
   ```
   
    Sous Windows:
    ```bash
    venv\Scripts\activate
    ```
   
    Sous Linux:
    ```bash
    source venv/bin/activate
    ```
    

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer le Notebook :**
   ```bash
   jupyter notebook
   ```

---

## Évaluation et Présentation

L'évaluation prend la forme d'une présentation orale synthétique (10 minutes de présentation + 10 minutes de Q/R) mettant l'accent sur :
- Les insights tirés de l'analyse exploratoire.
- La justification des choix de prétraitement.
- La stratégie d'optimisation des hyperparamètres.
- L'analyse critique des performances obtenues.
