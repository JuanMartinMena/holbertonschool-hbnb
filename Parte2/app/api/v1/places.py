from flask_restx import Namespace, Resource, fields
from app.services import HBnBFacade

api = Namespace('places', description='Place operations')
facade = HBnBFacade()

place_model = api.model('Place', {
    'name': fields.String(required=True, description='Name of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        place_data = api.payload
        new_place = facade.create_place(place_data)
        return {
            'id': new_place.id,
            'name': new_place.name,
            'description': new_place.description,
            'price': new_place.price,
            'latitude': new_place.latitude,
            'longitude': new_place.longitude,
            'owner_id': new_place.owner_id
        }, 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        return [{'id': p.id, 'name': p.name, 'latitude': p.latitude, 'longitude': p.longitude} for p in places], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        try:
            place = facade.get_place(place_id)
            return {
                'id': place.id,
                'name': place.name,
                'description': place.description,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'owner_id': place.owner_id,
            }, 200
        except ValueError:
            return {'message': 'Place not found'}, 404

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        place_data = api.payload
        try:
            facade.update_place(place_id, place_data)
            return {'message': 'Place updated successfully'}, 200
        except ValueError:
            return {'message': 'Place not found'}, 404
