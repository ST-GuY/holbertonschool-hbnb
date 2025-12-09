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

    def __init__(self, title: str, price: float, latitude: float = None,
                 longitude: float = None, description: str = None, owner_id: int = None):
        self.title = title
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.description = description
        self.owner_id = owner_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if len(value) > 100:
            raise ValueError("Title cannot exceed 100 characters")
        self._title = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Price must be a float")
        if value < 0:
            raise ValueError("Price must be positive")
        self._price = float(value)

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if value is not None:
            if not isinstance(value, (float, int)):
                raise TypeError("Latitude must be a float")
            if not -90 <= value <= 90:
                raise ValueError("Latitude must be between -90 and 90")
            self._latitude = float(value)
        else:
            self._latitude = None

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if value is not None:
            if not isinstance(value, (float, int)):
                raise TypeError("Longitude must be a float")
            if not -180 <= value <= 180:
                raise ValueError("Longitude must be between -180 and 180")
            self._longitude = float(value)
        else:
            self._longitude = None

    def to_dict(self):
        """Return a dictionary representation of the Place."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id
        }
