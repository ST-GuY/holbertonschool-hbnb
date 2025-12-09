from app import db


class Place(db.Model):
    __tablename__ = "places"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1024))
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    owner_id = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id
        }
