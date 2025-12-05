from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()

        # Validation texte
        if not text:
            raise ValueError("text is required.")

        # Validation rating
        if not (1 <= rating <= 5):
            raise ValueError("The rating must be between 1 and 5.")

        # Validation place
        if not isinstance(place, Place):
            raise TypeError("place must be an instance of Place.")

        # Validation user
        if not isinstance(user, User):
            raise TypeError("user must be an instance of User.")

        self.text = text
        self.rating = int(rating)
        self.place = place
        self.user = user
