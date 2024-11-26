from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from flask import jsonify

class HBnBFacade:
    def __init__(self):
        # Usamos los repositorios correctos para cada entidad
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Métodos relacionados con los usuarios
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        updated_user = self.user_repo.update(user_id, user_data)
        return updated_user
    
    # Métodos relacionados con los amenities
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None
        for key, value in amenity_data.items():
            setattr(amenity, key, value)
        self.amenity_repo.update(amenity_id, amenity_data)
        return amenity
    
    # Métodos relacionados con los lugares (places)
    def create_place(self, place_data):
        # Verificar si el dueño (owner) existe
        user = self.user_repo.get(place_data['owner_id'])

        # Si el owner no existe, crear un nuevo usuario (owner)
        if not user:
            owner_data = {
                'first_name': place_data.get('owner_first_name', 'Unknown'),
                'last_name': place_data.get('owner_last_name', 'Unknown'),
                'email': place_data.get('owner_email', 'default@example.com')
            }
            user = self.create_user(owner_data)  # Crear al owner

        # Obtener las amenidades, si están presentes en place_data
        amenities = []
        if 'amenities' in place_data:
            amenities = [self.amenity_repo.get(amenity_id) for amenity_id in place_data['amenities']]

        # Crear el lugar (Place)
        place = Place(
            title=place_data['title'],
            description=place_data.get('description', ''),
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
            owner_id=user.id,  # Asignar el ID del usuario (owner)
            amenities=amenities  # Lista de amenidades, vacía si no hay
        )

        # Añadir el lugar al repositorio
        self.place_repo.add(place)

        # Retorna el diccionario del lugar como JSON con código de estado 201
        return jsonify(place.to_dict()), 201  # Llamamos a `to_dict()` para obtener el formato JSON adecuado

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found")

        # Obtener detalles del owner y las amenidades
        owner = self.user_repo.get(place.owner_id)
        amenities = [self.amenity_repo.get(amenity.id) for amenity in place.amenities]
        return place, owner, amenities

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found")

        # Actualizar los datos del lugar
        place.title = place_data.get('title', place.title)
        place.description = place_data.get('description', place.description)
        place.price = place_data.get('price', place.price)
        place.latitude = place_data.get('latitude', place.latitude)
        place.longitude = place_data.get('longitude', place.longitude)

        self.place_repo.update(place_id, place_data)
        return place
