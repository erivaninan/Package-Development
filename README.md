# README


### Présentation Générale

Ce projet a été réalisé dans le cadre du cours de programmation Python à l'ISUP, Sorbonne Université, entre février et avril 2024. L'objectif du projet est d'appliquer les outils et méthodes vus en cours pour analyser des jeux de données et construire des modèles linéaires. Le projet se divise en deux parties principales :

1. Analyse statistique et modèle linéaire
2. Calculateur d'empreinte carbone

Ce document se concentre sur la partie 1 : analyse statistique et modèle linéaire.

### Partie 1 : Analyse Statistique et Modèle Linéaire

#### 1.1 Jeu de Données

Les données utilisées pour cette partie proviennent de la société RTE et enregistrent la quantité d’électricité produite pour chaque filière du mix énergétique durant l’année 2020 (quatre enregistrements par minute). Les colonnes principales incluent :

- Date et Heure
- Consommation totale en MW, avec prévisions à J-1 et à J
- Production de fioul, charbon, gaz, nucléaire, éolien, solaire, etc. en MW
- Importation/exportations en MW
- Estimation des émissions de CO2 en g/kWh

#### 1.2 Analyse Statistique et Visualisation

Les fonctions pour l'analyse statistique et la visualisation des données sont implémentées dans les modules `statistics.py` et `visualisation.py`. Les principales fonctionnalités incluent :

- Statistiques descriptives pour analyser et comparer les enregistrements numériques
- Analyse de corrélation entre les différentes variables
- Visualisation des données sous forme de graphiques divers

#### 1.3 Moindres Carrés Ordinaires

Un modèle linéaire est construit pour expliquer le taux d'émission de CO2 en fonction de certaines covariables du jeu de données. La méthode des moindres carrés ordinaires est implémentée dans une classe `OrdinaryLeastSquares` avec les méthodes suivantes :

- `fit` : Prend des données `X` et `y` en entrée et calcule l'estimateur des moindres carrés β̂.
- `predict` : Prend des données de test `Xt` et renvoie les prédictions associées.
- `get_coeffs` : Retourne les valeurs des coefficients estimés.
- `determination_coefficient` : Calcule et renvoie le coefficient de détermination R².

### Organisation du Code

#### main.py

Le module `main.py` est le point d'entrée principal du programme. Il exécute les fonctions nécessaires pour lire les données, effectuer des analyses et visualiser les résultats. Voici un aperçu des principales fonctions :

- `convertir_frequence(consommation, frequence)` : Convertit la consommation en consommation annuelle.
- `main()` : Fonction principale pour l'exécution du programme.

#### statistics.py

Le module `statistics.py` contient des fonctions pour l'analyse statistique :

- `stats_des(data)` : Affiche les statistiques descriptives de toutes les colonnes numériques du jeu de données.
- `variance(data)` : Affiche la variance de toutes les colonnes numériques du jeu de données.
- `covariance(data)` : Affiche la matrice de covariance de toutes les colonnes numériques du jeu de données.
- `correlation(data)` : Affiche la matrice de corrélation de toutes les colonnes numériques du jeu de données.
- `matrice_correlation(data)` : Affiche une matrice de corrélation sous forme de carte de chaleur.
- `table_de_contingence_multi(data, cols, aggfunc='size')` : Crée et affiche une table de contingence pour plusieurs colonnes catégorielles.
- `categorize_column(data, column, bins, labels)` : Crée une nouvelle colonne catégorisée à partir d'une colonne numérique.

#### visualisation.py

Le module `visualisation.py` contient des fonctions pour la visualisation des données :

- `calculate_consumption_sums(df, categories)` : Calcule la somme de la consommation pour chaque catégorie spécifiée.
- `plot_pie_chart(data, title)` : Affiche un graphique en secteurs basé sur les données fournies.
- `plot_consumption_trends(dataRTE, categories)` : Affiche les tendances de consommation annuelle pour chaque catégorie sur un même graphique.
- `matriceplots(data)` : Crée une matrice de graphiques pairplot pour visualiser les relations entre les variables.
- `histogramme(data)` : Affiche les histogrammes pour toutes les colonnes numériques du jeu de données.
- `mat_correlation(data)` : Affiche une carte de chaleur de la matrice de corrélation.
- `boxplots(data)` : Affiche des boxplots pour toutes les colonnes numériques du jeu de données.

### Installation et Utilisation

Pour installer et utiliser ce projet, suivez les étapes ci-dessous :

1. Clonez le dépôt du projet.
2. Assurez-vous d'avoir Python installé sur votre machine.
3. Installez les dépendances nécessaires : `pandas`, `matplotlib`, `seaborn`.
4. Exécutez le script principal `main.py` pour lancer l'analyse et la visualisation des données.

### Auteur

Erivan INAN

```bash
git clone <https://github.com/erivaninan/Linear-Model-Package>
cd <Linear-model-Package>
pip install -r requirements.txt
python main.py

