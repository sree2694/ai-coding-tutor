# app/api/chat.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.openai_service import get_chat_response

router = APIRouter()

class ChatRequest(BaseModel):
    question: str
    code: str

@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        prompt = f"You are a coding tutor helping a student. The student's code is:\n{request.code}\n\nQuestion: {request.question}\nGive a helpful answer."
        response = get_chat_response(prompt, model="gpt-3.5-turbo")
        return {"reply": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))