from app.models import BaseModel

class Amenity(BaseModel):
    def __init__(self, id=None, name=None):
        super().__init__(id)  # Llama al constructor de BaseModel, pasándole el id
        self.name = name

    def update(self, data):
        if "name" in data:
            name_value = data["name"]
            if name_value:  # Verifica que el valor no sea vacío
                self.name = name_value
            else:
                raise ValueError("Invalid input data: 'name' cannot be empty")
        else:
            raise ValueError("Invalid input data: 'name' field is required")
