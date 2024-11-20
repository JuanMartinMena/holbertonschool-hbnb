from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from app.services.facade import HBnBFacade

api = Namespace('amenities', description='Amenity operations')

# Modelo de Amenity para validación de entrada
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

facade = HBnBFacade()  # Crear la instancia de HBnBFacade

@api.route('/')
class AmenityList(Resource):
    # Método para registrar una nueva amenidad
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Registrar una nueva amenidad"""
        data = request.json
        try:
            # Llamada al servicio para crear una nueva amenidad
            new_amenity = facade.create_amenity(data)
            # Devuelve el diccionario de la nueva amenidad y el código de estado
            return new_amenity.to_dict(), 201
        except ValueError as e:
            # Manejo de errores en caso de datos inválidos
            return {'message': str(e)}, 400

    # Método para obtener todas las amenidades
    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Obtener todas las amenidades"""
        try:
            amenities = facade.get_all_amenities()
            # Devuelve la lista de amenidades
            return jsonify([amenity.to_dict() for amenity in amenities])
        except Exception as e:
            # Manejo de errores en caso de fallo en la consulta
            return {'message': str(e)}, 500


@api.route('/<string:amenity_id>')
class Amenity(Resource):
    # Método para obtener los detalles de una amenidad por ID
    @api.response(200, 'Amenity retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Obtener los detalles de una amenidad"""
        try:
            amenity = facade.get_amenity(amenity_id)
            if amenity:
                return jsonify(amenity.to_dict())
            return {'message': 'Amenity not found'}, 404
        except Exception as e:
            # Manejo de errores en caso de fallo en la consulta
            return {'message': str(e)}, 500

    # Método para actualizar una amenidad existente por ID
    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(400, 'Invalid input data')
    @api.response(404, 'Amenity not found')
    def put(self, amenity_id):
        """Actualizar la información de una amenidad"""
        data = request.json
        try:
            # Llamada al servicio para actualizar la amenidad
            updated_amenity = facade.update_amenity(amenity_id, data)
            if updated_amenity:
                # Devuelve la amenidad actualizada
                return updated_amenity.to_dict(), 200
            return {'message': 'Amenity not found'}, 404
        except ValueError as e:
            # Manejo de errores en caso de datos inválidos
            return {'message': str(e)}, 400
        except Exception as e:
            # Manejo de errores generales
            return {'message': str(e)}, 500
