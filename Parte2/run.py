from app import create_app  # Importa la función que crea la aplicación
from app.api import blueprint as api_blueprint  # Importa el blueprint que define las rutas de la API

# Crea la aplicación usando la función create_app()
app = create_app()

# Registra el blueprint en la aplicación
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    # Ejecuta la aplicación en modo de desarrollo
    app.run(debug=True)  # Aquí se puede configurar 'debug' según sea necesario
