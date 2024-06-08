# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:21:32

@author: Erivan INAN

Module de visualisation, comprenant divers graphiques adaptés à nos données. 
"""

# Importation des librairies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importation des modules 
import loading
from loading import *

fichier = "eCO2mix_RTE_Annuel-Definitif_2020.csv"
dataRTE = loading.lecture2(fichier)

# Calculer la somme de la consommation pour chaque catégorie
categories = ['Fioul', 'Charbon', 'Gaz', 'Nucléaire', 'Eolien', 'Solaire', 'Hydraulique', 'Pompage', 'Bioénergies']
sums = {}

def calculate_consumption_sums(df, categories):
    """
    Calcule la somme de la consommation pour chaque catégorie spécifiée.
    
    :param df: DataFrame pandas contenant les données.
    :param categories: Liste des catégories pour lesquelles calculer la consommation.
    :return: Dictionnaire avec les catégories comme clés et les sommes de consommation comme valeurs.
    """
    # Remplacer les valeurs manquantes par 0 et s'assurer que toutes les valeurs sont non négatives
    df = df.fillna(0)
    for category in categories:
        df[category] = df[category].apply(lambda x: max(x, 0))
        
    sums = {category: df[category].sum() for category in categories}
    return sums


# Crée un pie chart pour chaque catégorie
def plot_pie_chart(data, title):
    """
    Affiche un graphique en secteurs (pie chart) basé sur les données fournies.

    :param data: Dictionnaire avec les catégories comme clés et les valeurs de consommation comme valeurs.
    :param title: Titre du graphique.
    """
    labels = data.keys()
    sizes = data.values()
    
    # Vérifier les valeurs de 'sizes' pour s'assurer qu'elles sont toutes non négatives
    if any(size < 0 for size in sizes):
        raise ValueError("Les tailles des parts du pie chart doivent être des valeurs non négatives")

    # Définir une palette de couleurs pastel
    colors = sns.color_palette("pastel", len(labels))
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title(title)
    plt.axis('equal')  # Assure que le pie chart est dessiné comme un cercle
    plt.show()

def plot_consumption_trends(dataRTE, categories):
    """
    Affiche les tendances de consommation annuelle pour chaque catégorie sur un même graphique.

    :param dataRTE: DataFrame pandas contenant les données.
    :param categories: Liste des catégories pour lesquelles tracer les tendances de consommation.
    """
    plt.figure(figsize=(14, 8))
    
    for category in categories:
        plt.plot(dataRTE['Date'], dataRTE[category], label=category)
    
    plt.xlabel('Date')
    plt.ylabel('Consommation (MW)')
    plt.title('Évolution de la consommation annuelle par catégorie')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_consumption_trends2(dataRTE, categories):
    """
    Affiche les tendances de consommation annuelle pour chaque catégorie sur un même graphique.

    :param dataRTE: DataFrame pandas contenant les données.
    :param categories: Liste des catégories pour lesquelles tracer les tendances de consommation.
    """
    plt.figure(figsize=(16, 8))
    
    for category in categories:
        plt.plot(dataRTE['Date'], dataRTE[category], label=category)
    
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Consommation (MW)', fontsize=14)
    plt.title('Évolution de la consommation annuelle par catégorie', fontsize=16)
    plt.legend(title='Catégories', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def matriceplots(data):
    """
    Crée une matrice de graphiques pairplot pour visualiser les relations entre les variables.
    
    Parameters:
    data (pd.DataFrame): Le jeu de données à analyser.
    
    Returns:
    sns.PairGrid: L'objet PairGrid de Seaborn.
    """
    mat = sns.PairGrid(data)  # Création de la grille de paires avec Seaborn
    mat.map_diag(sns.histplot)  # Ajout des histogrammes sur la diagonale
    mat.map_offdiag(sns.scatterplot, s=1)  # Ajout des scatter plots sur les éléments hors diagonale avec une taille de point ajustée
    mat.add_legend()
    plt.show()
    return mat 

def histogramme(data):
    """
    Affiche les histogrammes pour toutes les colonnes numériques du jeu de données.
    
    Parameters:
    data (pd.DataFrame): Le jeu de données à analyser.
    
    Returns:
    None
    """
    num_cols = data.select_dtypes(include=['number']).columns
    data[num_cols].hist(bins=15, figsize=(15, 10), layout=(5, 4))
    plt.suptitle('Histogramme des colonnes')
    plt.show()

def mat_correlation(data):
    """
    Affiche une carte de chaleur de la matrice de corrélation.
    
    Parameters:
    data (pd.DataFrame): Le jeu de données à analyser.
    
    Returns:
    None
    """
    # Sélectionner uniquement les colonnes numériques
    num_cols = data.select_dtypes(include=['number']).columns
    corr_matrix = data[num_cols].corr()
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='pink', linewidths=0.5)
    plt.title('Heatmap de la matrice de corrélation')
    plt.show()

def boxplots(data):
    """
    Affiche des boxplots pour toutes les colonnes numériques du jeu de données.
    
    Parameters:
    data (pd.DataFrame): Le jeu de données à analyser.
    
    Returns:
    None
    """
    num_cols = data.select_dtypes(include=['number']).columns
    data[num_cols].plot(kind='box', subplots=True, layout=(5, 4), figsize=(15, 10), sharex=False, sharey=False)
    plt.suptitle('Boxplots des colonnes')
    plt.show()
