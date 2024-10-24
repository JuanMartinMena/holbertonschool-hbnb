from Parte2.app.models import BaseModel
from app.models.place import Place
from app.models.user import User

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place  # Validar que el lugar exista
        self.user = user  # Validar que el usuario exista
