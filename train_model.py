# backend/train_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

# Load data
df = pd.read_excel(r"chennai-monthly-rains.xlsx")

# Remove rows with all zeros or missing values
df.dropna(inplace=True)

# Prepare models folder
os.makedirs("models", exist_ok=True)

# Train model for each month
months = df.columns[1:-1]  # Exclude 'Year' and 'Total'

for month in months:
    X = df[["Year"]]
    y = df[month]
    
    model = LinearRegression()
    model.fit(X, y)

    # Save model
    with open(f"models/model_{month}.pkl", "wb") as f:
        pickle.dump(model, f)

print("✅ All monthly models trained and saved!")
