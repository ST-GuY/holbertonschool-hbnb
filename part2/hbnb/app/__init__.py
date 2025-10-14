from flask import Flask
from flask_restx import Api


def create_app():
    # Créer l'application Flask
    app = Flask(__name__)

    # Initialiser l'API RESTx
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description="HBnB Application API",
        doc='/api/v1/'  # Chemin de la doc
    )

    # Retourner l'application
    return app
