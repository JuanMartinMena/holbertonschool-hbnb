from models.base_for_all import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()  # Inicializa los atributos de BaseModel
        self.title = title  # Título del lugar
        self.description = description  # Descripción detallada del lugar
        self.price = price  # Precio del lugar
        self.latitude = latitude  # Coordenada de latitud
        self.longitude = longitude  # Coordenada de longitud
        self.owner = owner  # Propietario del lugar
        self.reviews = []  # Lista para almacenar reviews relacionadas
        self.amenities = []  # Lista para almacenar amenities relacionadas

    def add_review(self, review):
        """Añade una review al lugar."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Añade un amenity al lugar."""
        self.amenities.append(amenity)
