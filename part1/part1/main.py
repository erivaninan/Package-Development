# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:21:32

@author: Erivan INAN

Module général d'exécution des différentes fonctions et méthodes.
"""

# Importation des librairies 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importation des modules
import loading
import statistics
import visualisation
import mco
from loading import *
from statistics import *
from visualisation import *
from mco import *
from mco import OrdinaryLeastSquares


def main():
    fichier = "eCO2mix_RTE_Annuel-Definitif_2020.csv"
    # Charger et nettoyer les données
    dataRTE = lecture2(fichier)

    # Afficher les premières lignes des données nettoyées
    print(dataRTE.head())

    print("Noms des colonnes :", dataRTE.columns)

    # Statistiques descriptives
    print('statistiques descriptives', statistics.stats_des(dataRTE))
    statistics.matrice_correlation(dataRTE)
    statistics.variance(dataRTE)
    statistics.covariance(dataRTE)
    
    # Visualisation des données
    visualisation.matriceplots(dataRTE) # /!\ cette fonction met du temps à charger 
    visualisation.histogramme(dataRTE)
    visualisation.mat_correlation(dataRTE)
    visualisation.boxplots(dataRTE)
    
    # Pie chart global
    # Catégories de production électrique
    categories = ['Fioul', 'Charbon', 'Gaz', 'Nucléaire', 'Eolien', 'Solaire', 'Hydraulique', 'Pompage', 'Bioénergies']
    
    # Sommes de consommation
    consumption_sums = visualisation.calculate_consumption_sums(dataRTE, categories)
    
    for category, value in consumption_sums.items():     # On veut que toutes les valeurs soient positives
        if value < 0:
            raise ValueError(f"La somme de la consommation pour {category} est négative: {value}")
            
    visualisation.plot_pie_chart(consumption_sums, 'Répartition de la consommation par catégorie')
        
    # Moindres carrés ordinaires 
    print("Noms des colonnes :", dataRTE.columns)
    X = dataRTE[['Fioul', 'Charbon', 'Gaz', 'Nucléaire', 'Eolien', 'Solaire']] # Variables explicatives
    y = dataRTE['Taux de Co2'] # Variable expliquée

    # Création du modèle et ajustement
    model = OrdinaryLeastSquares(intercept=True)
    model.fit(X, y)
    
    # Affichage des coefficients
    print("Coefficients estimés :", model.get_coeffs())
    
    # Prédictions
    y_pred = model.predict(X)
    print("Prédictions :", y_pred)
    
    # Coefficient de détermination R2
    r2 = model.determination_coefficient(X, y)
    print("Coefficient de détermination R2 :", r2)

    model.visualise_result(X, y)

if __name__ == "__main__":
    main()