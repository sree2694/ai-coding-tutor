from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router
from app.api.execute import router as execute_router

app = FastAPI()

# Include the code and chat routes
app.include_router(chat_router, prefix="/api")
app.include_router(execute_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)