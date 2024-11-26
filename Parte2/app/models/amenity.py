from app.models.base_for_all import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name[:50]  # Máximo 50 caracteres
