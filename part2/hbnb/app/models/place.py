from models.base_model import BaseModel
from models.user import User


class Place(BaseModel):
    def __init__(self, title, price, latitude, longitude, owner, description=None):
        super().__init__()

        # Title validation
        if not title or len(title) > 100:
            raise ValueError("title est obligatoire et doit faire moins de 100 caractères.")

        # Price validation
        if price < 0:
            raise ValueError("price doit être un nombre positif.")

        # Latitude validation
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("latitude doit être entre -90.0 et 90.0")

        # Longitude validation
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("longitude doit être entre -180.0 et 180.0")

        # Owner validation
        if not isinstance(owner, User):
            raise TypeError("owner doit être une instance de User.")

        self.title = title
        self.description = description
        self.price = float(price)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.owner = owner
