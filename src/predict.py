import pickle
import numpy as np
from src.feature_extraction import extract_features

def load_model():
    return pickle.load(open("models/fraud_model.pkl", "rb"))

def predict_risk(raw_input):
    model = load_model()
    features = extract_features(raw_input)

    score = model.decision_function([features])[0]

    # Convert to 0–1 risk
    risk = 1 - ((score + 0.5) / 1.0)
    risk = max(0, min(1, risk))

    return round(risk, 3)