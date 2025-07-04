from fastapi import APIRouter
from triaging.growth_predictor import predict_growth
from triaging.treatment_recommender import recommend_treatment

router = APIRouter()

@router.post("/growth")
def get_growth_prediction(payload: dict):
    return {"predicted_size_next_month": predict_growth(payload)}

@router.post("/treatment")
def get_treatment_plan(payload: dict):
    return {"recommended_plan": recommend_treatment(payload)}

