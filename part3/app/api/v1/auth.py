from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from app.services import facade

api = Namespace('auth', description='Authentication operations')

# ----------------------------
# MODEL POUR LOGIN
# ----------------------------

login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

# ----------------------------
# ROUTE : /auth/login
# ----------------------------


@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    @api.response(200, 'Login successful')
    @api.response(401, 'Invalid credentials')
    def post(self):
        """Authenticate user and return a JWT token"""
        credentials = api.payload

        # Récupérer l'utilisateur par email
        user = facade.get_user_by_email(credentials['email'])

        # Vérifier que l'utilisateur existe et que le mot de passe correspond
        if not user or not check_password_hash(user.password, credentials['password']):
            return {'error': 'Invalid credentials'}, 401

        # Générer le JWT token
        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"is_admin": getattr(user, "is_admin", False)}
        )

        return {'access_token': access_token}, 200
