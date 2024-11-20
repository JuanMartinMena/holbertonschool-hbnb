import os

class Config:
    """Configuración base para la aplicación"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')  # Clave secreta para sesiones y protección de cookies
    DEBUG = False  # Deshabilita el modo de depuración por defecto

class DevelopmentConfig(Config):
    """Configuración específica para el entorno de desarrollo"""
    DEBUG = True  # Habilita el modo de depuración para desarrollo
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')  # Ejemplo de URI para una base de datos SQLite

class ProductionConfig(Config):
    """Configuración específica para el entorno de producción"""
    DEBUG = False  # Deshabilita el modo de depuración para producción
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://user:password@localhost/prod_db')  # URI para una base de datos en producción

class TestingConfig(Config):
    """Configuración específica para el entorno de pruebas"""
    TESTING = True  # Habilita las configuraciones de prueba
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///test_db.sqlite')  # URI para una base de datos de prueba

# Diccionario que mapea los entornos a las configuraciones
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig  # Entorno por defecto si no se especifica otro
}
