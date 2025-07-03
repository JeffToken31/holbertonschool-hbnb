import app
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('admin', description='Admin operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='password of the user'),
    'is_admin': fields.Boolean(required=True, descrition='is admin')
})

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})


@api.route('/users/')
class AdminUserCreate(Resource):
    @api.expect(user_model, validate=True)
    @api.doc(security='Bearer')
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = api.payload
        email = user_data.get('email')

        # Check if email is already in use
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        # Logic to create a new user
        try:
            new_user = facade.create_user(user_data)
        except (TypeError, ValueError) as e:
            return {'error': str(e)}, 400
        return {"id": new_user.id, "message": "User registered successfully"}, 201

@api.route('/users/<user_id>')
class AdminUserResource(Resource):
    @api.expect(user_model, validate=True)
    @api.doc(security='Bearer')
    @api.response(200, 'User details modified successfully')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt_identity()
        
        # If 'is_admin' is part of the identity payload
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = api.payload
        email = user_data.get('email')

        if email:
            # Check if email is already in use
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email is already in use'}, 400

        # Logic to update user details, including email and password
        try:
            user_updated = facade.update_user(user_id, user_data)
            if not user_updated:
                return {'error': 'User not found'}, 404
        except (TypeError, ValueError) as e:
            return {'error': str(e)}, 400
        return user_updated.to_dict(), 200


    #penser a implementer deletee user

@api.route('/amenities/')
class AdminAmenityCreate(Resource):
    @api.expect(amenity_model)
    @api.doc(security='Bearer')
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        # Logic to create a new amenity
        amenity_data = api.payload
        try:
            new_amenity = facade.create_amenity(amenity_data)
        except (TypeError, ValueError) as e:
            return {'error': str(e)}, 400

        return new_amenity.to_dict(), 201

@api.route('/amenities/<amenity_id>')
class AdminAmenityModify(Resource):
    @api.expect(amenity_model, validate=True)
    @api.doc(security='Bearer')
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, amenity_id):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        amenity_data = api.payload
        try:
            amenity_updated = facade.update_amenity(amenity_id, amenity_data)
            if not amenity_updated:
                return {'error': 'Amenity not found'}, 404
        except (TypeError, ValueError) as e:
            return {'error': str(e)}, 400
        return amenity_updated.to_dict()
    #pensez a implementer delete