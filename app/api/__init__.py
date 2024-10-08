from flask import Blueprint

# Creating a blueprint for API routes
api_blueprint: Blueprint = Blueprint('api', __name__)

# Importing routes so they are registered with the blueprint
from app.api import routes
