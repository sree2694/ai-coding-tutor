from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import subprocess
from app.services.mongo_service import save_code_execution_data
from app.services.openai_service import get_chat_response

router = APIRouter()

class CodeRequest(BaseModel):
    code: str
    language: str

@router.post("/execute")
async def execute_code(req: CodeRequest):
    try:
        # You can extend this for real Dockerized execution
        if req.language == "python":
            exec_result = subprocess.run(
                ["python3", "-c", req.code],
                capture_output=True,
                text=True,
                timeout=5
            )
            return {"output": exec_result.stdout or exec_result.stderr}
        else:
            return {"output": f"Language {req.language} not supported yet."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/run_code")
async def run_code(file_name: str, code: str):
    # Simulate code execution here
    result = "Execution result goes here"  # Replace with actual execution logic
    
    # Save code execution result to MongoDB
    document_id = save_code_execution_data(file_name, code, result)
    
    return {"status": "success", "document_id": document_id, "result": result}

@router.post("/chat")
async def chat_with_ai(message: str):
    # Get AI response
    response = get_chat_response(message)
    return {"status": "success", "response": response}
