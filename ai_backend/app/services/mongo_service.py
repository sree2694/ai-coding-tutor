from pymongo import MongoClient
from app.utils.config import MONGO_URI, MONGO_DB_NAME

# Create a MongoDB client
client = MongoClient(MONGO_URI)

# Access the database
db = client[MONGO_DB_NAME]

def save_code_execution_data(file_name: str, code: str, result: str):
    collection = db['executions']
    document = {
        'file_name': file_name,
        'code': code,
        'result': result,
    }
    result = collection.insert_one(document)
    return str(result.inserted_id)

def get_code_executions():
    collection = db['executions']
    return list(collection.find())
