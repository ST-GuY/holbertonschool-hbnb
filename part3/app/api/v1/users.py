from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('users', description='User operations')

# --- Models ---
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user')
})

update_user_model = api.model('UserUpdate', {
    'first_name': fields.String(description='First name of the user'),
    'last_name': fields.String(description='Last name of the user'),
    'email': fields.String(description='Email of the user'),          # admin only
    'password': fields.String(description='Password of the user')     # admin only
})


# --- Helper ---
def is_admin():
    jwt_data = get_jwt()
    return jwt_data.get("is_admin", False)


# --- Endpoints ---
@api.route('/')
class UserList(Resource):
    @jwt_required()
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(403, 'Unauthorized action')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Create a new user (admin only)"""
        if not is_admin():
            return {'error': 'Unauthorized action'}, 403

        user_data = api.payload
        try:
            new_user = facade.create_user(user_data)
            return {'id': new_user.id, 'message': 'User created successfully'}, 201
        except Exception as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Retrieve a list of users"""
        users = facade.get_users()
        return [user.to_dict() for user in users], 200


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

    @jwt_required()
    @api.expect(update_user_model)
    @api.response(200, 'User updated successfully')
    @api.response(403, 'Unauthorized action')
    @api.response(400, 'Invalid input data')
    @api.response(404, 'User not found')
    def put(self, user_id):
        """Update user details (owner or admin)"""
        current_user_id = get_jwt_identity()
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        update_data = api.payload

        # Vérification des droits
        if not is_admin() and user_id != current_user_id:
            return {'error': 'Unauthorized action'}, 403

        # Seul l’admin peut modifier email et password
        if not is_admin():
            if 'email' in update_data or 'password' in update_data:
                return {'error': 'You cannot modify email or password'}, 400

        try:
            facade.update_user(user_id, update_data)
            return user.to_dict(), 200
        except Exception as e:
            return {'error': str(e)}, 400
