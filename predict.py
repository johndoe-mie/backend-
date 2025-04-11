# backend/predict.py

import pandas as pd
import pickle

def predict_rainfall_for_year(year):
    months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    predictions = {}
    for month in months:
        with open(f"models/model_{month}.pkl", "rb") as f:
            model = pickle.load(f)
            pred = model.predict([[year]])[0]
            predictions[month] = round(pred, 2)
    return predictions
