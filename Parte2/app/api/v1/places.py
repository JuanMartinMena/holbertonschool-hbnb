from flask_restx import Namespace, Resource, fields
from flask import request
from app.services.facade import HBnBFacade

# Instancia del namespace
api = Namespace('places', description='Place operations')

# Instancia de la fachada
facade = HBnBFacade()

# Modelo para validar y documentar los datos de entrada/salida
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenity IDs")
})

# Rutas
@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        data = request.json  # Obtiene el payload JSON enviado en la solicitud
        if not data:
            return {"error": "No input data provided"}, 400

        try:
            place = facade.create_place(data)  # Llama al método en la fachada para crear el lugar
            return place, 201  # Devuelve el lugar creado
        except ValueError as e:
            return {"error": str(e)}, 400  # Maneja errores de validación

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()  # Obtiene todos los lugares desde la fachada
        return places, 200  # Devuelve la lista de lugares

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)  # Obtiene el lugar por ID desde la fachada
        if not place:
            return {"error": "Place not found"}, 404
        return place, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        data = request.json  # Obtiene el payload JSON enviado en la solicitud
        if not data:
            return {"error": "No input data provided"}, 400

        try:
            place = facade.update_place(place_id, data)  # Actualiza el lugar desde la fachada
            return place, 200
        except ValueError as e:
            return {"error": str(e)}, 400  # Maneja errores de validación
        except KeyError:
            return {"error": "Place not found"}, 404
