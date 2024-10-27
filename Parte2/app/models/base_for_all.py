import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, id=None):
        self.id = id if id is not None else str(uuid.uuid4())  # Genera un UUID si no se proporciona uno
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Actualizar el timestamp de updated_at cada vez que se modifica el objeto"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Actualizar los atributos del objeto según el diccionario proporcionado"""
        updated = False
        for key, value in data.items():
            if hasattr(self, key) and getattr(self, key) != value:
                setattr(self, key, value)
                updated = True
        if updated:
            self.save()  # Actualizar el timestamp de updated_at solo si hay cambios

    def to_dict(self):
        """Convertir el objeto a un diccionario serializable a JSON"""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),  # Convierte a ISO 8601
            "updated_at": self.updated_at.isoformat(),  # Convierte a ISO 8601
        }
