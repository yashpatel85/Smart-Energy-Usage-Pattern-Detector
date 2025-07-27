# predict.py
import joblib
import pandas as pd

# Load model
model = joblib.load('D:/ML Projects/Smart Energy Usage Pattern Detector/models/isolation_forest.pkl')

def detect_anomalies(df):
    preds = model.predict(df)
    scores = model.decision_function(df)
    df['anomaly'] = preds
    df['anomaly_score'] = scores
    return df
