from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
