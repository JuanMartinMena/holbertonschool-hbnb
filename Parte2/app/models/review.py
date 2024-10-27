from app.models import BaseModel
from app.models.place import Place
from app.models.user import User

class Review(BaseModel):
    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id  # Almacena el ID del lugar
        self.user_id = user_id  # Almacena el ID del usuario

        # Validar que el lugar y el usuario existen en el repositorio
        if not Place.exists(place_id):
            raise ValueError("El lugar especificado no existe.")
        if not User.exists(user_id):
            raise ValueError("El usuario especificado no existe.")
