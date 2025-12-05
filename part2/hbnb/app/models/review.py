from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()

        # Validation texte
        if not text:
            raise ValueError("text est obligatoire.")

        # Validation rating
        if not (1 <= rating <= 5):
            raise ValueError("rating doit être entre 1 et 5.")

        # Validation place
        if not isinstance(place, Place):
            raise TypeError("place doit être une instance de Place.")

        # Validation user
        if not isinstance(user, User):
            raise TypeError("user doit être une instance de User.")

        self.text = text
        self.rating = int(rating)
        self.place = place
        self.user = user
