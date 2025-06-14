from flask import Flask
from dotenv import load_dotenv

from src.app.router.routes import all_routes
from src.app.settings.app_settings import AppSettings

load_dotenv()
def create_app(settings: AppSettings):
    app = Flask(
        __name__,
        template_folder="templates/",
        static_folder="static/"
    )

    app.config['DEBUG'] = settings.debug
    app.config["SECRET_KEY"] = settings.secret_key

    for bp in all_routes:
        app.register_blueprint(bp)

    return app
