# app/models/place.py
from app.models.base_for_all import BaseModel
from app.models.amenity import Amenity
from app.models.user import User

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner, amenities=None):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner  # Relación con User
        self.amenities = amenities if amenities else []  # Relación con Amenity

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __repr__(self):
        return f"<Place {self.title}>"
