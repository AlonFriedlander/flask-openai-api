# Flask-OpenAI API Project

#### Author: **Alon Friedlander**
***
## Project Overview
This project demonstrates integration with OpenAI’s API to handle user queries, returning answers that are stored in a PostgreSQL database. The project includes Flask for the server, PostgreSQL for database storage, Alembic for database migrations, and pytest for testing. Docker and Docker Compose are used to containerize the application, ensuring ease of deployment and environment consistency.
### Tasks Completed
- **Flask Server**: Set up a Flask server to handle user questions through a POST endpoint /api/ask.
- **OpenAI Integration**: Integrated OpenAI’s API to get answers for user-provided questions.
- **PostgreSQL Database**: Configured a PostgreSQL database to store questions and answers.
- **Alembic Migrations**: Implemented database migrations using Alembic for managing schema changes.
- **Dockerization**: Dockerized both the Flask server and PostgreSQL database.
- **Testing**: Added pytest test for the /api/ask endpoint to ensure proper functionality.

### Setup Instructions

#### Prerequisites
- **Docker:** Make sure Docker is installed on your machine.
- **Docker Compose:** Install Docker Compose for managing multi-container environments.
- **OpenAI API Key:** An OpenAI API key is required for the API integration.

#### Running the Project
1. Clone the repository:
```bash
git clone https://github.com/AlonFriedlander/flask-openai-api.git
cd flask-openai-api
```
2. Create an .env file with your environment variables (example):
```bash
POSTGRES_USER=<your_postgres_user>
POSTGRES_PASSWORD=<your_postgres_password>
POSTGRES_DB=flask_api_db
DATABASE_URL=postgresql://user:password@db:5432/flask_api_db
OPENAI_API_KEY=<your-openai-api-key>
```
> **Note:** Replace the placeholders with your actual credentials.
3. Build and run the containers:
```bash
docker-compose up
```
4. Run the tests (optional): If you want to manually run the tests, use the following command:
```bash
docker-compose --profile test run test
```

### Migrations
Database schema changes are managed by Alembic, and migrations are applied automatically when the containers are started. You don't need to manually run migration commands.


### API Details
- **POST** `http://127.0.0.1:5000/api/ask`: This endpoint accepts a JSON payload with a question field. The API retrieves the answer from OpenAI, stores the question and answer in the database, and returns the result as a JSON response.
**Example Request:**
```json
{
  "question": "What is the meaning of life?"
}
```
**Example Response:**
```json
{
  "question": "What is the meaning of life?",
  "answer": "The meaning of life is a philosophical question that has been debated by thinkers for centuries..."
}
```
