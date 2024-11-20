from app.models import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def to_dict(self):
        """Convierte el objeto Amenity a un diccionario serializable"""
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),  # Asegúrate de que 'created_at' sea un objeto datetime
            'updated_at': self.updated_at.isoformat()   # Similar para 'updated_at'
        }
