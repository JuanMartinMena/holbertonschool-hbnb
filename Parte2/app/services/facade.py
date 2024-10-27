from uuid import uuid4
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()

    # --- Métodos para gestionar usuarios ---
    def create_user(self, user_data):
        user_id = str(uuid4())  # Generar un UUID único para el usuario
        user = User(id=user_id, **user_data)
        self.user_repo.add(user)  # Guardar el usuario en el repositorio
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, data):
        user = self.user_repo.get(user_id)
        if not user:
            raise ValueError("User not found")  # Manejo de error si el usuario no existe
        user.update(**data)
        self.user_repo.update(user_id, data)  # Usamos el ID del usuario para la actualización
        return user

    # --- Métodos para gestionar amenities ---
    def create_amenity(self, amenity_data):
        amenity_id = str(uuid4())  # Generar un UUID único para el amenity
        amenity = Amenity(id=amenity_id, **amenity_data)  # Crea una nueva instancia de Amenity
        self.amenity_repo.add(amenity)  # Guardar el amenity en el repositorio
        return amenity

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)
        if amenity is None:
            raise ValueError("Amenity not found")  # Manejo de error si el amenity no existe
        return amenity

    def get_all_amenities(self):
        return self.amenity_repo.get_all()  # Devuelve todas las amenities

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if amenity is None:
            raise ValueError("Amenity not found")  # Manejo de error si el amenity no existe
        amenity.update(**amenity_data)  # Actualiza la instancia de Amenity con los datos nuevos
        self.amenity_repo.update(amenity_id, amenity_data)  # Guarda los cambios en el repositorio
        return amenity

    # --- Métodos para gestionar lugares ---
    def create_place(self, place_data):
        place_id = str(uuid4())  # Generar un UUID único para el lugar
        place = Place(id=place_id, **place_data)  # Crea una nueva instancia de Place
        self.place_repo.add(place)  # Guardar el lugar en el repositorio
        return place

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if place is None:
            raise ValueError("Place not found")  # Manejo de error si el lugar no existe
        return place

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if place is None:
            raise ValueError("Place not found")  # Manejo de error si el lugar no existe
        place.update(**place_data)  # Actualiza la instancia de Place con los datos nuevos
        self.place_repo.update(place_id, place_data)  # Guarda los cambios en el repositorio
        return place
