import unittest
from app.services import facade
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

class TestHBnBFacade(unittest.TestCase):

    def setUp(self):
        """Avant chaque test, on vide les repositories pour éviter les interférences."""
        facade.user_repo._storage.clear()
        facade.place_repo._storage.clear()
        facade.review_repo._storage.clear()
        facade.amenity_repo._storage.clear()

    # ---------- User Tests ---------- #
    def test_create_user(self):
        user_data = {"first_name": "Alice", "email": "alice@example.com"}
        user = facade.create_user(user_data)

        self.assertIsInstance(user, User)
        self.assertEqual(user.first_name, "Alice")
        self.assertEqual(facade.get_user(user.id), user)

    def test_update_user(self):
        user = facade.create_user({"first_name": "Bob", "email": "bob@example.com"})
        facade.user_repo.update(user.id, {"first_name": "Bobby"})
        updated = facade.get_user(user.id)
        self.assertEqual(updated.first_name, "Bobby")

    def test_delete_user(self):
        user = facade.create_user({"first_name": "Charlie", "email": "charlie@example.com"})
        facade.delete_user(user.id)
        self.assertIsNone(facade.get_user(user.id))

    # ---------- Place Tests ---------- #
    def test_create_place(self):
        place_data = {"name": "Beach House", "city": "Miami"}
        place = facade.create_place(place_data)
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city, "Miami")

    # ---------- Review Tests ---------- #
    def test_create_review(self):
        review_data = {"text": "Great place!"}
        review = facade.create_review(review_data)
        self.assertIsInstance(review, Review)
        self.assertEqual(review.text, "Great place!")

    # ---------- Amenity Tests ---------- #
    def test_create_amenity(self):
        amenity_data = {"name": "WiFi"}
        amenity = facade.create_amenity(amenity_data)
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "WiFi")


if __name__ == "__main__":
    unittest.main()
