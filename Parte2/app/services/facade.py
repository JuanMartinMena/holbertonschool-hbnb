from flask import jsonify
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        # Inicialización de repositorios para las distintas entidades
        self.user_repo = InMemoryRepository()  # Repositorio para usuarios
        self.amenity_repo = InMemoryRepository()  # Repositorio para amenities
        self.place_repo = InMemoryRepository()  # Repositorio para lugares
        self.review_repo = InMemoryRepository()  # Repositorio para reviews

    # --- Métodos para gestionar usuarios ---
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return jsonify(user.to_dict())  # Aquí cambiamos a jsonify

    def get_user(self, user_id):
        user = self.user_repo.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user.to_dict())

    def get_user_by_email(self, email):
        user = self.user_repo.get_by_attribute('email', email)
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user.to_dict())

    def update_user(self, user_id, data):
        valid_keys = ['first_name', 'last_name', 'email', 'is_admin']
        for key in data.keys():
            if key not in valid_keys:
                return jsonify({"error": f"Invalid attribute: {key}"}), 400

        user = self.user_repo.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        user.update(data)
        self.user_repo.update(user)
        return jsonify(user.to_dict())

    def get_all_users(self):
        users = self.user_repo.get_all()
        return jsonify([user.to_dict() for user in users])

    # --- Métodos para gestionar amenities ---
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return jsonify(amenity.to_dict())

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return jsonify({"error": "Amenity not found"}), 404
        return jsonify(amenity.to_dict())

    def get_all_amenities(self):
        amenities = self.amenity_repo.get_all()
        return jsonify([amenity.to_dict() for amenity in amenities])

    def update_amenity(self, amenity_id, data):
        amenity = self.get_amenity(amenity_id)
        amenity.update(data)
        self.amenity_repo.update(amenity)
        return jsonify(amenity.to_dict())

    # --- Métodos para gestionar lugares ---
    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return jsonify(place.to_dict())

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            return jsonify({"error": "Place not found."}), 404
        return jsonify(place.to_dict())

    def get_all_places(self):
        places = self.place_repo.get_all()
        return jsonify([place.to_dict() for place in places])

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            return jsonify({"error": "Place not found."}), 404
        place.update(place_data)
        self.place_repo.update(place)
        return jsonify(place.to_dict())

    # --- Métodos para gestionar reviews ---
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return jsonify(review.to_dict())

    def get_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            return jsonify({"error": "Review not found"}), 404
        return jsonify(review.to_dict())