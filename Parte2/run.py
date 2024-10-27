from app import create_app
from app.api import api_bp

app = create_app()
app.register_blueprint(api_bp)  # Registrar el blueprint de la API

if __name__ == '__main__':
    # Ejecutar el servidor en modo debug para obtener más información en caso de errores
    app.run(debug=True)
