import uuid
from datetime import datetime


class Amenity:
    def __init__(self, name):
        # ID unique généré automatiquement
        self.id = str(uuid.uuid4())

        # Nom obligatoire + max 50 caractères
        if not name or len(name) > 50:
            raise ValueError("The name of the amenity is mandatory and must be less than 50 characters long.")
        self.name = name

        # Dates de création et mise à jour
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    # Méthode pour mettre à jour une amenity
    def update(self, name=None):
        if name:
            if len(name) > 50:
                raise ValueError("The name must be less than 50 characters long.")
            self.name = name

        # Mise à jour de la date
        self.updated_at = datetime.now()

    # Affichage simple
    def __str__(self):
        return f"Amenity: {self.name}"
