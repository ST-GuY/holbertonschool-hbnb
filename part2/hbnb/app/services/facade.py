from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        # Repositories mémoire pour chaque type
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # ---------- Users ---------- #
    def create_user(self, user_data):
        """
        Crée un utilisateur et l'ajoute au repository.
        user_data: dict avec les champs du User (first_name, email, ...)
        """
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """
        Récupère un utilisateur par ID.
        Retourne None si l'utilisateur n'existe pas.
        """
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """
        Récupère un utilisateur par son email (pour vérifier l'unicité).
        """
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        """
        Retourne la liste de tous les utilisateurs.
        """
        return self.user_repo.get_all()

    def update_user(self, user_id, data):
        """
        Met à jour un utilisateur existant avec les données fournies.
        Retourne l'utilisateur mis à jour, ou None s'il n'existe pas.
        """
        user = self.user_repo.get(user_id)
        if not user:
            return None
        # Met à jour les champs existants
        for key, value in data.items():
            if hasattr(user, key):
                setattr(user, key, value)
        return user

    def delete_user(self, user_id):
        """
        Supprime un utilisateur du repository.
        """
        self.user_repo.delete(user_id)

    # ---------- Place ---------- #
    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def update_place(self, place_id, data):
        self.place_repo.update(place_id, data)

    def delete_place(self, place_id):
        self.place_repo.delete(place_id)

    # ---------- Review ---------- #
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def update_review(self, review_id, data):
        self.review_repo.update(review_id, data)

    def delete_review(self, review_id):
        self.review_repo.delete(review_id)

    # ---------- Amenity ---------- #
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def update_amenity(self, amenity_id, data):
        self.amenity_repo.update(amenity_id, data)

    def delete_amenity(self, amenity_id):
        self.amenity_repo.delete(amenity_id)
