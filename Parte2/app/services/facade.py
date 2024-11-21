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
        valid_keys = ['first_name', 'last_name', 'email', 'is_admin']
        for key in data.keys():
            if key not in valid_keys:
                raise ValueError(f"Invalid attribute: {key}")

        user = self.user_repo.get(user_id)
        if not user:
            raise ValueError("User not found")

        user.update(data)  # Actualiza los atributos del objeto usuario
        self.user_repo.update(user)  # Actualiza el repositorio en memoria
        return user

    def get_all_users(self):
        """Obtiene todos los usuarios del repositorio"""
        return self.user_repo.get_all()

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

    def update_amenity(self, amenity_id, data):
        """Actualiza una amenidad"""
        amenity = self.get_amenity(amenity_id)
        amenity.update(data)
        self.amenity_repo.update(amenity)
        return amenity

    # --- Métodos para gestionar lugares ---
    def create_place(self, place_data):
        """Crea un lugar y lo guarda en el repositorio"""
        # Verificar si el dueño es válido
        owner = self.user_repo.get(place_data['owner'])
        if not owner:
            raise ValueError("Invalid user ID for owner")

        place_data['owner'] = owner

        # Verificar las amenidades (si las hay)
        if 'amenities' in place_data:
            amenities = [self.amenity_repo.get(amenity_id) for amenity_id in place_data['amenities']]
            if None in amenities:
                raise ValueError("One or more amenity IDs are invalid")
            place_data['amenities'] = amenities

        # Crear el lugar usando los datos proporcionados
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """Obtiene un lugar por su ID"""
        place = self.place_repo.get(place_id)
        if place is None:
            raise ValueError("Place not found")
        return place

    def get_all_places(self, filters=None):
        """Obtiene todos los lugares, opcionalmente aplicando filtros"""
        if filters:
            return self.place_repo.filter_by(filters)
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """Actualiza los datos de un lugar"""
        place = self.place_repo.get(place_id)
        if place is None:
            raise ValueError("Place not found")

        # Verificar si el dueño es válido
        if 'owner' in place_data:
            owner = self.user_repo.get(place_data['owner'])
            if not owner:
                raise ValueError("Invalid user ID for owner")
            place_data['owner'] = owner

        # Actualizar el lugar con los nuevos datos
        place.update(place_data)
        self.place_repo.update(place)
        return place

    # --- Métodos para gestionar reviews ---
    def create_review(self, review_data):
        """Crea una nueva reseña y la guarda"""
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        """Obtiene una reseña por su ID"""
        return self.review_repo.get(review_id)
