# Développement de package 🌟


### Présentation Générale

Ce projet a été réalisé dans le cadre du cours de programmation Python à l'ISUP, Sorbonne Université, entre février et avril 2024. L'objectif du projet est d'appliquer les outils et méthodes vus en cours pour analyser des jeux de données et construire des modèles linéaires. Le projet se divise en deux parties principales :

1. Analyse statistique et modèle linéaire
2. Calculateur d'empreinte carbone

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

Le module `statistics.py` contient les fonctions suivantes pour l'analyse statistique :

- `stats_des(data)` : Affiche les statistiques descriptives de toutes les colonnes numériques du jeu de données.
- `variance(data)` : Affiche la variance de toutes les colonnes numériques du jeu de données.
- `covariance(data)` : Affiche la matrice de covariance de toutes les colonnes numériques du jeu de données.
- `correlation(data)` : Affiche la matrice de corrélation de toutes les colonnes numériques du jeu de données.
- `matrice_correlation(data)` : Affiche une matrice de corrélation sous forme de carte de chaleur.
- `table_de_contingence_multi(data, cols, aggfunc='size')` : Crée et affiche une table de contingence pour plusieurs colonnes catégorielles.
- `categorize_column(data, column, bins, labels)` : Crée une nouvelle colonne catégorisée à partir d'une colonne numérique.

#### visualisation.py

Le module `visualisation.py` contient les fonctions suivantes pour la visualisation des données :

- `calculate_consumption_sums(df, categories)` : Calcule la somme de la consommation pour chaque catégorie spécifiée.
- `plot_pie_chart(data, title)` : Affiche un graphique en secteurs basé sur les données fournies.
- `plot_consumption_trends(dataRTE, categories)` : Affiche les tendances de consommation annuelle pour chaque catégorie sur un même graphique.
- `matriceplots(data)` : Crée une matrice de graphiques pairplot pour visualiser les relations entre les variables.
- `histogramme(data)` : Affiche les histogrammes pour toutes les colonnes numériques du jeu de données.
- `mat_correlation(data)` : Affiche une carte de chaleur de la matrice de corrélation.
- `boxplots(data)` : Affiche des boxplots pour toutes les colonnes numériques du jeu de données.

### Installation et Utilisation

Pour installer et utiliser ce package, suivez les étapes ci-dessous :

1. Clonez le dépôt du projet.

```bash
git clone <https://github.com/erivaninan/Carbon-Calculator-Package>
cd <Carbon-Calculator-Package>
pip install -r requirements.txt
python main.py
```

2. Assurez-vous d'avoir Python installé sur votre machine.
3. Installez les dépendances nécessaires : `pandas`, `matplotlib`, `seaborn`.
4. Exécutez le script principal `main.py` pour lancer l'analyse et la visualisation des données.

### Partie 2 : Calculateur d'empreinte carbone

#### 2.1 Jeu de Données

Le jeu de données utilisé pour cette partie provient de la base de données carbone, contenant des informations sur les émissions de CO2 par poste de consommation.

#### 2.2 Objectifs

L'objectif de cette partie est de développer un calculateur d'empreinte carbone capable de :
- Calculer les émissions de CO2 en fonction des consommations données.
- Afficher les résultats des émissions de CO2.
- Calculer les émissions de CO2 par catégorie en fonction des consommations données.

### Modules et Fonctions

#### Module `CalcuCarbone.py`

**Classe `CarbonCalculator`**:
- `__init__(self, data)`: Initialise le calculateur d'empreinte carbone avec les données fournies. Le paramètre `data` est un `pandas.DataFrame` contenant les données d'émission de CO2.
- `calculer_emissions(self, consommations)`: Calcule les émissions de CO2 en fonction des consommations données. Le paramètre `consommations` est un dictionnaire contenant les consommations par poste. La fonction retourne un dictionnaire des émissions par catégorie.
- `convertir_frequence(consommation, frequence)`: Convertit la consommation en consommation annuelle. Complétez le paramètre `frequence` par 'q' pour quotidienne, 'h' pour hebdomadaire, 'm' pour mensuelle, ou 'a' pour annuelle.
- `afficher_resultats(self, consommations)`: Affiche les résultats des émissions de CO2. Le paramètre `consommations` est un dictionnaire contenant les consommations par poste.
- `calculer_emissions_par_categorie(self, consommations, categories)`: Calcule les émissions de CO2 par catégorie en fonction des consommations données. Le paramètre `categories` est un dictionnaire des catégories et sous-catégories. La fonction retourne un dictionnaire des émissions par catégorie.

#### Module `main.py`

**Fonction `main()`**:
- C'est la fonction principale qui exécute les différentes fonctions et méthodes du projet. Elle lit les fichiers CSV contenant les données, initialise le calculateur d'empreinte carbone, demande à l'utilisateur sa consommation annuelle par catégorie, calcule et affiche les résultats des émissions de CO2, et génère un graphique des émissions par catégorie.

#### Module `loading.py`

**Fonction `lecture2(fichier)`**:
- Cette fonction charge le fichier CSV et retourne un `pandas.DataFrame` contenant les données chargées. Le paramètre `fichier` est le chemin vers le fichier CSV. La fonction gère également les valeurs manquantes en les remplaçant par des valeurs par défaut (0 pour les valeurs numériques et des chaînes vides pour les chaînes de caractères).

### Installation et Utilisation

Pour utiliser ce calculateur d'empreinte carbone, suivez les étapes suivantes :

1. Clonez le dépôt ou téléchargez les fichiers du projet.

```bash
git clone <https://github.com/erivaninan/Carbon-Calculator-Package>
cd <Carbon-Calculator-Package>
pip install -r requirements.txt
python main.py
```

2. Installez les dépendances nécessaires listées dans le fichier `setup.py`.
3. Exécutez le module `main.py` pour démarrer le calculateur et suivre les instructions à l'écran pour entrer vos consommations annuelles par catégorie.
4. Visualisez les résultats des émissions de CO2 par catégorie.
5. En cas d'obtention de résultats non cohérents avec la réalité, voir le dossier `exemple_application` où les valeurs entrées dans chaques catégories sont précisées dans le fichier .txt et le graphique résultat joint en fichier .png 

### Auteur

Erivan INAN
