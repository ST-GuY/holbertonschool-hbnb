# app/models/user.py
from app.models import BaseModel


class User(BaseModel):
    """
    Modèle User qui hérite de BaseModel.
    Champs principaux : first_name, last_name, email
    """
    def __init__(self, first_name, email, last_name=None, **kwargs):
        # Appelle le constructeur de BaseModel
        super().__init__(**kwargs)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
