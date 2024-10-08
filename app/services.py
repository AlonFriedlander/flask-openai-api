import openai
from flask import current_app


def get_openai_answer(question):
    """Interact with OpenAI to get an answer for the given question."""
    openai.api_key = current_app.config['OPENAI_API_KEY']

    # Use ChatCompletion for chat models like gpt-3.5-turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        max_tokens=150  # Adjust the max tokens as per your requirement
    )

    return response['choices'][0]['message']['content']
