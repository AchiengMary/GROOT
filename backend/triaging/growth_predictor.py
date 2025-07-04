def predict_growth(data: dict) -> float:
    # Dummy prediction logic
    return round(data.get("cyst_size", 3.2) + data.get("growth_rate", 0.5), 2)
