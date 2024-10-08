from app.extensions import db


class QuestionAnswer(db.Model):
    """Model to store questions and their corresponding answers.

    Attributes:
        id (int): The primary key, a unique identifier for each question-answer pair.
        question (str): The question text provided by the user.
        answer (str): The answer text returned from the OpenAI API.
    """
    __tablename__ = 'questions_answers'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question: str = db.Column(db.String(500), nullable=False)  # Assuming max length for question
    answer: str = db.Column(db.String(500), nullable=False)  # Assuming max length for answer

