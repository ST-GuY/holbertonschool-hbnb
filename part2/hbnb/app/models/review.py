# app/models/review.py
from app.models import BaseModel


class Review(BaseModel):
    """
    Modèle Review qui hérite de BaseModel.
    Champs principaux : text, user_id, place_id
    """
    def __init__(self, text, user_id=None, place_id=None, **kwargs):
        # Appelle le constructeur de BaseModel
        super().__init__(**kwargs)
        self.text = text
        self.user_id = user_id
        self.place_id = place_id
