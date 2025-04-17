from fastapi import APIRouter
from app.models.schemas import CodeExecutionRequest, CodeExecutionResponse
from app.services.code_runner import execute_code

router = APIRouter()

@router.post("/run-code", response_model=CodeExecutionResponse)
def run_code(req: CodeExecutionRequest):
    """
    Endpoint to execute user code.
    It will take the language and code and return the output or error.
    """
    response = execute_code(req.language, req.code, req.input)
    return response
