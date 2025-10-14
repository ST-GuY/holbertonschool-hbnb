# app/models/amenity.py
from app.models import BaseModel


class Amenity(BaseModel):
    """
    Modèle Amenity qui hérite de BaseModel.
    Champs principaux : name, description
    """
    def __init__(self, name, description=None, **kwargs):
        # Appelle le constructeur de BaseModel
        super().__init__(**kwargs)
        self.name = name
        self.description = description
