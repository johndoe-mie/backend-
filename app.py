from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import os
from predict import predict_rainfall_for_year

app = Flask(__name__)
CORS(app, origins="*")  # ← allows frontend on another domain to access this API

@app.route("/")
def home():
    return jsonify({"message": "ML Weather API is live!"})

df = pd.read_excel("chennai-monthly-rains.xlsx")
df.set_index("Year", inplace=True)

@app.route("/predict", methods=["GET"])
def predict():
    past_year = int(request.args.get("year", 2023))
    
    predicted_2025 = predict_rainfall_for_year(2025)

    if past_year in df.index:
        past_data = df.loc[past_year].to_dict()
    else:
        return jsonify({"error": "Year not found"}), 404

    return jsonify({
        "predicted_2025": predicted_2025,
        "past_year": past_year,
        "past_data": past_data
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=True, host="0.0.0.0", port=port)
