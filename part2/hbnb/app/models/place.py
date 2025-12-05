from models.base_model import BaseModel
from models.user import User


class Place(BaseModel):
    def __init__(self, title, price, latitude, longitude, owner, description=None):
        super().__init__()

        # Title validation
        if not title or len(title) > 100:
            raise ValueError("title is required and must be less than 100 characters.")

        # Price validation
        if price < 0:
            raise ValueError("price must be a positive number.")

        # Latitude validation
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("latitude must be between -90.0 and 90.0")

        # Longitude validation
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0")

        # Owner validation
        if not isinstance(owner, User):
            raise TypeError("owner must be an instance of User.")

        self.title = title
        self.description = description
        self.price = float(price)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.owner = owner
