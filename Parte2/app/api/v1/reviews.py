from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Modelo de Review para validación de entrada
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)', min=1, max=5),
    'place_id': fields.String(required=True, description='ID of the place being reviewed'),
    'user_id': fields.String(required=True, description='ID of the user who wrote the review')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Registrar una nueva reseña"""
        data = request.json
        try:
            new_review = facade.create_review(data)
            return jsonify(id=new_review.id, text=new_review.text, rating=new_review.rating), 201
        except ValueError as e:
            return {'message': str(e)}, 400

    @api.response(200, 'Lista de reseñas obtenida exitosamente')
    def get(self):
        """Obtener una lista de todas las reseñas"""
        reviews = facade.get_all_reviews()
        return jsonify([{
            'id': review.id,
            'text': review.text,
            'rating': review.rating,
            'place_id': review.place_id,
            'user_id': review.user_id
        } for review in reviews]), 200

@api.route('/<string:review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Detalles de la reseña obtenidos exitosamente')
    @api.response(404, 'Reseña no encontrada')
    def get(self, review_id):
        """Obtener detalles de una reseña por ID"""
        try:
            review = facade.get_review(review_id)
            return jsonify({
                'id': review.id,
                'text': review.text,
                'rating': review.rating,
                'place_id': review.place_id,
                'user_id': review.user_id
            }), 200
        except ValueError:
            return {'message': 'Review not found'}, 404

    @api.expect(review_model)
    @api.response(200, 'Reseña actualizada exitosamente')
    @api.response(404, 'Reseña no encontrada')
    @api.response(400, 'Datos de entrada no válidos')
    def put(self, review_id):
        """Actualizar la información de una reseña"""
        data = request.json
        try:
            updated_review = facade.update_review(review_id, data)
            return {'message': 'Review updated successfully'}, 200
        except ValueError as e:
            return {'message': str(e)}, 404 if 'not found' in str(e) else 400
