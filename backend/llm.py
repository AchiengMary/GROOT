from fastapi import APIRouter
from pinecone_db.query import query_pinecone

router = APIRouter()

@router.post("/")
def chat(payload: dict):
    question = payload.get("question")
    if not question:
        return {"response": "Please ask a valid question."}
    result = query_pinecone(question)
    return {"response": result}
