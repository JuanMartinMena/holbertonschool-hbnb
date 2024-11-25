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
        return jsonify(user), 201

    def get_user(self, user_id):
        user = self.user_repo.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user)

    def get_user_by_email(self, email):
        user = self.user_repo.get_by_attribute('email', email)
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user)

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
        return jsonify(user)

    def get_all_users(self):
        users = self.user_repo.get_all()
        return jsonify(users)

    # --- Métodos para gestionar amenities ---
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return jsonify(amenity), 201

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return jsonify({"error": "Amenity not found"}), 404
        return jsonify(amenity)

    def get_all_amenities(self):
        amenities = self.amenity_repo.get_all()
        return jsonify(amenities)

    def update_amenity(self, amenity_id, data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return jsonify({"error": "Amenity not found"}), 404

        amenity.update(data)
        self.amenity_repo.update(amenity)
        return jsonify(amenity)

    # --- Métodos para gestionar lugares ---
    def create_place(self, place_data):
        # Validar que el usuario asociado al lugar exista
        user = self.user_repo.get(place_data.get("user_id"))
        if not user:
            return jsonify({"error": "User not found for this place"}), 404

        place = Place(**place_data)
        self.place_repo.add(place)
        return jsonify(place), 201

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            return jsonify({"error": "Place not found"}), 404
        return jsonify(place)

    def get_all_places(self):
        places = self.place_repo.get_all()
        return jsonify(places)

    def update_place(self, place_id, data):
        valid_keys = ['name', 'description', 'price', 'latitude', 'longitude', 'amenities']
        for key in data.keys():
            if key not in valid_keys:
                return jsonify({"error": f"Invalid attribute: {key}"}), 400

        place = self.place_repo.get(place_id)
        if not place:
            return jsonify({"error": "Place not found"}), 404

        # Actualizar el lugar
        place.update(data)
        self.place_repo.update(place)
        return jsonify(place)

    # --- Métodos para gestionar reviews ---
    def create_review(self, review_data):
        # Validar que el lugar y el usuario asociados a la reseña existan
        place = self.place_repo.get(review_data.get("place_id"))
        user = self.user_repo.get(review_data.get("user_id"))
        if not place or not user:
            return jsonify({"error": "Place or User not found for this review"}), 404

        review = Review(**review_data)
        self.review_repo.add(review)
        return jsonify(review), 201

    def get_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            return jsonify({"error": "Review not found"}), 404
        return jsonify(review)
