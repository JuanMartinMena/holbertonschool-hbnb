from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Registrar el namespace de usuarios
    api.add_namespace(users_ns, path='/api/v1/users')
    
    return app
