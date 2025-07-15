import joblib
import pandas as pd

model = joblib.load("triaging/models/growth_model.pkl")

def predict_growth(input_dict):
    df = pd.DataFrame([input_dict])
    return model.predict(df)[0]