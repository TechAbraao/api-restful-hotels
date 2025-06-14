from src.app.router.endpoints.hotels_bp import hotels_bp
from src.app.router.endpoints.auth_bp import auth_bp
from src.app.router.endpoints.root_bp import root_bp

all_routes = [
    hotels_bp,
    auth_bp,
    root_bp
]
