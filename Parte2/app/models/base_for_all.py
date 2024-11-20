import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())  # Genera un UUID único
        self.created_at = datetime.utcnow()  # Asegura que las fechas sean en UTC
        self.updated_at = datetime.utcnow()  # Asegura que las fechas sean en UTC

    def save(self):
        """Actualiza el timestamp de updated_at cada vez que el objeto es modificado"""
        self.updated_at = datetime.utcnow()  # Usar UTC para consistencia

    def update(self, data):
        """Actualiza los atributos del objeto basándose en el diccionario proporcionado"""
        for key, value in data.items():
            if hasattr(self, key):  # Verifica que el atributo exista en el objeto
                setattr(self, key, value)
            else:
                print(f"Warning: Attribute '{key}' does not exist on {self.__class__.__name__}.")
        self.save()  # Actualiza el timestamp de updated_at después de modificar el objeto
    
    def to_dict(self):
        """Convierte el objeto en un diccionario adecuado para JSON"""
        # Asegúrate de que las fechas se conviertan a cadenas de texto para ser serializadas en JSON
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "name": getattr(self, "name", None)  # Asegura que 'name' esté presente si existe en la clase
        }
