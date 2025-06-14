from src.app import create_app
from src.app.settings.app_settings import app_settings

app = create_app(app_settings)

if __name__ == '__main__':
    app.run(**app_settings.__dict__)
