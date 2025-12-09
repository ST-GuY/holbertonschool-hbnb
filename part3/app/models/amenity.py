from app import db


class Amenity(db.Model):
    __tablename__ = "amenities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name: str):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not value.strip():
            raise ValueError("Name cannot be empty")
        if len(value) > 50:
            raise ValueError("Name cannot exceed 50 characters")
        self._name = value

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
