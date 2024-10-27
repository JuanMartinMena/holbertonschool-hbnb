from flask_restx import Api
from flask import Blueprint
from .v1.amenities import api as amenities_ns

# Crear un Blueprint para el API
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_bp, version='1.0', title='HBNB API', description='HBNB API documentation')

# Registrar los namespaces de los endpoints
api.add_namespace(amenities_ns)

def init_app(app):
    """Inicializar el API con la aplicación principal de Flask"""
    app.register_blueprint(api_bp)
