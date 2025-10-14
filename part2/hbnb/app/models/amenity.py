from app.models import BaseModel


class Amenity(BaseModel):
    """
    Représente une commodité (Wi-Fi, piscine, etc.)
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name", "")
        self.description = kwargs.get("description", "")
