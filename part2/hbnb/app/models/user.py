from app.models import BaseModel

class User(BaseModel):
    """
    Représente un utilisateur de la plateforme HBnB.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.first_name = kwargs.get("first_name", "")
        self.last_name = kwargs.get("last_name", "")
        self.email = kwargs.get("email", "")
        self.password = kwargs.get("password", "")
