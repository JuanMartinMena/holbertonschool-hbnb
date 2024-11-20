from app.models import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def update(self, amenity_data):
        """Actualiza los atributos de la amenidad"""
        if 'name' in amenity_data:
            self.name = amenity_data['name']

    def to_dict(self):
        """Convierte el objeto Amenity a un diccionario serializable"""
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
