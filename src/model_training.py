import os
os.makedirs("models", exist_ok=True)

import pandas as pd
import pickle
from sklearn.ensemble import IsolationForest

def train_model():
    df = pd.read_csv("data/behavioural_data.csv")

    X = df.drop("fraud", axis=1)

    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    model.fit(X)

    with open("models/fraud_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model saved successfully!")

if __name__ == "__main__":
    train_model()