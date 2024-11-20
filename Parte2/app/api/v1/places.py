from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from app.services import facade

api = Namespace('places', description='Place operations')

# Modelo de Place para validación de entrada
place_model = api.model('Place', {
    'name': fields.String(required=True, description='Name of the place'),
    'description': fields.String(required=True, description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night for the place'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'amenities': fields.List(fields.String, description='List of amenity IDs for the place'),
    'user_id': fields.String(required=True, description='ID of the user owning the place')
})

@api.route('/places')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Registrar un nuevo lugar"""
        data = request.json
        try:
            new_place = facade.create_place(data)
            return jsonify(id=new_place.id, name=new_place.name, price=new_place.price), 201
        except ValueError as e:
            return {'message': str(e)}, 400

    @api.response(200, 'Lista de lugares obtenida exitosamente')
    def get(self):
        """Obtener una lista de todos los lugares"""
        places = facade.get_all_places()
        return jsonify([{
            'id': place.id,
            'name': place.name,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude
        } for place in places]), 200

@api.route('/<string:place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Detalles del lugar obtenidos exitosamente')
    @api.response(404, 'Lugar no encontrado')
    def get(self, place_id):
        """Obtener detalles de un lugar por ID"""
        try:
            place = facade.get_place(place_id)
            return jsonify({
                'id': place.id,
                'name': place.name,
                'description': place.description,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude
            }), 200
        except ValueError:
            return {'message': 'Place not found'}, 404

    @api.expect(place_model)
    @api.response(200, 'Lugar actualizado exitosamente')
    @api.response(404, 'Lugar no encontrado')
    @api.response(400, 'Datos de entrada no válidos')
    def put(self, place_id):
        """Actualizar la información de un lugar"""
        data = request.json
        try:
            updated_place = facade.update_place(place_id, data)
            return {'message': 'Place updated successfully'}, 200
        except ValueError as e:
            return {'message': str(e)}, 404 if 'not found' in str(e) else 400
