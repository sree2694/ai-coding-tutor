from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import router
from dotenv import load_dotenv
import os

app = FastAPI(title="AI Code Editor & Chatbot")

load_dotenv()  # take environment variables from .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Allow cross-origin requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Frontend will be on localhost or similar, adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all router endpoints (from chatbot and code execution)
app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Code Editor & Chatbot API"}
