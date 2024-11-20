from app.models.base_for_all import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()  # Esto llama al constructor de BaseModel, generando el id automáticamente
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
