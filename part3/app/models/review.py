from app import db


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    # Relation Review → User (One-to-Many)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relation Review → Place (One-to-Many)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "rating": self.rating,
            "user_id": self.user_id,
            "place_id": self.place_id
        }
