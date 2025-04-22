# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router
from app.api.execute import router as execute_router
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.on_event("startup")
def check_mongo_connection():
    try:
        client = MongoClient("mongodb://mongo:27017")
        client.admin.command('ping')
        print("✅ Connected to MongoDB!")
    except ConnectionFailure as e:
        print("❌ Could not connect to MongoDB:", e)

app.include_router(chat_router, prefix="/api")
app.include_router(execute_router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
