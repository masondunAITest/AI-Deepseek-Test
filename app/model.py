import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Sample pre-trained model (replace with your real training data)
class ValuationModel:
    def __init__(self):
        # Mock trained model - REPLACE WITH YOUR ACTUAL TRAINING CODE
        self.model = RandomForestRegressor()
        X_train = np.array([[1, 50, 100000], [2, 30, 50000]])  # [years_in_business, employees, revenue]
        y_train = np.array([500000, 200000])  # Valuation in USD
        self.model.fit(X_train, y_train)
    
    def predict(self, years, employees, revenue):
        """Predict business valuation in USD"""
        features = [[years, employees, revenue]]
        return self.model.predict(features)[0]
