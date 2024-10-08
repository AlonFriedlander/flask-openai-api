import pytest
from app import create_app
from flask import json


@pytest.fixture
def client():
    """
    Fixture to set up a test client for the Flask app.

    This function initializes the Flask app in testing mode and provides
    a test client that can be used to make requests to the app's routes
    during testing.

    Yields:
        client: The test client instance for Flask.
    """
    app = create_app()
    app.config['TESTING'] = True  # Enable testing mode

    # Provide a test client to simulate HTTP requests.
    with app.test_client() as client:
        yield client


def test_ask_endpoint(client):
    """
    Test the /api/ask endpoint to ensure it handles the request and
    returns a valid response with an answer from OpenAI.

    Args:
        client: The test client instance.

    This test sends a POST request to the /api/ask endpoint with a sample
    question, and it asserts that the response has a 200 status code and
    contains a valid answer in the response JSON.

    Assertions:
        - Status code should be 200.
        - Response data should contain an 'answer' key.
        - The 'answer' should not be None.
    """
    # Simulating a POST request to the /api/ask endpoint
    response = client.post('/api/ask', json={
        'question': 'Messi or Ronaldo?'
    })

    # Ensure the request was successful (status code 200)
    assert response.status_code == 200

    # Parse the response data as JSON
    data = json.loads(response.data)

    # Ensure the 'answer' key exists in the response and is not None
    assert 'answer' in data
    assert data['answer'] is not None
