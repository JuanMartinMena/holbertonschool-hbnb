from app.models.base_for_all import BaseModel
from app.models.place import Place
from app.models.user import User

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating

        # Validar que el lugar sea una instancia de Place
        if not isinstance(place, Place):
            raise ValueError("place debe ser una instancia de Place")
        self.place = place

        # Validar que el usuario sea una instancia de User
        if not isinstance(user, User):
            raise ValueError("user debe ser una instancia de User")
        self.user = user
