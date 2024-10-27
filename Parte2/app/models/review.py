from app.models import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id  # Almacena el ID del lugar
        self.user_id = user_id  # Almacena el ID del usuario
