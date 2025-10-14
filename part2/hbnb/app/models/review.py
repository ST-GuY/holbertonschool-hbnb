from app.models import BaseModel

class Review(BaseModel):
    """
    Représente un avis laissé par un utilisateur sur un lieu.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_id = kwargs.get("user_id", "")
        self.place_id = kwargs.get("place_id", "")
        self.text = kwargs.get("text", "")
        self.rating = kwargs.get("rating", 0)
