import uuid
from datetime import datetime
from models.user import User
from models.place import Place


class Review:
    def __init__(self, text, rating, place, user):
        # ID unique généré automatiquement
        self.id = str(uuid.uuid4())

        # TEXT : contenu obligatoire
        if not text:
            raise ValueError("The text of the notice is mandatory.")
        self.text = text

        # RATING : note entre 1 et 5
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError("The rating must be an integer between 1 and 5.")
        self.rating = rating

        # PLACE : doit être une instance valide de Place
        if not isinstance(place, Place):
            raise ValueError("The location must be a valid instance of Place.")
        self.place = place

        # USER : doit être une instance valide de User
        if not isinstance(user, User):
            raise ValueError("The author must be a valid instance of User.")
        self.user = user

        # Dates de création et de mise à jour
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    # Méthode pour mettre à jour une review
    def update(self, text=None, rating=None):
        if text:
            self.text = text

        if rating is not None:
            if not isinstance(rating, int) or rating < 1 or rating > 5:
                raise ValueError("The rating must be an integer between 1 and 5.")
            self.rating = rating

        # Mise à jour de la date
        self.updated_at = datetime.now()

    # Affichage texte simple
    def __str__(self):
        return f"Avis par {self.user.first_name} : {self.text} (Note : {self.rating}/5)"
