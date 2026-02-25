

import pandas as pd
import numpy as np
import random
import os
os.makedirs("data", exist_ok=True)

def generate_data(samples=1000):
    data = []

    for _ in range(samples):
        avg_key_hold = np.random.normal(0.15, 0.05)
        typing_speed = np.random.normal(4, 1)
        mouse_speed = np.random.normal(150, 50)
        click_rate = np.random.normal(1, 0.5)
        session_duration = np.random.normal(8, 2)

        # Fraud logic (simulated pattern)
        fraud = 1 if typing_speed < 2 or mouse_speed > 300 else 0

        data.append([
            avg_key_hold,
            typing_speed,
            mouse_speed,
            click_rate,
            session_duration,
            fraud
        ])

    columns = [
        "avg_key_hold",
        "typing_speed",
        "mouse_speed",
        "click_rate",
        "session_duration",
        "fraud"
    ]

    df = pd.DataFrame(data, columns=columns)
    df.to_csv("data/behavioural_data.csv", index=False)
    print("Dataset generated successfully!")

if __name__ == "__main__":
    generate_data()