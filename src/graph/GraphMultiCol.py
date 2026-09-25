# src/graph/GraphMultiCol.py

from math import ceil

from matplotlib.pyplot import subplots, tight_layout, show
from seaborn import countplot, boxplot


def plot_countplots_side_by_side(features, data, n_cols=3):
    if len(features) == 0:
        return

    # Calcul du nombre de lignes nécessaires
    n_rows = ceil(len(features) / n_cols)
    fig, axes = subplots(n_rows, n_cols, figsize=(7 * n_cols, 4.5 * n_rows))

    # Normalisation des axes sous forme de tableau 1D
    if n_rows == 1 and n_cols == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for idx, column in enumerate(features):
        ax = axes[idx]
        countplot(x=data[column], ax=ax)
        ax.set_title(f"Distribution of {column}")

        # Ajuster dynamiquement la densité des labels
        labels = ax.get_xticklabels()
        max_labels = 10
        step = max(1, len(labels) // max_labels)

        # Application des ticks et de la rotation
        ticks_locs = range(0, len(labels), step)
        ax.set_xticks(ticks_locs)
        ax.set_xticklabels(
            [labels[i].get_text() for i in ticks_locs], rotation=45
        )

    # Masquer les sous-graphiques vides s'il y a un nombre impair d'éléments
    for idx in range(len(features), len(axes)):
        fig.delaxes(axes[idx])

    tight_layout()
    show()


def plot_boxplots_side_by_side(numerical_features, categorical_column, data, n_cols=3):
    if len(numerical_features) == 0:
        return

    # Calcul du nombre de lignes nécessaires
    n_rows = ceil(len(numerical_features) / n_cols)
    fig, axes = subplots(n_rows, n_cols, figsize=(7 * n_cols, 4.5 * n_rows))

    # Normalisation des axes sous forme de tableau 1D
    if n_rows == 1 and n_cols == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for idx, column in enumerate(numerical_features):
        ax = axes[idx]
        boxplot(x=data[categorical_column], y=data[column], ax=ax)
        ax.set_title(f"{column} by {categorical_column}")

        # Rotation des labels de l'axe X si les catégories sont longues
        ax.tick_params(axis="x", rotation=45)

    # Masquer les sous-graphiques vides s'il y a un nombre impair d'éléments
    for idx in range(len(numerical_features), len(axes)):
        fig.delaxes(axes[idx])

    tight_layout()
    show()