# backend/api/chat.py

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
import openai
import os

router = APIRouter()

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    question: str
    code: str

@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        prompt = f"You are a coding tutor helping a student. The student's code is:\n{request.code}\n\nQuestion: {request.question}\nGive a helpful answer."

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI tutor for competitive coding."},
                {"role": "user", "content": prompt}
            ]
        )

        return {"reply": response.choices[0].message['content'].strip()}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
