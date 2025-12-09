from app.models.review import Review
from app import db


class ReviewRepository:
    @staticmethod
    def add(review: Review):
        db.session.add(review)
        db.session.commit()
        return review

    @staticmethod
    def get_by_id(review_id: int):
        return Review.query.get(review_id)

    @staticmethod
    def get_all():
        return Review.query.all()
