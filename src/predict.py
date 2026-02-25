import pickle
from src.feature_extraction import extract_features

with open("models/fraud_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_risk(raw_input):
    features = extract_features(raw_input)
    score = model.decision_function([features])[0]

    risk = 1 - ((score + 0.5) / 1.0)
    risk = max(0, min(1, risk))

    return round(risk, 3)