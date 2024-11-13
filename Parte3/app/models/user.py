from app.models.base_for_all import BaseModel


class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

    def hash_password(self, password):
        self.hash_password = bcrypt.generate_password_hash(password).decode('utf-8')


    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
