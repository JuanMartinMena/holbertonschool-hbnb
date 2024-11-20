from app.models.base_for_all import BaseModel
from app.models.user import User

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.id = str(uuid.uuid4())  # Generar un UUID único para el Place
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        
        # Validar que el owner sea una instancia de User
        if not isinstance(owner, User):
            raise ValueError("El propietario debe ser una instancia de User")
        
        self.owner = owner
        self.reviews = []  # Inicializamos la lista de reseñas
        self.amenities = []  # Inicializamos la lista de amenities

    def add_review(self, review):
        """Agrega una reseña a la lista de reseñas"""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Agrega una amenidad a la lista de amenities"""
        self.amenities.append(amenity)
