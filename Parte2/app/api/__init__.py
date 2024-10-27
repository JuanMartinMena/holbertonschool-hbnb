from flask_restx import Api
from flask import Blueprint
from .v1.amenities import api as amenities_ns
from .v1.users import api as users_ns  # Importa el namespace para usuarios
from .v1.places import api as places_ns  # Importa el namespace para lugares

# Crear un Blueprint para el API
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_bp, version='1.0', title='HBNB API', description='HBNB API documentation')

# Registrar los namespaces de los endpoints
api.add_namespace(amenities_ns)
api.add_namespace(users_ns)  # Registrar el namespace de usuarios
api.add_namespace(places_ns)  # Registrar el namespace de lugares

def init_app(app):
    """Inicializar el API con la aplicación principal de Flask"""
    app.register_blueprint(api_bp)
