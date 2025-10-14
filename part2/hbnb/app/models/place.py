# app/models/place.py
from app.models import BaseModel


class Place(BaseModel):
    """
    Modèle Place qui hérite de BaseModel.
    Champs principaux : name, city, description
    """
    def __init__(self, name, city, description=None, **kwargs):
        # Appelle le constructeur de BaseModel
        super().__init__(**kwargs)
        self.name = name
        self.city = city
        self.description = description
