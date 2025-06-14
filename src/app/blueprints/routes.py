from src.app.blueprints.api.hotels_bp import hotels_bp
from src.app.blueprints.api.auth_users_bp import auth_users_bp

from src.app.blueprints.frontend.views_bp import views_bp

all_routes = [
    hotels_bp,
    auth_users_bp,
    views_bp
]
