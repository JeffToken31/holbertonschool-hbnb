from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenity_ns
from app.api.v1.review import api as review_ns
from app.api.v1.place import api as place_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc="/api/v1/docs")

    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    # Register the amenity namespace
    api.add_namespace(amenity_ns, path='/api/v1/amenities')
    # Register the review namespace
    api.add_namespace(review_ns, path='/api/v1/review')
    # Register the review namespace
    api.add_namespace(place_ns, path='/api/v1/place')

    return app