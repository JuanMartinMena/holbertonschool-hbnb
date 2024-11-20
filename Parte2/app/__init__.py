from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.places import api as places_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.reviews import api as reviews_ns

def create_app():
    # Crear la aplicación Flask
    app = Flask(__name__)

    # Inicializar la API con Flask-RESTx
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Registrar los namespaces para cada recurso de la API
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    return app
