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

    def add_review(self, review):
        """Ajoute un objet Review à la place"""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Ajoute un objet Amenity à la place"""
        self.amenities.append(amenity)
