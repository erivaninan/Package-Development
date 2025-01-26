# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:15:17

Module général d'exécution des différentes fonctions et méthodes.
"""

# Importation des librairies
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importation des modules
from part2.CalcuCarbone import CarbonCalculator
from part2.loading import lecture2

def main():
    # Lecture des fichiers CSV
    fichier1 = "basecarbone_sample.csv"
    fichier2 = "basecarbone-v17-fr.csv"
    data_sample = loading.lecture2(fichier1)
    data_full = loading.lecture2(fichier2)

    # Merge des deux fichiers pour enrichir les données
    data = pd.concat([data_sample, data_full], ignore_index=True).drop_duplicates()

    # Vérifie la présence des colonnes nécessaires
    required_columns = ['Nom base français', 'Unité français', 'Total poste non décomposé']
    for col in required_columns:
        if col not in data.columns:
            raise KeyError(f"La colonne '{col}' est manquante dans les données.")

    # Initialisation du calculateur
    calculator = CarbonCalculator(data)

    # Définit les catégories et leurs sous-catégories
    categories = {
        'Transports': {
            'Avion': 'km parcourus',
            'Métro': 'km parcourus',
            'RER': 'km parcourus',
            'TGV': 'km parcourus',
            'Voiture': 'km parcourus',
            'Bus': 'km parcourus'
        },
        'Logement': {
            'Fioul': 'litres',
            'Gaz': 'm³',
            'Électricité': 'kWh'
        },
        'Alimentation': {
            'Repas': 'nombre',
            'Viande de boeuf': 'kg',
            'Légumes': 'kg'
        },
        'Électronique': {
            'Tablette': 'unités',
            'Smartphone': 'unités'
        }
    }

    # Demande à l'utilisateur sa consommation annuelle par catégorie
    consommations = {}
    print("Veuillez entrer votre consommation pour les différentes sous-catégories (spécifiez la fréquence : Q pour quotidienne, H pour hebdomadaire, M pour mensuelle, A pour annuelle) :")
    for category, subcategories in categories.items():
        print(f"\nCatégorie : {category}")
        for subcat, unit in subcategories.items():
            try:
                consommation = float(input(f"{subcat} (en {unit}) : "))
                frequence = input(f"Spécifiez la fréquence (Q/H/M/A) pour {subcat} : ").strip().lower()
                consommation_an = CarbonCalculator.convertir_frequence(consommation, frequence)
                consommations[subcat] = consommation_an
            except ValueError:
                consommations[subcat] = 0.0

    # Calcule et affiche les résultats
    calculator.afficher_resultats(consommations)

    # Calcule les émissions par catégorie
    emissions_by_category = calculator.calculer_emissions_par_categorie(consommations, categories)

    # Crée un DataFrame pour les émissions par catégorie
    emissions_df = pd.DataFrame.from_dict(emissions_by_category, orient='index', columns=['Emissions'])
    emissions_df = emissions_df.sort_values(by='Emissions', ascending=False)

    # Crée le graphique
    palette_couleurs = sns.color_palette(["#FFB6C1", "#ADD8E6", "#90EE90", "#FFD700"])  # rose clair, bleu clair, vert clair, doré
    plt.figure(figsize=(10, 6))
    sns.barplot(x=emissions_df.index, y='Emissions', data=emissions_df, palette=palette_couleurs)
    plt.xlabel('Catégories')
    plt.ylabel('Emissions de CO2 (kg)')
    plt.title('Emissions de CO2 par Catégorie')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
