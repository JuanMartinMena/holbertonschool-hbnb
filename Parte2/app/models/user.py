from app.models.base_for_all import BaseModel

class User(BaseModel):
    """Clase que representa un usuario en el sistema."""
    
    def __init__(self, first_name, last_name, email, is_admin=False, id=None):
        super().__init__(id=id)  # Llamar al constructor de BaseModel

        # Validaciones
        if not isinstance(first_name, str) or not first_name:
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(last_name, str) or not last_name:
            raise ValueError("El apellido debe ser una cadena no vacía.")
        if not isinstance(email, str) or not email:
            raise ValueError("El correo electrónico debe ser una cadena no vacía.")
        if not isinstance(is_admin, bool):
            raise ValueError("is_admin debe ser un valor booleano.")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

    def to_dict(self):
        """Convertir el objeto a un diccionario serializable a JSON, incluyendo los atributos del User"""
        user_dict = super().to_dict()  # Obtener el dict de BaseModel
        user_dict.update({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin,
        })
        return user_dict
