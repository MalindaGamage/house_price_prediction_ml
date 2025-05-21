import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import os


class HousePriceModel:
    def __init__(self):
        self.model = LinearRegression()

    def load_data(self, file_path):
        """Load house size and price data from CSV."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Data file not found at: {file_path}")
        data = pd.read_csv(file_path)
        X = data[['size_sqft']].values  # Features (house size)
        y = data['price'].values  # Target (price)
        return X, y

    def train(self, X, y):
        """Train the linear regression model."""
        self.model.fit(X, y)
        print("Model trained successfully!")

    def predict(self, size_sqft):
        """Predict price for a given house size."""
        size_array = np.array([[size_sqft]])
        predicted_price = self.model.predict(size_array)
        return predicted_price[0]

    def get_coefficients(self):
        """Return model coefficients (slope and intercept)."""
        return self.model.coef_, self.model.intercept_