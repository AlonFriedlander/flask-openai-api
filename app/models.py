from app.extensions import db


class QuestionAnswer(db.Model):
    """Model to store questions and their corresponding answers."""
    __tablename__ = 'questions_answers'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
