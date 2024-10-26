from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Modelo de Amenity para validación de entrada
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Registrar una nueva amenidad"""
        data = request.json
        try:
            new_amenity = facade.create_amenity(data)
            return jsonify(id=new_amenity.id, name=new_amenity.name), 201
        except ValueError as e:
            return {'message': str(e)}, 400

    @api.response(200, 'Lista de amenidades obtenida exitosamente')
    def get(self):
        """Obtener una lista de todas las amenidades"""
        amenities = facade.get_all_amenities()
        return jsonify([{'id': amenity.id, 'name': amenity.name} for amenity in amenities]), 200

@api.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Detalles de amenidad obtenidos exitosamente')
    @api.response(404, 'Amenidad no encontrada')
    def get(self, amenity_id):
        """Obtener detalles de una amenidad por ID"""
        try:
            amenity = facade.get_amenity(amenity_id)
            return jsonify(id=amenity.id, name=amenity.name), 200
        except ValueError:
            return {'message': 'Amenity not found'}, 404

    @api.expect(amenity_model)
    @api.response(200, 'Amenidad actualizada exitosamente')
    @api.response(404, 'Amenidad no encontrada')
    @api.response(400, 'Datos de entrada no válidos')
    def put(self, amenity_id):
        """Actualizar la información de una amenidad"""
        data = request.json
        try:
            updated_amenity = facade.update_amenity(amenity_id, data)
            return {'message': 'Amenity updated successfully'}, 200
        except ValueError as e:
            return {'message': str(e)}, 404 if 'not found' in str(e) else 400
