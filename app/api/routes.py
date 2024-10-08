from flask import request, jsonify, Response
from app.services import get_openai_answer
from app.models import QuestionAnswer
from app.extensions import db
from app.api import api_blueprint
from typing import Dict, Tuple


@api_blueprint.route('/ask', methods=['POST'])
def ask_question() -> tuple[Response, int]:
    """
    Endpoint to ask a question and receive an answer from OpenAI.

    Expects a JSON payload with a 'question' key.
    Returns:
        - 200 OK with the question and answer if successful.
        - 400 Bad Request if the question is missing.
        - 500 Internal Server Error if there is an issue during processing.
    """
    data: Dict = request.json
    question: str = data.get('question')

    if not question:
        return jsonify({"error": "Please provide a question"}), 400

    try:
        # Call OpenAI API to get an answer
        answer: str = get_openai_answer(question)

        # Save question and answer in the database
        qa = QuestionAnswer(question=question, answer=answer)
        db.session.add(qa)
        db.session.commit()

        return jsonify({"question": question, "answer": answer}), 200

    except Exception as e:
        # Log the error (optional: implement logging)
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
