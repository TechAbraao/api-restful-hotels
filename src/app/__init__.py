from flask import Flask
from dotenv import load_dotenv


from src.app.router.endpoints.hotels_bp import hotels_bp
from src.app.router.endpoints.auth_bp import auth_bp

load_dotenv()
def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    app.register_blueprint(hotels_bp)
    app.register_blueprint(auth_bp)

    return app
