import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_ai_response(message: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or your preferred model
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"
