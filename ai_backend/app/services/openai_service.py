import openai
from app.utils.config import OPENAI_API_KEY

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

def get_chat_response(message: str) -> str:
    """
    Send the user's message to the OpenAI API and get a response.
    """
    try:
        # Call OpenAI's GPT model
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose the appropriate model
            prompt=message,
            max_tokens=150  # Set the token limit for the response
        )
        
        # Return the AI's response
        return response.choices[0].text.strip()
    
    except openai.error.OpenAIError as e:
        # If there's an error with OpenAI API, raise a specific error
        raise Exception(f"OpenAI API error: {str(e)}")
    except Exception as e:
        # Handle other unexpected errors
        raise Exception(f"Unexpected error: {str(e)}")
