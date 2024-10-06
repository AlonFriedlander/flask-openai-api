from flask import Flask
from app.api import api_blueprint  # Importing the API blueprint
from app.extensions import db  # Importing the SQLAlchemy instance
from app.config import Config  # Importing the configuration


def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)

    # Load configuration from the config.py file
    app.config.from_object(Config)

    # Initialize extensions (e.g., database)
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
