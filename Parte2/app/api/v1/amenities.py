from flask_restx import Namespace, Resource, fields
from flask import request
from app.services.facade import HBnBFacade

api = Namespace('amenities', description='Amenity operations')

# Modelo de Amenity para validación de entrada
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

facade = HBnBFacade()  # Crear la instancia de HBnBFacade

@api.route('/')
class AmenityList(Resource):
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
