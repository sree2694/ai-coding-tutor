# app/utils/config.py
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "default_db")

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]

def get_collection(collection_name):
    return db[collection_name]