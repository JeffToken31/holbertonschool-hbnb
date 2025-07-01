from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenity_ns
from app.api.v1.review import api as review_ns
from app.api.v1.place import api as place_ns
from app.api.v1.auth import api as auth_ns
from app.api.v1.protected import api as protected_ns
from app.extends import bcrypt
from app.extends import jwt
from config import DevelopmentConfig


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config["JWT_SECRET_KEY"] = "my-very-strong-and-long-secret-key-1234567890"

    authorizations = {
        'BearerAuth': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'Bearer <access_token>'
        }
    }
    api = Api(app,
            version='1.0',
            title='HBnB API',
            description='HBnB Application API',
            doc="/api/v1/docs",
            authorizations=authorizations,
            security='BearerAuth')


    bcrypt.init_app(app)
    jwt.init_app(app)

    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenity_ns, path='/api/v1/amenities')
    api.add_namespace(review_ns, path='/api/v1/reviews')
    api.add_namespace(place_ns, path='/api/v1/places')
    api.add_namespace(auth_ns, path='/api/v1/auth')
    api.add_namespace(protected_ns, path='/api/v1/protected')

    return app
