import re
import uuid
from datetime import datetime


class User:
    def __init__(self, first_name, last_name, email, is_admin=False):
        # ID unique généré automatiquement
        self.id = str(uuid.uuid4())

        # Prénom et nom avec validation de longueur
        if not first_name or len(first_name) > 50:
            raise ValueError("The first name of the user. Required, maximum length of 50 characters")
        self.first_name = first_name

        if not last_name or len(last_name) > 50:
            raise ValueError("The last name of the user. Required, maximum length of 50 characters.")
        self.last_name = last_name

        # Email avec validation de format
        if not self.is_valid_email(email):
            raise ValueError("Invalid email.")
        self.email = email

        # Administrateur par défaut False
        self.is_admin = is_admin

        # Dates de création et de mise à jour
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    # Méthode pour valider l'email
    @staticmethod
    def is_valid_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    # Méthode pour mettre à jour les informations
    def update(self, first_name=None, last_name=None, email=None, is_admin=None):
        if first_name:
            if len(first_name) > 50:
                raise ValueError("The first name must be less than 50 characters long.")
            self.first_name = first_name
        if last_name:
            if len(last_name) > 50:
                raise ValueError("The name must be less than 50 characters long.")
            self.last_name = last_name
        if email:
            if not self.is_valid_email(email):
                raise ValueError("Invalid email.")
            self.email = email
        if is_admin is not None:
            self.is_admin = is_admin

        # Mise à jour de la date
        self.updated_at = datetime.now()

    # Affichage simple de l'utilisateur
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email}) - Admin: {self.is_admin}"
