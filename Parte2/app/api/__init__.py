from flask_restx import Api
from app.api.v1.amenities import api as amenities_api
from app.api.v1.places import api as places_api
from app.api.v1.reviews import api as reviews_api

# Crea una instancia de la clase Api
api = Api()

# Registrar los Namespaces
api.add_namespace(amenities_api, path='/api/v1/amenities')
api.add_namespace(places_api, path='/api/v1/places')
api.add_namespace(reviews_api, path='/api/v1/reviews')

def init_app(app):
    """Inicializa la API en la aplicación Flask"""
    api.init_app(app)

def create_api(app):
    """Inicializa la API en la aplicación Flask con documentación Swagger"""
    api = Api(app, doc='/swagger')
    api.add_namespace(places_api, path='/api/v1/places')
    api.add_namespace(amenities_api, path='/api/v1/amenities')
    api.add_namespace(reviews_api, path='/api/v1/reviews')
