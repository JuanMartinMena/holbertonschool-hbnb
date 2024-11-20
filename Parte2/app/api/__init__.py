# app/api/v1/__init__.py

from flask import Blueprint
from flask_restx import Api

# Importa los namespaces de los distintos módulos (users, amenities, etc.)
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns

# Crea un Blueprint para la versión 1 de la API
blueprint = Blueprint('api_v1', __name__, url_prefix='/api/v1')

# Crea una instancia de Flask-RESTx Api
api = Api(
    blueprint,
    title='HBNB API',
    version='1.0',
    description='API for the HBNB application'
)

# Registra los namespaces en la API bajo el Blueprint
api.add_namespace(users_ns, path='/users')
api.add_namespace(amenities_ns, path='/amenities')
api.add_namespace(places_ns, path='/places')
api.add_namespace(reviews_ns, path='/reviews')
