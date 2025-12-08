from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services import facade

# Création du namespace "auth"
api = Namespace('auth', description='Authentication operations')

# Modèle pour la validation de l'input (email + password)
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})


@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Authenticate user and return a JWT token"""
        credentials = api.payload  # Récupère le JSON envoyé par le client
        # Étape 1 : récupérer l'utilisateur par email
        user = facade.get_user_by_email(credentials['email'])

        # Étape 2 : vérifier si l'utilisateur existe et si le mot de passe est correct
        if not user or not user.verify_password(credentials['password']):
            return {'error': 'Invalid credentials'}, 401

        # Étape 3 : générer un JWT avec l'id de l'utilisateur et le flag is_admin
        access_token = create_access_token(
            identity=str(user.id),  # On met l'ID de l'utilisateur
            additional_claims={"is_admin": user.is_admin}  # Info supplémentaire
        )

        # Étape 4 : renvoyer le token JWT au client
        return {'access_token': access_token}, 200
