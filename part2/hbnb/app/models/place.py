import uuid
from datetime import datetime
from models.user import User


class Place:
    def __init__(self, title, price, latitude, longitude, owner, description=None):
        # ID unique généré automatiquement
        self.id = str(uuid.uuid4())

        # Titre obligatoire, max 100 caractères
        if not title or len(title) > 100:
            raise ValueError("The title is mandatory and must be less than 100 characters long.")
        self.title = title

        # Description optionnelle
        self.description = description

        # Prix positif
        if price <= 0:
            raise ValueError("The price must be a positive number.")
        self.price = float(price)

        # Latitude valide
        if latitude < -90.0 or latitude > 90.0:
            raise ValueError("The latitude must be between -90.0 and 90.0.")
        self.latitude = float(latitude)

        # Longitude valide
        if longitude < -180.0 or longitude > 180.0:
            raise ValueError("The longitude must be between -180.0 and 180.0.")
        self.longitude = float(longitude)

        # Vérifier que le propriétaire est une instance de User
        if not isinstance(owner, User):
            raise ValueError("The owner must be an existing user.")
        self.owner = owner

        # Dates de création et de mise à jour
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    # Méthode pour mettre à jour les informations
    def update(self, title=None, price=None, latitude=None, longitude=None, owner=None, description=None):
        if title:
            if len(title) > 100:
                raise ValueError("The title must be less than 100 characters long.")
            self.title = title
        if price is not None:
            if price <= 0:
                raise ValueError("The price must be a positive number.")
            self.price = float(price)
        if latitude is not None:
            if latitude < -90.0 or latitude > 90.0:
                raise ValueError("The latitude must be between -90.0 and 90.0.")
            self.latitude = float(latitude)
        if longitude is not None:
            if longitude < -180.0 or longitude > 180.0:
                raise ValueError("The longitude must be between -180.0 and 180.0.")
            self.longitude = float(longitude)
        if owner is not None:
            if not isinstance(owner, User):
                raise ValueError("The owner must be an existing user.")
            self.owner = owner
        if description is not None:
            self.description = description

        # Mettre à jour la date de modification
        self.updated_at = datetime.now()

    # Affichage simple du lieu
    def __str__(self):
        return f"{self.title} ({self.latitude}, {self.longitude}) - Prix: {self.price}€ - Owner: {self.owner.first_name} {self.owner.last_name}"
