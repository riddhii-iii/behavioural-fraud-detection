from flask import Flask, request, jsonify
import os

app = Flask(__name__)

model = None

@app.route("/")
def home():
    return "Server Running"

@app.route("/predict", methods=["POST"])
def predict():
    global model

    if model is None:
        return jsonify({"error": "Model not loaded yet"}), 500

    return jsonify({"message": "Predict working"})