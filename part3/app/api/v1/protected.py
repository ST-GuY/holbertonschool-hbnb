from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace("protected", description="Protected endpoint")


@api.route("")
class Protected(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        return {"message": f"Hello, user {user_id}"}, 200
