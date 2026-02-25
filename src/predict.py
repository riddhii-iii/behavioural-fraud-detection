import os
import pickle
from src.feature_extraction import extract_features

MODEL_PATH = "models/fraud_model.pkl"

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model file not found. Train model first.")
    return pickle.load(open(MODEL_PATH, "rb"))

def predict_risk(raw_input):
    model = load_model()
    features = extract_features(raw_input)

    score = model.decision_function([features])[0]

    risk = 1 - ((score + 0.5) / 1.0)
    risk = max(0, min(1, risk))

    return round(risk, 3)