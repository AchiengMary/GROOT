from fastapi import APIRouter
from triaging.growth_predictor import predict_growth
from triaging.treatment_recommender import recommend_treatment

router = APIRouter()

@router.post("/growth")
def growth(payload: dict):
    prediction = predict_growth(payload)
    return {"predicted_growth": prediction}

@router.post("/recommendation")
def recommend(payload: dict):
    recommendation = recommend_treatment(payload)
    return {"treatment": recommendation}
