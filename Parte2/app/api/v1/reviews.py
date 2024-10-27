from flask_restx import Namespace, Resource, fields
from app.services import HBnBFacade

# Crear un Namespace para las operaciones de reseñas
api = Namespace('reviews', description='Review operations')

# Definir el modelo de reseña para la validación de entrada y documentación
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user': fields.String(required=True, description='ID of the user'),  # Cambiado de user_id a user
    'place': fields.String(required=True, description='ID of the place')  # Cambiado de place_id a place
})

# Instanciar el facade para manejar las operaciones de reseñas
facade = HBnBFacade()

# Definir el recurso para la lista de reseñas
@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Registrar una nueva reseña"""
        data = api.payload
        try:
            review = facade.create_review(data)
            return review.__dict__, 201
        except ValueError as e:
            return {'message': str(e)}, 400

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Recuperar una lista de todas las reseñas"""
        reviews = facade.get_all_reviews()
        return [review.__dict__ for review in reviews], 200

# Definir el recurso para una reseña específica
@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Obtener detalles de la reseña por ID"""
        review = facade.get_review(review_id)
        if review:
            return review.__dict__, 200
        return {'message': 'Review not found'}, 404

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Actualizar la información de una reseña"""
        data = api.payload
        try:
            review = facade.update_review(review_id, data)
            return {'message': 'Review updated successfully'}, 200
        except ValueError as e:
            return {'message': str(e)}, 404

    @api.response(204, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Eliminar una reseña por ID"""
        try:
            facade.delete_review(review_id)
            return '', 204
        except ValueError as e:
            return {'message': str(e)}, 404

# Definir el recurso para obtener reseñas por lugar
@api.route('/place/<place_id>')
class ReviewByPlace(Resource):
    @api.response(200, 'Reviews retrieved successfully')
    @api.response(404, 'No reviews found for the specified place')
    def get(self, place_id):
        """Obtener reseñas para un lugar específico"""
        reviews = facade.get_reviews_by_place(place_id)
        if reviews:
            return [review.__dict__ for review in reviews], 200
        return {'message': 'No reviews found for the specified place'}, 404
