import pytest
from app import create_app  # Assuming this is how your Flask app is created
from flask import json


@pytest.fixture
def client():
    app = create_app()  # Ensure this returns the Flask app
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_ask_endpoint(client):
    response = client.post('/api/ask', json={
        'question': 'What is the meaning of life?'
    })

    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'answer' in data
    assert data['answer'] is not None
