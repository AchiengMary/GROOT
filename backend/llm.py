from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def chatbot(payload: dict):
    q = payload.get("question", "")
    return {"response": f"Sorry, I don't understand '{q}' yet — try rephrasing!"}
