from app.models.base_for_all import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name[:50]  # Máximo 50 caracteres
        self.last_name = last_name[:50]   # Máximo 50 caracteres
        self.email = email  # Validación del formato puede ser añadida
        self.is_admin = is_admin
