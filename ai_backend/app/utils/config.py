import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()  # Load environment variables from .env file

# Get the values from the environment
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]

async def get_collection(collection_name):
    return db[collection_name]