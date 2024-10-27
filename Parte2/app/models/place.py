from app.models import BaseModel

class Place(BaseModel):
    def __init__(self, id=None, title=None, description=None, price=None, latitude=None, longitude=None, owner_id=None):
        super().__init__(id)
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = []

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be a non-negative float")
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if value < -90 or value > 90:
            raise ValueError("Latitude must be between -90 and 90")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if value < -180 or value > 180:
            raise ValueError("Longitude must be between -180 and 180")
        self._longitude = value

    def add_amenity(self, amenity):
        self.amenities.append(amenity)
