from app import db

class Place(db.Model):
    __tablename__ = "places"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1024))
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    # Mapper user_id sur la colonne existante owner_id, en utilisant UUID (string)
    user_id = db.Column('owner_id', db.String(36), db.ForeignKey('users.id'), nullable=False)

    # Relation Place → Review (One-to-Many)
    reviews = db.relationship('Review', backref='place', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "user_id": self.user_id
        }
