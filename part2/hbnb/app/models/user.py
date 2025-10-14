# app/models/user.py
from app.models import BaseModel
import re


class User(BaseModel):
    """
    Modèle User avec validations :
    - first_name et last_name : max 50 caractères
    - email : obligatoire, format valide
    - is_admin : bool, default False
    """
    def __init__(self, first_name, last_name, email, is_admin=False, **kwargs):
        super().__init__(**kwargs)

        # Validation noms
        if not first_name or len(first_name) > 50:
            raise ValueError("first_name est requis et <= 50 caractères")
        if not last_name or len(last_name) > 50:
            raise ValueError("last_name est requis et <= 50 caractères")
        self.first_name = first_name
        self.last_name = last_name

        # Validation email
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(email_regex, email):
            raise ValueError("email invalide")
        self.email = email

        self.is_admin = bool(is_admin)
