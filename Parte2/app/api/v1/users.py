from flask import request
from flask_restx import Namespace, Resource
from app.services.facade import HBnBFacade

api = Namespace('users', description='Operaciones relacionadas con los usuarios')

facade = HBnBFacade()

@api.route('/')
class UserList(Resource):
    """Clase para manejar operaciones de usuarios"""
    
    def post(self):
        """Crear un nuevo usuario"""
        user_data = request.json  # Obtener datos del usuario
        existing_user = facade.get_user_by_email(user_data['email'])  # Verificar si el usuario ya existe
        if existing_user:
            return {'error': 'Email ya registrado'}, 400  # Manejar error si el email ya está registrado

        new_user = facade.create_user(user_data)  # Crear usuario
        return new_user.to_dict(), 201  # Retornar datos del usuario creado usando to_dict()

    def get(self):
        """Obtener todos los usuarios"""
        users = facade.user_repo.get_all()  # Obtener todos los usuarios
        return [user.to_dict() for user in users], 200  # Retornar lista de usuarios usando to_dict()


@api.route('/<string:user_id>')
class User(Resource):
    """Clase para manejar operaciones de un usuario específico"""
    
    def get(self, user_id):
        """Obtener un usuario por ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'Usuario no encontrado'}, 404  # Manejar error si el usuario no existe
        return user.to_dict(), 200  # Retornar datos del usuario usando to_dict()

    def put(self, user_id):
        """Actualizar un usuario por ID"""
        data = request.json  # Obtener datos a actualizar
        updated_user = facade.update_user(user_id, data)  # Actualizar usuario
        if not updated_user:
            return {'error': 'Usuario no encontrado'}, 404  # Manejar error si el usuario no existe
        return updated_user.to_dict(), 200  # Retornar datos del usuario actualizado usando to_dict()
