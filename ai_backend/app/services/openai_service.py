# app/services/openai_service.py
import openai
from app.utils.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_chat_response(message: str, model: str = "text-davinci-003") -> str:
    try:
        if model == "gpt-3.5-turbo":
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful AI tutor for competitive coding."},
                    {"role": "user", "content": message}
                ]
            )
            return response.choices[0].message['content'].strip()
        else:
            response = openai.Completion.create(
                engine=model,
                prompt=message,
                max_tokens=150
            )
            return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        raise Exception(f"OpenAI API error: {str(e)}")
    except Exception as e:
        raise Exception(f"Unexpected error: {str(e)}")