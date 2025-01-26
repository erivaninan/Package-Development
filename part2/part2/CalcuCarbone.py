# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 13:21:55

Module d'exécution des différentes fonctions et méthodes
pour le calcul de l'empreinte carbone.
"""

import pandas as pd

class CarbonCalculator:
    def __init__(self, data):
        """
        Initialise le calculateur d'empreinte carbone avec les données fournies.
        
        Parameters:
        data (pd.DataFrame): Le DataFrame contenant les données d'émission de CO2.
        """
        self.data = data

    def calculer_emissions(self, consommations):
        """
        Calcule les émissions de CO2 en fonction des consommations données.
        Parameters:
        consommations (dict): Dictionnaire contenant les consommations par poste.
        Returns:
        dict: Dictionnaire des émissions par catégorie.
        """
        emissions = {cat: 0 for cat in consommations}
        for poste, consommation in consommations.items():
            if poste in self.data['Nom base français'].values:
                emission_par_unite = self.data.loc[self.data['Nom base français'] == poste, 'Total poste non décomposé'].values
                if len(emission_par_unite) > 0:
                    emissions[poste] = consommation * emission_par_unite[0]
        return emissions

    def convertir_frequence(consommation, frequence):
        """Convertir la consommation en consommation annuelle."""
        if frequence == 'q':
            return consommation * 365
        elif frequence == 'h':
            return consommation * 52
        elif frequence == 'm':
            return consommation * 12
        elif frequence == 'a':
            return consommation
        else:
            return consommation
    
    def afficher_resultats(self, consommations):
        """
        Affiche les résultats des émissions de CO2.
        Parameters:
        consommations (dict): Dictionnaire contenant les consommations par poste.
        """
        emissions = self.calculer_emissions(consommations)
        total_emissions = sum(emissions.values())
        print(f"\nTotal annuel des émissions de CO2 : {total_emissions:.2f} kg CO2eq")
        for poste, emission in emissions.items():
            print(f"{poste} : {emission:.2f} kg CO2eq")

    def calculer_emissions_par_categorie(self, consommations, categories):
        """
        Calcule les émissions de CO2 par catégorie en fonction des consommations données.

        Parameters:
        consommations (dict): Dictionnaire contenant les consommations par poste.
        categories (dict): Dictionnaire des catégories et sous-catégories.

        Returns:
        dict: Dictionnaire des émissions par catégorie.
        """
        emissions = self.calculer_emissions(consommations)
    
        emissions_by_category = {cat: 0 for cat in categories}

        for poste, emission in emissions.items():
            found = False
            for cat, subcats in categories.items():
                if poste in subcats:
                    emissions_by_category[cat] += emission
                    found = True
                    break
            if not found:
                print(f"Poste de consommation non trouvé dans les catégories : {poste}")
    
        return emissions_by_category
