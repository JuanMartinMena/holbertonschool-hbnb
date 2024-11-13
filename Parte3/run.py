from app import create_app
from app.api import blueprint as api_blueprint

app = create_app()
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run()
