def recommend_treatment(data: dict) -> str:
    if data.get("CA_125_Level", 0) > 35 or data.get("cyst_size", 0) > 5:
        return "Consider surgical removal"
    return "Monitor and follow-up"
