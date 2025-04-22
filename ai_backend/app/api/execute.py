# app/api/execute.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.mongo_service import save_code_execution_data
from docker_runner.executor import run_python_code
import subprocess

router = APIRouter()

class CodeRequest(BaseModel):
    code: str
    language: str
    file_name: str = "code.py"

@router.post("/execute/inline")
async def execute_inline(req: CodeRequest):
    try:
        if req.language.lower() == "python":
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

@router.post("/execute/save")
async def execute_and_save(req: CodeRequest):
    try:
        result = run_python_code(req.code)
        doc_id = save_code_execution_data(req.file_name, req.code, result)
        return {"status": "success", "document_id": doc_id, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/execute/docker")
async def execute_docker(req: CodeRequest):
    try:
        result = run_python_code(req.code)
        return {"output": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))