from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

api = Namespace('protected', description='Protected routes')


@api.route('/hello')
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()  # ID de l'utilisateur dans le token
        claims = get_jwt()  # Claims supplémentaires (is_admin)

        return {
            "message": f"Hello user {current_user}",
            "is_admin": claims["is_admin"]
        }, 200
