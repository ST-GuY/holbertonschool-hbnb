from models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()

        if not name or len(name) > 50:
            raise ValueError("name est obligatoire et doit faire moins de 50 caractères.")

        self.name = name
