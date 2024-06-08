# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:21:32

Module de lecture des données 
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def lecture2(fichier):
    """
    Nettoie les données en gérant les valeurs manquantes (NaN).
    Remplace par 0 les valeurs manquantes pour les variables numériques 
    et par des chaînes de caractères vides pour les variables de type chaîne.

    :param fichier: Chemin vers le fichier CSV.
    :return: DataFrame nettoyé.
    """    
    data = pd.read_csv(fichier, sep=';')
        
    # Remplacer les valeurs numériques manquantes par 0
    num_cols = data.select_dtypes(include=['number']).columns
    data[num_cols] = data[num_cols].fillna(0)
        
    # Remplacer les valeurs str manquantes par des chaînes de caractères vides
    str_cols = data.select_dtypes(include=['object']).columns
    data[str_cols] = data[str_cols].fillna('')
    print(data.head())
        
    return data
