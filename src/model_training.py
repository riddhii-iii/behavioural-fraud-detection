from sklearn.ensemble import IsolationForest
import pandas as pd
import pickle

def train_model():
    df = pd.read_csv("data/behavioural_data.csv")
    X = df.drop("fraud", axis=1)

    model = IsolationForest(contamination=0.1)
    model.fit(X)

    pickle.dump(model, open("models/fraud_model.pkl", "wb"))
    print("Anomaly model saved!")