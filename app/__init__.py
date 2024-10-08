import logging
from flask import Flask
from app.api import api_blueprint  # Importing the API blueprint
from app.extensions import db  # Importing the SQLAlchemy instance
from app.config import Config  # Importing the configuration


def create_app() -> Flask:
    """
    Create and configure the Flask application.

    - Loads configuration from config.py.
    - Initializes the database using SQLAlchemy.
    - Registers API routes using blueprints.

    Returns:
        A configured Flask application instance.

    Raises:
        RuntimeError: If an error occurs during application setup.
    """
    try:
        app = Flask(__name__)

        # Load configuration from the config.py file
        app.config.from_object(Config)

        # Initialize extensions (e.g., SQLAlchemy database)
        db.init_app(app)

        # Register blueprints to organize API routes
        app.register_blueprint(api_blueprint, url_prefix='/api')

        return app

    except Exception as e:
        # Log the error for debugging
        logging.error(f"Failed to create Flask app: {e}")

        # Raise a more descriptive error
        raise RuntimeError("Application setup failed. Check the logs for details.") from e
