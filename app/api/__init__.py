from flask import Blueprint

# Creating a blueprint for API routes
api_blueprint = Blueprint('api', __name__)

# Make sure to import routes here so they are registered with the blueprint
from app.api import routes
