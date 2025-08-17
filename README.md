# Carbon Calculator Package Development 🌱

### Overview 🌟

This project was developed as part of the Python Programming course at Sorbonne University, between February and April 2024.
Its goal is to apply programming **concepts and statistical methods to analyze datasets and build linear models**, while also developing a **carbon footprint calculator**.

---

The project is divided into two main parts:

**1. Statistical Analysis & Linear Modeling**

**2. Carbon Footprint Calculator**

--- 

### Part 1: Statistical Analysis & Linear Modeling

#### 1.1 Dataset 📊

The dataset for this section was provided by RTE and records electricity production by energy source during the year 2020 (four entries per minute).

The main variables include:
- Date and Time
- Total consumption (MW) with day-ahead and same-day forecasts
- Production by source: fuel, coal, gas, nuclear, wind, solar, etc. (MW)
- Imports/exports (MW)
- Estimated CO₂ emissions (g/kWh)

#### 1.2 Statistical Analysis & Visualization

Implemented in `statistics.py` and `visualisation.py`.

- Descriptive statistics for numerical variables
- Correlation analysis between variables
- Multiple visualization tools (heatmaps, histograms, scatter matrices, trend plots, etc.)

#### 1.3 Ordinary Least Squares

A linear regression model is built to explain CO₂ emissions based on selected covariates.
The method is implemented in the `OrdinaryLeastSquares` class, with the following methods:

- `fit` : Fits the OLS estimator β̂ from input data,
- `predict` : Predicts outcomes for test data,
- `get_coeffs` : Returns estimated coefficients,
- `determination_coefficient` : Computes and returns R².

### Pipeline ⚙️

#### - `main.py`

Main entry point of the project. 

Handles:
- Data loading and preprocessing,
- Statistical analysis,
- Visualization of results.

Functions:
- `convertir_frequence(consommation, frequence)` : Converts consumption to annual values.
- `main()` : Orchestrates the workflow.


#### - `statistics.py`

This module contains the following functions for statistical analysis:

- `stats_des(data)` : Prints descriptive statistics of all numerical columns of the dataset.
- `variance(data)` : Prints the variance of all numerical columns of the dataset.
- `covariance(data)` : Prints covariance matrix of all numerical columns of the dataset.
- `correlation(data)` : Prints correlation matrix of all numerical columns of the dataset.
- `matrice_correlation(data)` : Prints Correlation heatmap.
- `table_de_contingence_multi(data, cols, aggfunc='size')` : Creates and displays Multi-variable contingency tables.
- `categorize_column(data, column, bins, labels)` : Categorizes numeric columns.

#### - `visualisation.py`

This module contains the following functions for data visualization:

- `calculate_consumption_sums(df, categories)` : Computes the Sum of consumption per category.
- `plot_pie_chart(data, title)` : Plots Pie chart visualization based on provided data.
- `plot_consumption_trends(dataRTE, categories)` : Plots Annual consumption trends per category in the same plot.
- `matriceplots(data)` : Creates a Pairplot of variables to visualize relations between variables.
- `histogramme(data)` : Plots Histograms for numerical columns.
- `mat_correlation(data)` : Correlation heatmap.
- `boxplots(data)` : Boxplots for numeric columns.


---

### Part 2: Carbon Footprint Calculator 🌍

#### 2.1 Dataset 📊

The dataset comes from a carbon database, containing CO₂ emission factors by consumption category.

#### 2.2 Objectives

The calculator is designed to:
- Compute total CO₂ emissions based on user consumption data,
- Display results interactively,
- Break down emissions by category.

### Modules & Classes

#### - Module `CalcuCarbone.py`

**Class `CarbonCalculator`**:
- `__init__(self, data)`: Initializes calculator with a pandas.DataFrame.
- `calculer_emissions(self, consommations)`: Computes CO₂ emissions based on the given consumption data. The parameter `consommations` is a dictionary containing consumption values by category. The function returns a dictionary of emissions per category.
- `convertir_frequence(consommation, frequence)`: Converts consumption into annual consumption. The parameter frequence should be set to 'q' for daily, 'h' for weekly, 'm' for monthly, or 'a' for annual.
- `afficher_resultats(self, consommations)`: Displays the CO₂ emissions results. The parameter `consommations` is a dictionary containing consumption values by category.
- `calculer_emissions_par_categorie(self, consommations, categories)`: Computes CO₂ emissions by category based on the given consumption data. The parameter `categories` is a dictionary of categories and subcategories. The function returns a dictionary of emissions per category.

#### - Module `main.py`

**Function `main()`**:
This is the main function that runs the different methods of the project. It reads the CSV files containing the data, initializes the carbon footprint calculator, prompts the user for their annual consumption by category, computes and displays the CO₂ emissions results, and generates a chart of emissions by category.


#### - Module `loading.py`

**Function `lecture2(fichier)`**:
This function loads the CSV file and returns a `pandas.DataFrame` containing the data. The parameter `fichier` is the path to the CSV file. The function also handles missing values by replacing them with default values (0 for numeric fields and empty strings for text fields).

--- 

### Installation & Usage 🔧

1. Clone the repository:

```bash
git clone <https://github.com/erivaninan/Package-Development>
cd <Package-Development>
pip install -r requirements.txt
python main.py
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the main program:

```bash
python main.py
```

4. Enter your annual consumption values by category.

5. View results and visualizations of CO₂ emissions per category.

*If results seem inconsistent with reality, check the folder `exemple_application/` for examples of input values (.txt) and corresponding output plots (.png).*

---

This project demonstrates the integration of statistical modeling and sustainability applications, bridging energy data analysis with a practical carbon footprint calculator.
