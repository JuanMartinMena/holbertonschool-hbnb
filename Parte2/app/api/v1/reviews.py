from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('reviews', description='Operaciones de reseñas')
facade = HBnBFacade()
# Definir el modelo de la reseña para la validación de entrada y documentación
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Texto de la reseña'),
    'rating': fields.Integer(required=True, description='Puntuación del lugar (1-5)'),
    'user_id': fields.String(required=True, description='ID del usuario'),
    'place_id': fields.String(required=True, description='ID del lugar')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Reseña creada con éxito')
    @api.response(400, 'Datos de entrada no válidos')
    def post(self):
        """Registrar una nueva reseña"""
        review_data = api.payload
        try:
            review = facade.create_review(review_data)
            return review.to_dict(), 201
        except ValueError as e:
            return {'message': str(e)}, 400

    @api.response(200, 'Lista de reseñas obtenida con éxito')
    def get(self):
        """Obtener una lista de todas las reseñas"""
        reviews = facade.get_all_reviews()
        return [review.to_dict() for review in reviews], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Detalles de la reseña obtenidos con éxito')
    @api.response(404, 'Reseña no encontrada')
    def get(self, review_id):
        """Obtener detalles de una reseña específica"""
        try:
            review = facade.get_review(review_id)
            return review.to_dict(), 200
        except ValueError as e:
            return {'message': str(e)}, 404

    @api.expect(review_model)
    @api.response(200, 'Reseña actualizada con éxito')
    @api.response(404, 'Reseña no encontrada')
    @api.response(400, 'Datos de entrada no válidos')
    def put(self, review_id):
        """Actualizar la información de una reseña"""
        review_data = api.payload
        try:
            review = facade.update_review(review_id, review_data)
            return {'message': 'Reseña actualizada con éxito'}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

    @api.response(200, 'Reseña eliminada con éxito')
    @api.response(404, 'Reseña no encontrada')
    def delete(self, review_id):
        """Eliminar una reseña"""
        try:
            facade.delete_review(review_id)
            return {'message': 'Reseña eliminada con éxito'}, 200
        except ValueError as e:
            return {'message': str(e)}, 404

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'Lista de reseñas del lugar obtenida con éxito')
    @api.response(404, 'Lugar no encontrado')
    def get(self, place_id):
        """Obtener todas las reseñas de un lugar específico"""
        try:
            reviews = facade.get_reviews_by_place(place_id)
            return [review.to_dict() for review in reviews], 200
        except ValueError as e:
            return {'message': str(e)}, 404
