import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, id=None):
        self.id = id if id is not None else str(uuid.uuid4())  # Genera un UUID si no se proporciona uno
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Update the updated_at timestamp
