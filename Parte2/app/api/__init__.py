from flask_restx import Api
from app.api.v1.amenities import api as amenities_api
from app.api.v1.places import api as places_api

# Crea una instancia de la clase Api
api = Api()

# Registrar el Namespace de amenities
api.add_namespace(amenities_api, path='/api/v1/amenities')

def init_app(app):
    """Inicializa la API en la aplicación Flask"""
    api.init_app(app)

def create_api(app):
    api = Api(app, doc='/swagger')
    api.add_namespace(places_api, path='/api/v1/places')