import uuid
from app.models.base_for_all import BaseModel
from app.models.user import User
from app.models.amenity import Amenity

class Place(BaseModel):
    """
    Representa un lugar en el sistema.

    Args:
        title (str): Título o nombre del lugar.
        description (str): Descripción del lugar.
        price (float): Precio por noche.
        latitude (float): Latitud de la ubicación.
        longitude (float): Longitud de la ubicación.
        owner (User): Propietario del lugar.
    """
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.id = str(uuid.uuid4())  # Generar un UUID único para el Place
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

        # Validar que el owner sea una instancia válida de User
        if owner is None or not isinstance(owner, User):
            raise ValueError("El propietario debe ser una instancia válida de User")

        self.owner = owner
        self.reviews = []  # Inicializamos la lista de reseñas
        self.amenities = []  # Inicializamos la lista de amenities

    def add_review(self, review):
        """Agrega una reseña a la lista de reseñas"""
        from app.models.review import Review  # Importación dentro de la función
        if not isinstance(review, Review):
            raise ValueError("La reseña debe ser una instancia de Review")
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Agrega una amenidad a la lista de amenities"""
        if not isinstance(amenity, Amenity):
            raise ValueError("La amenidad debe ser una instancia de Amenity")
        self.amenities.append(amenity)
