from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

# Crear la instancia de HBnBFacade para manejar las operaciones de amenities
facade = HBnBFacade()

# Crear el namespace para los endpoints de amenities
api = Namespace('amenities', description='Amenity operations')

# Definir el modelo de Amenity para validación de entrada y documentación
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
        try:
            # Extraer los datos del JSON enviado en la solicitud
            amenity_data = api.payload
            # Crear un nuevo amenity a través de la capa de fachada
            new_amenity = facade.create_amenity(amenity_data)
            return {'id': new_amenity.id, 'name': new_amenity.name}, 201
        except Exception as e:
            return {'message': str(e)}, 400

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        # Obtener todas las amenities a través de la capa de fachada
        amenities = facade.get_all_amenities()
        return [{'id': amenity.id, 'name': amenity.name} for amenity in amenities], 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        try:
            # Obtener el amenity específico usando el ID
            amenity = facade.get_amenity(amenity_id)
            return {'id': amenity.id, 'name': amenity.name}, 200
        except ValueError:
            return {'message': 'Amenity not found'}, 404

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        try:
            # Extraer datos actualizados desde el JSON de la solicitud
            amenity_data = api.payload
        
            # Actualizar el amenity a través de la fachada
            updated_amenity = facade.update_amenity(amenity_id, amenity_data)
        
            return {'id': updated_amenity.id, 'name': updated_amenity.name}, 200
        except ValueError as e:
            return {'message': str(e)}, 400  # Cambiado a 400 para errores de validación
        except Exception as e:
            return {'message': 'Invalid input data'}, 400  # Asegúrate de que el mensaje sea claro