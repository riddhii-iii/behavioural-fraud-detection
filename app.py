from flask import Flask, request, jsonify, render_template
import os
from src.data_collection import generate_data
from src.model_training import train_model
from src.predict import predict_risk

app = Flask(__name__)

# Always regenerate dataset + retrain
if not os.path.exists("data/behavioural_data.csv"):
    generate_data(1000)

train_model()

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        risk_score = predict_risk(data)

        return jsonify({
            "risk_score": risk_score,
            "prediction": "High Risk ⚠️" if risk_score > 0.7 else "Low Risk ✅"
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)