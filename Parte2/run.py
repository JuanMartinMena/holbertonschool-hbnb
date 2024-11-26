from app import create_app
from app.api import api

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
