from app.models.amenity import Amenity
from app import db


class AmenityRepository:
    @staticmethod
    def add(amenity: Amenity):
        db.session.add(amenity)
        db.session.commit()
        return amenity

    @staticmethod
    def get_by_id(amenity_id: int):
        return Amenity.query.get(amenity_id)

    @staticmethod
    def get_all():
        return Amenity.query.all()
