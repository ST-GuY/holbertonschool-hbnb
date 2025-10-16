# app/models/place.py
from app.models import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()  # Initialise id, created_at, updated_at de BaseModel
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner  # Doit être une instance de User
        self.reviews = []   # Liste pour stocker les Review liées
        self.amenities = []  # Liste pour stocker les Amenity liés

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be a number")
        if value < 0:
            raise ValueError("Price must be non-negative")
        self._price = float(value)

    @property
    def latitude(self):
        return self.latitude
    
    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Latitude must be a number")
        if value < -90 or value > 90:
            raise ValueError("Latitude must be between -90 and 90")
        self._latitude = float(value)

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Longitude must be a number")
        if value < -180 or value > 180:
            raise ValueError("Longitude must be between -180 and 180")
        self._longitude = float(value)

    def add_review(self, review):
        """Ajoute un objet Review à la place"""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Ajoute un objet Amenity à la place"""
        self.amenities.append(amenity)
