# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:23:55

Module d'importation et de nettoyage des données.
"""

import pandas as pd 

def lecture2(fichier):
    """
    Charge le fichier CSV et retourne un DataFrame.
    
    Parameters:
    fichier (str): Le chemin vers le fichier CSV.
    
    Returns:
    pd.DataFrame: Le DataFrame contenant les données chargées.
    """  
    data = pd.read_csv(fichier, sep=';')
        
    if data.shape[1] == 1:  # Si une seule colonne est détectée, essayer avec un autre séparateur
        data = pd.read_csv(fichier, sep=',', skipinitialspace=True)
        
    # Remplacer les valeurs numériques manquantes par 0
    num_cols = data.select_dtypes(include=['number']).columns
    data[num_cols] = data[num_cols].fillna(0)
        
    # Remplacer les valeurs str manquantes par des chaînes de caractères vides
    str_cols = data.select_dtypes(include=['object']).columns
    data[str_cols] = data[str_cols].fillna('')
    print(data.head())
        
    return data
