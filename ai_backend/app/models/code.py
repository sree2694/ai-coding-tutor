from pydantic import BaseModel

class CodeExecution(BaseModel):
    file_name: str
    code: str
    result: str
