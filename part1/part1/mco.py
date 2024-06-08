import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class OrdinaryLeastSquares:
    def __init__(self, intercept=True):
        self.intercept = intercept
        self.coeffs = None
    
    def fit(self, X, y):
        if isinstance(X, pd.DataFrame):
            X = X.values
        if isinstance(y, pd.Series):
            y = y.values
        
        # Ajout de l'intercept si nécessaire
        if self.intercept:
            X = np.hstack((np.ones((X.shape[0], 1)), X))
        
        # Calcul de l'estimateur des moindres carrés
        XtX = np.dot(X.T, X)
        XtX_inv = np.linalg.inv(XtX)
        XtY = np.dot(X.T, y)
        self.coeffs = np.dot(XtX_inv, XtY)
    
    def predict(self, X):
        if isinstance(X, pd.DataFrame):
            X = X.values
        
        # Ajout de l'intercept si nécessaire
        if self.intercept:
            X = np.hstack((np.ones((X.shape[0], 1)), X))
        
        return np.dot(X, self.coeffs)
    
    def get_coeffs(self):
        return self.coeffs
    
    def determination_coefficient(self, X, y):
        y_pred = self.predict(X)
        ss_total = np.sum((y - np.mean(y))**2)
        ss_residual = np.sum((y - y_pred)**2)
        r2 = 1 - (ss_residual / ss_total)
        return r2

    def visualise_result(self, X, y):
        """
        Visualise the results of the model predictions versus the actual values.

        :param X: The input features for prediction.
        :param y: The actual target values.
        """
        if isinstance(X, pd.DataFrame):
            X = X.values
        if isinstance(y, pd.Series):
            y = y.values

        y_pred = self.predict(X)

        plt.figure(figsize=(10, 6))
        plt.scatter(range(len(y)), y, color='black', label='Données réelles', s=1)    # Tracer les données réelles
        plt.plot(range(len(y_pred)), y_pred, color='pink', label='Ligne de régression', linewidth=1)     # Tracer les prédictions
        plt.title("Représentation du modèle")
        plt.xlabel("Index")
        plt.ylabel("Valeur de y")
        plt.legend()
        plt.show()