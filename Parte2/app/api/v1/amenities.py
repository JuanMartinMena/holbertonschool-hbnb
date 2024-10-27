from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        # Create a new amenity using the provided data
        data = api.payload  # This gets the incoming JSON data
        try:
            new_amenity = facade.create_amenity(data)
            return new_amenity, 201
        except Exception as e:
            return {'message': str(e)}, 400  # Return any error messages

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = facade.get_all_amenities()
        return amenities, 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity_by_id(amenity_id)
        if not amenity:
            return {'message': 'Amenity not found'}, 404
        return amenity, 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        # Get the amenity from the repository
        amenity = facade.get_amenity_by_id(amenity_id)
        if not amenity:
            return {'message': 'Amenity not found'}, 404

        # Update the amenity with the provided data
        data = api.payload  # This gets the incoming JSON data
        try:
            amenity.update(data)  # Assuming the update method exists in your model
            return {'message': 'Amenity updated successfully'}, 200
        except Exception as e:
            return {'message': str(e)}, 400  # Return any error messages
