import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())  # Genera un UUID único como string
        self.created_at = datetime.now()  # Marca la creación
        self.updated_at = datetime.now()  # Marca la última actualización

    def save(self):
        """Actualiza el timestamp de updated_at."""
        self.updated_at = datetime.now()

    def update(self, data):
        """Actualiza los atributos del objeto según un diccionario de datos."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Asegura que updated_at se actualice
