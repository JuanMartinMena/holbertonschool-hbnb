from app.models import BaseModel

class Amenity(BaseModel):
    def __init__(self, id=None, name=None):
        super().__init__(id)  # BaseModel genera el ID y otros atributos base
        self.name = name

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
