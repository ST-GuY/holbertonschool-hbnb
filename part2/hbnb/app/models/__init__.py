import uuid
from datetime import datetime, timezone


class BaseModel:
    """
    Classe de base pour toutes les entités du modèle.
    Fournit un id unique, des dates de création/mise à jour, et une méthode de mise à jour.
    """
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        # Utilisation de datetime aware pour éviter les warnings Python 3.12+
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self, data):
        """
        Met à jour les attributs de l’objet avec un dictionnaire.
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now(timezone.utc)

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"
