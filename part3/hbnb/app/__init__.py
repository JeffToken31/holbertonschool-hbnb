from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenity_ns
from app.api.v1.review import api as review_ns
from app.api.v1.place import api as place_ns
from app.api.v1.auth import api as auth_ns
from app.api.v1.admin import api as admin_ns
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

bcrypt = Bcrypt()
jwt = JWTManager()

def admin_users():
        from app.services import facade
        email = "admin@example.com"
        user = facade.get_user_by_email(email)
        if not user:
            user = facade.create_user({
                "first_name": "Admin",
                "last_name": "Root",
                "email": email,
                "password": "adminpassword"
            })
            user.is_admin = True
            print(f"admin user: {user.email}")
        else:
            print(f"User already exists: {user.email}")

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc="/api/v1/docs")
    bcrypt.init_app(app)
    jwt.init_app(app)

    api.add_namespace(auth_ns, path='/api/v1/auth')
    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    # Register the amenity namespace
    api.add_namespace(amenity_ns, path='/api/v1/amenities')
    # Register the review namespace
    api.add_namespace(review_ns, path='/api/v1/reviews')
    # Register the place namespace
    api.add_namespace(place_ns, path='/api/v1/places')
    # Register the admin namespace
    api.add_namespace(admin_ns, path='/api/v1/admin')


    admin_users()
    return app
