from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('reviews', description='Review operations')

# --- Models ---
review_model = api.model('Review', {
    'place_id': fields.String(required=True, description='ID of the place'),
    'text': fields.String(required=True, description='Review text')
})

review_update_model = api.model('ReviewUpdate', {
    'text': fields.String(required=True, description='Updated review text')
})


# --- Helper function ---
def is_admin():
    jwt_data = get_jwt()
    return jwt_data.get("is_admin", False)


# --- Endpoints ---
@api.route('/')
class ReviewList(Resource):
    @jwt_required()
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Create a new review (authenticated)"""
        current_user_id = get_jwt_identity()
        data = api.payload
        place = facade.get_place(data['place_id'])
        if not place:
            return {'error': 'Place not found'}, 404

        # Check ownership
        if str(place.owner.id) == current_user_id:
            return {'error': 'You cannot review your own place.'}, 400

        # Check duplicate review
        for review in place.reviews:
            if str(review.user.id) == current_user_id:
                return {'error': 'You have already reviewed this place.'}, 400

        # Create review
        data['user_id'] = current_user_id
        try:
            new_review = facade.create_review(data)
            return new_review.to_dict(), 201
        except Exception as e:
            return {'error': str(e)}, 400


@api.route('/<review_id>')
class ReviewResource(Resource):
    @jwt_required()
    @api.expect(review_update_model)
    @api.response(200, 'Review updated successfully')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'Review not found')
    def put(self, review_id):
        """Update a review (authenticated, owner or admin)"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404

        current_user_id = get_jwt_identity()
        if not is_admin() and str(review.user.id) != current_user_id:
            return {'error': 'Unauthorized action'}, 403

        try:
            facade.update_review(review_id, api.payload)
            return {'message': 'Review updated successfully'}, 200
        except Exception as e:
            return {'error': str(e)}, 400

    @jwt_required()
    @api.response(200, 'Review deleted successfully')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review (authenticated, owner or admin)"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404

        current_user_id = get_jwt_identity()
        if not is_admin() and str(review.user.id) != current_user_id:
            return {'error': 'Unauthorized action'}, 403

        try:
            facade.delete_review(review_id)
            return {'message': 'Review deleted successfully'}, 200
        except Exception as e:
            return {'error': str(e)}, 400
