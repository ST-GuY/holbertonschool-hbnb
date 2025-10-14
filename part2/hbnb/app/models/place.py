from app.models import BaseModel

class Place(BaseModel):
    """
    Représente un lieu proposé par un utilisateur.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name", "")
        self.description = kwargs.get("description", "")
        self.city = kwargs.get("city", "")
        self.price_per_night = kwargs.get("price_per_night", 0)
        self.owner_id = kwargs.get("owner_id", "")
