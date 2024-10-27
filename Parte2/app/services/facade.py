from uuid import uuid4
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        # Inicialización de los repositorios en memoria para cada entidad
        self.user_repo = InMemoryRepository()  # Repositorio para usuarios
        self.amenity_repo = InMemoryRepository()  # Repositorio para amenities
        self.place_repo = InMemoryRepository()  # Repositorio para lugares
        self.review_repo = InMemoryRepository()  # Repositorio para reviews

    # --- Métodos para gestionar usuarios ---
    def create_user(self, user_data):
        user = User(**user_data)  # Crear una instancia de usuario
        self.user_repo.add(user)  # Guardar el usuario en el repositorio
        return user  # Retornar el usuario creado

    def get_user(self, user_id):
        return self.user_repo.get(user_id)  # Obtener un usuario por su ID

    def get_user_by_email(self, email):
        # Obtener un usuario por su atributo 'email'
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, data):
        user = self.user_repo.get(user_id)  # Buscar usuario
        if not user:
            raise ValueError("User not found")  # Error si el usuario no existe
        user.update(**data)  # Actualizar los datos en la instancia del usuario
        self.user_repo.update(user_id, data)  # Guardar los cambios en el repositorio
        return user  # Retornar el usuario actualizado

    # --- Métodos para gestionar amenities ---
    def create_amenity(self, amenity_data):
        amenity_id = str(uuid4())  # Generar un UUID único para el amenity
        amenity = Amenity(id=amenity_id, **amenity_data)  # Crear instancia de Amenity
        self.amenity_repo.add(amenity)  # Guardar el amenity en el repositorio
        return amenity  # Retornar el amenity creado

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)  # Obtener amenity por su ID
        if amenity is None:
            raise ValueError("Amenity not found")  # Error si el amenity no existe
        return amenity  # Retornar el amenity

    def get_all_amenities(self):
        return self.amenity_repo.get_all()  # Obtener todos los amenities

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)  # Buscar amenity por ID
        if amenity is None:
            raise ValueError("Amenity not found")  # Error si el amenity no existe
        amenity.update(**amenity_data)  # Actualizar datos del amenity
        self.amenity_repo.update(amenity_id, amenity_data)  # Guardar cambios en repositorio
        return amenity  # Retornar el amenity actualizado

    # --- Métodos para gestionar lugares ---
    def create_place(self, place_data):
        place_id = str(uuid4())  # Generar un UUID único para el lugar
        place = Place(id=place_id, **place_data)  # Crear instancia de Place
        self.place_repo.add(place)  # Guardar el lugar en el repositorio
        return place  # Retornar el lugar creado

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)  # Obtener lugar por su ID
        if place is None:
            raise ValueError("Place not found")  # Error si el lugar no existe
        return place  # Retornar el lugar

    def get_all_places(self):
        return self.place_repo.get_all()  # Obtener todos los lugares

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)  # Buscar lugar por ID
        if place is None:
            raise ValueError("Place not found")  # Error si el lugar no existe
        place.update(**place_data)  # Actualizar datos del lugar
        self.place_repo.update(place_id, place_data)  # Guardar cambios en repositorio
        return place  # Retornar el lugar actualizado

    # --- Métodos para gestionar reviews ---
    def create_review(self, review_data):
        # Validar que el 'place' y 'user' existan antes de crear un review
        place = self.place_repo.get(review_data['place'])
        user = self.user_repo.get(review_data['user'])

        if place is None:
            raise ValueError("Place not found")  # Error si el lugar no existe
        if user is None:
            raise ValueError("User not found")  # Error si el usuario no existe

        review_id = str(uuid4())  # Generar un UUID único para el review
        review = Review(id=review_id, **review_data)  # Crear instancia de Review
        self.review_repo.add(review)  # Guardar el review en el repositorio
        return review  # Retornar el review creado

    def get_review(self, review_id):
        review = self.review_repo.get(review_id)  # Obtener review por su ID
        if review is None:
            raise ValueError("Review not found")  # Error si el review no existe
        return review  # Retornar el review

    def get_all_reviews(self):
        return self.review_repo.get_all()  # Obtener todos los reviews

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)  # Buscar review por ID
        if review is None:
            raise ValueError("Review not found")  # Error si el review no existe
        review.update(**review_data)  # Actualizar datos del review
        self.review_repo.update(review_id, review_data)  # Guardar cambios en repositorio
        return review  # Retornar el review actualizado

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)  # Obtener review por ID
        if review is None:
            raise ValueError("Review not found")  # Error si el review no existe
        self.review_repo.delete(review_id)  # Asumir que tienes un método delete en el repositorio

    def get_reviews_by_place(self, place_id):
        # Filtrar las reseñas por ID del lugar
        return [review for review in self.review_repo.get_all() if review.place == place_id]
