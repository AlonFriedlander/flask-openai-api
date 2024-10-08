import openai
from flask import current_app
from typing import Optional


def get_openai_answer(question: str) -> Optional[str]:
    """Interact with OpenAI to get an answer for the given question.

    Args:
        question (str): The user's question to send to OpenAI.

    Returns:
        Optional[str]: The answer returned from OpenAI, or None if an error occurs.
    """
    try:
        # Set OpenAI API key from the app configuration
        openai.api_key = current_app.config['OPENAI_API_KEY']

        # Use ChatCompletion for models like gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=150  # Adjust max tokens based on your requirements
        )

        # Extracting the answer content safely
        return response['choices'][0]['message']['content']

    except KeyError as e:
        # Handle cases where 'choices' or 'message' keys are missing in response
        current_app.logger.error(f"Unexpected response format from OpenAI: {e}")
        return None
    except Exception as e:
        # Handle general errors (e.g., network issues, invalid API key, etc.)
        current_app.logger.error(f"Failed to get answer from OpenAI: {e}")
        return None

