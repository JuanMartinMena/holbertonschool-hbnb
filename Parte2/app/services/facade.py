from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        # Inicialización de repositorios para las distintas entidades
        self.user_repo = InMemoryRepository() #Repostiorio para users
        self.amenity_repo = InMemoryRepository()  # Repositorio para amenities
        self.place_repo = InMemoryRepository()  # Repositorio para lugares
        self.review_repo = InMemoryRepository()  # Repositorio para reviews

    # --- Métodos para gestionar usuarios ---
    def create_user(self, user_data):
        """Crea un usuario y lo guarda en el repositorio"""
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Obtiene un usuario por ID"""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Obtiene un usuario por su email"""
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, data):
        """Actualiza los datos de un usuario"""
        user = self.user_repo.get(user_id)
        if not user:
            return None
        user.update(**data)
        self.user_repo.update(user)
        return user

    # --- Métodos para gestionar amenities ---
    def create_amenity(self, amenity_data):
        """Crea una nueva amenidad y la guarda en el repositorio"""
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Obtiene una amenidad por su ID"""
        amenity = self.amenity_repo.get(amenity_id)
        if amenity is None:
            raise ValueError("Amenity not found")
        return amenity

    def get_all_amenities(self):
        """Obtiene todas las amenidades"""
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """Actualiza una amenidad"""
        amenity = self.amenity_repo.get(amenity_id)
        if amenity is None:
            raise ValueError("Amenity not found")
        amenity.update(**amenity_data)
        self.amenity_repo.update(amenity)
        return amenity

    # --- Métodos para gestionar lugares (places) ---
    def create_place(self, place_data):
        """Crea un lugar y lo guarda en el repositorio"""
        owner = self.user_repo.get(place_data['owner'])  # Validar que el propietario existe
        if not owner:
            raise ValueError("Invalid user ID for owner")
        
        place = Place(**place_data)
        place.owner = owner  # Asignar el propietario
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """Obtiene un lugar por su ID"""
        place = self.place_repo.get(place_id)
        if place is None:
            raise ValueError("Place not found")
        return place

    def get_all_places(self):
        """Obtiene todos los lugares"""
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """Actualiza los datos de un lugar"""
        place = self.place_repo.get(place_id)
        if place is None:
            raise ValueError("Place not found")
        place.update(**place_data)
        self.place_repo.update(place)
        return place

    # --- Métodos para gestionar reviews ---
    def create_review(self, review_data):
        """Crea una nueva review y la guarda en el repositorio"""
        user = self.user_repo.get(review_data['user'])  # Validar que el usuario existe
        if not user:
            raise ValueError("Invalid user ID for review")

        place = self.place_repo.get(review_data['place'])  # Validar que el lugar existe
        if not place:
            raise ValueError("Invalid place ID for review")
        
        review = Review(**review_data)
        self.review_repo.add(review)
        place.add_review(review)  # Añadir la review al lugar
        return review

    def get_review(self, review_id):
        """Obtiene una review por su ID"""
        review = self.review_repo.get(review_id)
        if review is None:
            raise ValueError("Review not found")
        return review

    def get_all_reviews(self):
        """Obtiene todas las reviews"""
        return self.review_repo.get_all()

    def update_review(self, review_id, review_data):
        """Actualiza una review"""
        review = self.review_repo.get(review_id)
        if review is None:
            raise ValueError("Review not found")
        review.update(**review_data)
        self.review_repo.update(review)
        return review
