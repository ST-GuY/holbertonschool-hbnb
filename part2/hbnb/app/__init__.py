from flask import Flask
from flask_restx import Api
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns


def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')

    # Enregistre le namespace amenities sur /api/v1/amenities
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')

    return app
