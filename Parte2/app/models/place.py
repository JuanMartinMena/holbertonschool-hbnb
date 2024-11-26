# models/place.py
from app.models.base_for_all import BaseModel
from app.models.user import User
from app.models.amenity import Amenity

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=None):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = amenities if isinstance(amenities, list) else []  # Default to empty list if None

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be a numeric value")
        if value < 0:
            raise ValueError("Price must be a non-negative value")
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180")
        self._longitude = value

    def add_amenity(self, amenity_id):
        if amenity_id not in self.amenities:
            self.amenities.append(amenity_id)

    def remove_amenity(self, amenity_id):
        if amenity_id in self.amenities:
            self.amenities.remove(amenity_id)
