from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.auth import api as auth_ns
from app.extensions import bcrypt, jwt, db
from app.database import init_db, seed_db


def create_app(config_class="config.DevelopmentConfig"):
    # Création de l'application Flask
    # Flask va automatiquement chercher :
    # - templates/ dans app/templates
    # - static/ dans app/static
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Active CORS pour toute l'application
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Initialisation de l'API REST
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Initialisation des extensions
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    # Initialisation et remplissage de la base de données
    with app.app_context():
        init_db()
        seed_db()

    # Enregistrement des namespaces API
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(auth_ns, path='/api/v1/auth')

    # Enregistrement du blueprint frontend
    from app.routes import frontend
    app.register_blueprint(frontend)

    return app
