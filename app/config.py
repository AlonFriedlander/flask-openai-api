import os


class Config:
    """
    Configuration class for the Flask application.

    Attributes:
        SQLALCHEMY_DATABASE_URI (str): Database connection URI for SQLAlchemy.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Whether to track modifications in SQLAlchemy (set to False for performance).
        OPENAI_API_KEY (str): API key for OpenAI services.
    """

    # Get the database URL from environment variables, defaulting to a local Postgres instance if not provided
    SQLALCHEMY_DATABASE_URI: str = os.getenv(
        'DATABASE_URL',
        'postgresql://user:password@db:5432/flask_api_db'
    )

    # Disable SQLAlchemy modification tracking to save memory
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    # Fetch the OpenAI API key from environment variables and raise an error if it's not set
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY')

    if not OPENAI_API_KEY:
        raise ValueError("The OpenAI API key must be set in the environment variable 'OPENAI_API_KEY'.")
