from flask_restx import Api
from flask import Blueprint
from .v1.amenities import api as amenities_ns  # Namespace para amenities
from .v1.users import api as users_ns  # Namespace para usuarios
from .v1.places import api as places_ns  # Namespace para lugares
from .v1.reviews import api as reviews_ns  # Namespace para reviews

# Crear un Blueprint para el API
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_bp, version='1.0', title='HBNB API', description='HBNB API documentation')

# Registrar los namespaces
api.add_namespace(users_ns)  # Registrar usuarios
api.add_namespace(amenities_ns)  # Registrar amenities
api.add_namespace(places_ns)  # Registrar lugares
api.add_namespace(reviews_ns)  # Registrar reviews

def init_app(app):
    """Inicializar el API con la aplicación principal de Flask"""
    app.register_blueprint(api_bp)  # Registrar el Blueprint en la app principal
