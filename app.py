from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
from predict import predict_rainfall_for_year

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # ✅ this works reliably

@app.route("/")
def home():
    return jsonify({"message": "ML Weather API is live"})

df = pd.read_excel("chennai-monthly-rains.xlsx")
df.set_index("Year", inplace=True)

@app.route("/predict", methods=["GET"])
def predict():
    try:
        past_year = int(request.args.get("year", 2010))
        predicted_2025 = predict_rainfall_for_year(2025)

        if past_year in df.index:
            past_data = df.loc[past_year].to_dict()
        else:
            return jsonify({"error": "Year not found"}), 404

        return jsonify({
            "past_year": past_year,
            "past_data": past_data,
            "predicted_2025": predicted_2025
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
