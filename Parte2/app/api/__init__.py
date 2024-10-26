from flask import Blueprint
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns

# Crea un blueprint para el prefijo /api/v1
blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

# Configura la API de Flask-RESTx
api = Api(
    blueprint,
    title='HBNB API',
    version='1.0',
    description='API for the HBNB application'
)

# Registra los namespaces en el blueprint
api.add_namespace(users_ns, path='/users')
api.add_namespace(amenities_ns, path='/amenities')
