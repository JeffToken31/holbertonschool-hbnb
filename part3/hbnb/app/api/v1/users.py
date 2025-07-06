from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import bcrypt



api = Namespace('users', description='User operations')
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='password of the user')
})


@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400
        try:
            new_user = facade.create_user(user_data)
        except (TypeError, ValueError) as e:
            return {'error': str(e)}, 400
        return {"id": new_user.id, "message": "User registered successfully"}, 201

    @api.response(200, 'the list of users is successfully retrieved')
    def get(self):
        """
        List all users
        """
        users = facade.get_all_users()
        return [{
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email} for user in users
            ], 200


@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return user.to_dict(), 200

    @api.expect(user_model, validate=True)
    @api.response(200, 'User details modified successfully')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def put(self, user_id):
        """Modify user"""
        user_data = api.payload
        current_user = get_jwt_identity()
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        if user_id != current_user["id"]:
            return {'error': 'Unauthorized action'}, 403

        if 'email' in user_data and user_data['email'] != user.email:
            return {'error': 'You cannot modify email or password.'}, 400

        if 'password' in user_data and not bcrypt.check_password_hash(user.password, user_data['password']):
            return {'error': 'You cannot modify email or password.'}, 400

        try:
            user_updated = facade.update_user(user_id, user_data)
            if not user_updated:
                return {'error': 'User not found'}, 404
        except (TypeError, ValueError) as e:
            return {'error': str(e)}, 400
        return user_updated.to_dict(), 200
