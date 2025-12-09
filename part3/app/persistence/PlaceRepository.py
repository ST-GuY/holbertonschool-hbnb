from app.models.place import Place
from app import db


class PlaceRepository:
    @staticmethod
    def add(place: Place):
        db.session.add(place)
        db.session.commit()
        return place

    @staticmethod
    def get_by_id(place_id: int):
        return Place.query.get(place_id)

    @staticmethod
    def get_all():
        return Place.query.all()
