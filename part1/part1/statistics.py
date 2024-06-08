# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:21:32

@author: Erivan INAN
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def stats_des(data):
    """
    Affiche les statistiques descriptives de toutes les colonnes numériques du jeu de données.
    
    Parameters:
    data (pd.DataFrame): Le jeu de données à analyser.
    
    Returns:
    pd.DataFrame: Les statistiques descriptives du jeu de données.
    """
    descriptives = data.describe()
    print("Statistiques descriptives :")
    print(descriptives)
    return descriptives

def variance(data):
    """
    Affiche la variance de toutes les colonnes numériques du jeu de données.
    
    Parameters:
    data (pd.DataFrame): Le jeu de données à analyser.
    
    Returns:
    pd.Series: La variance de chaque colonne numérique.
    """
    num_cols = data.select_dtypes(include=['number']).columns
    variances = data[num_cols].var()
    print("Variances :")
    print(variances)
    return variances

def covariance(data):
    """
    Affiche la matrice de covariance de toutes les colonnes numériques du jeu de données.
    
    Parameters:
    data (pd.DataFrame): Le jeu de données à analyser.
    
    Returns:
    pd.DataFrame: La matrice de covariance.
    """
    num_cols = data.select_dtypes(include=['number']).columns
    cov_matrix = data[num_cols].cov()
    print("Matrice de covariance :")
    print(cov_matrix)
    return cov_matrix

def correlation(data):
    """
    Affiche la matrice de corrélation de toutes les colonnes numériques du jeu de données.
    
    Parameters:
    data (pd.DataFrame): Le jeu de données à analyser.
    
    Returns:
    pd.DataFrame: La matrice de corrélation.
    """
    num_cols = data.select_dtypes(include=['number']).columns
    corr_matrix = data[num_cols].corr()
    print("Matrice de corrélation :")
    print(corr_matrix)
    return corr_matrix


def matrice_correlation(data):
    """
    Compute and display the correlation matrix for the dataset.
    
    Parameters:
    data (pd.DataFrame): The dataset to analyze.
    
    Returns:
    None
    """
    # Select only numeric columns for correlation calculation
    numeric_data = data.select_dtypes(include=['number'])
    corr = numeric_data.corr()
    
    # Plot the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="pink")
    plt.title("Matrice de Correlations")
    plt.show()


def table_de_contingence_multi(data, cols, aggfunc='size'):
    """
    Crée et affiche une table de contingence pour plusieurs colonnes catégorielles.
    
    Parameters:
    data (pd.DataFrame): Le jeu de données à analyser.
    cols (list): Liste des colonnes catégorielles à inclure dans la table de contingence.
    aggfunc (str or function): Fonction d'agrégation à utiliser (par défaut 'size' pour le comptage).
    
    Returns:
    pd.DataFrame: La table de contingence.
    """
    
    # Vérifier que les colonnes existent dans le DataFrame
    for col in cols:
        if col not in data.columns:
            raise ValueError(f"La colonne {col} n'est pas dans le DataFrame.")
    
    # Créer la table de contingence
    contingence_table = pd.pivot_table(data, index=cols, aggfunc=aggfunc)
    
    # Afficher la table de contingence
    print("Table de contingence (multi-colonnes) :")
    print(contingence_table)
    
    return contingence_table

def categorize_column(data, column, bins, labels):
    """
    Crée une nouvelle colonne catégorisée à partir d'une colonne numérique.
    
    Parameters:
    data (pd.DataFrame): Le jeu de données à analyser.
    column (str): La colonne numérique à catégoriser.
    bins (list): Les limites des catégories.
    labels (list): Les étiquettes des catégories.
    
    Returns:
    pd.DataFrame: Le DataFrame avec une nouvelle colonne catégorisée.
    """
    if column not in data.columns:
        raise ValueError(f"La colonne {column} n'est pas dans le DataFrame.")
    
    data[f'{column}_category'] = pd.cut(data[column], bins=bins, labels=labels)
    return data