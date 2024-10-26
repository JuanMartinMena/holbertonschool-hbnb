from app.models.user import User
from app.models.amenity import Amenity  # Importa el modelo de Amenity
from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()  # Repositorio para amenities

    # --- Métodos para gestionar usuarios ---
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, data):
        user = self.user_repo.get(user_id)
        if not user:
            return None
        user.update(**data)
        self.user_repo.update(user)
        return user

    # --- Métodos para gestionar amenities ---
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)  # Crea una nueva instancia de Amenity
        self.amenity_repo.add(amenity)     # Guarda en el repositorio de amenities
        return amenity

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)
        if amenity is None:
            raise ValueError("Amenity not found")
        return amenity

    def get_all_amenities(self):
        return self.amenity_repo.get_all()  # Devuelve todas las amenities

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if amenity is None:
            raise ValueError("Amenity not found")
        amenity.update(**amenity_data)
        self.amenity_repo.update(amenity)
        return amenity
