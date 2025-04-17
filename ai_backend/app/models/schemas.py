from pydantic import BaseModel

# Schema for the code execution request
class CodeExecutionRequest(BaseModel):
    language: str  # e.g., 'python', 'javascript'
    code: str       # Code that needs to be executed
    input: str = "" # Optional input for the code execution

# Schema for the code execution response
class CodeExecutionResponse(BaseModel):
    output: str  # The output of the code execution
    error: str = ""  # Any error that occurred during code execution

# Schema for the chatbot request
class ChatRequest(BaseModel):
    message: str  # User's message to the chatbot

# Schema for the chatbot response
class ChatResponse(BaseModel):
    reply: str  # AI-generated reply
