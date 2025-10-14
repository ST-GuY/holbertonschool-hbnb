# app/models/review.py
from app.models import BaseModel


class Review(BaseModel):
    """
    Modèle Review qui hérite de BaseModel.
    Champs principaux : text, rating, user, place
    """
    def __init__(self, text, rating, place, user, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.rating = rating
        self.place = place   # instance de Place
        self.user = user     # instance de User
