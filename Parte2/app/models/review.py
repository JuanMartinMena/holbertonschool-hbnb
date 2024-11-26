from app.models.base_for_all import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = self.validate_rating(rating)
        self.place = place  # Referencia a Place
        self.user = user  # Referencia a User

    def validate_rating(self, rating):
        if 1 <= rating <= 5:
            return rating
        raise ValueError("Rating must be between 1 and 5.")
