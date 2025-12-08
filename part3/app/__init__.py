from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from app.extensions import bcrypt, jwt
from app.services import facade

db = SQLAlchemy()


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Configuration JWT
    app.config["JWT_SECRET_KEY"] = "change_this_secret_key"
    app.config["JWT_ERROR_MESSAGE_KEY"] = "error"

    # Init Bcrypt + JWT
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Create default user (dev only)
    facade.create_user({
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "password": "your_password",
        "is_admin": True
    })

    # Import namespaces
    from app.api.v1.users import api as users_ns
    from app.api.v1.amenities import api as amenities_ns
    from app.api.v1.places import api as places_ns
    from app.api.v1.reviews import api as reviews_ns
    from app.api.v1.auth import api as auth_ns
    from app.api.v1.protected import api as protected_ns

    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Application API'
    )

    # Register namespaces
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(auth_ns, path='/api/v1/auth')
    api.add_namespace(protected_ns, path='/api/v1/protected')

    return app
