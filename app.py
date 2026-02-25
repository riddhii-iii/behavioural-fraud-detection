from flask import Flask, request, jsonify, render_template
import os
import pickle
import numpy as np

app = Flask(__name__)

model = None

def load_model():
    global model
    if model is None:
        if not os.path.exists("models/fraud_model.pkl"):
            raise Exception("Model file not found.")
        with open("models/fraud_model.pkl", "rb") as f:
            model = pickle.load(f)
    return model

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        model = load_model()

        features = np.array([[
            data["avg_key_hold"],
            data["typing_speed"],
            data["mouse_speed"],
            data["click_rate"],
            data["session_duration"]
        ]])

        score = model.decision_function(features)[0]

        risk = 1 - ((score + 0.5) / 1.0)
        risk = max(0, min(1, risk))

        return jsonify({
            "risk_score": round(risk, 3),
            "prediction": "High Risk ⚠️" if risk > 0.7 else "Low Risk ✅"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500