from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.ai_chat import get_ai_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat_with_ai(req: ChatRequest):
    """
    Endpoint to communicate with the AI chatbot.
    It will take the user's message and respond with AI-generated text.
    """
    reply = get_ai_response(req.message)
    return ChatResponse(reply=reply)
