from fastapi import FastAPI
from auth.routes import router as auth_router
from triaging.routes import router as triaging_router
from llm import router as chatbot_router

app = FastAPI(title="Ovarian Cyst AI Platform")

# Routers
app.include_router(auth_router, prefix="/auth")
app.include_router(triaging_router, prefix="/triage")
app.include_router(chatbot_router, prefix="/chat")

@app.get("/")
def root():
    return {"message": "Welcome to the AI platform for Ovarian Cyst Management"}
