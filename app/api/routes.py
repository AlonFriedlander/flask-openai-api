from flask import request, jsonify
from app.services import get_openai_answer
from app.models import QuestionAnswer
from app.extensions import db
from app.api import api_blueprint


@api_blueprint.route('/ask', methods=['POST'])
def ask_question():
    """Endpoint to ask a question and receive an answer from OpenAI."""
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({"error": "Please provide a question"}), 400

    # Call OpenAI API to get an answer
    answer = get_openai_answer(question)

    # Save question and answer in the database
    qa = QuestionAnswer(question=question, answer=answer)
    db.session.add(qa)
    db.session.commit()

    return jsonify({"question": question, "answer": answer})
