# app/services/mongo_service.py
from motor.motor_asyncio import AsyncIOMotorClient
from app.utils.config import MONGO_URI, MONGO_DB_NAME

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]

async def save_code_execution_data(file_name: str, code: str, result: str):
    collection = db['executions']
    document = {
        'file_name': file_name,
        'code': code,
        'result': result,
    }
    result = await collection.insert_one(document)
    return str(result.inserted_id)

async def get_code_executions():
    collection = db['executions']
    return await collection.find().to_list(length=100)