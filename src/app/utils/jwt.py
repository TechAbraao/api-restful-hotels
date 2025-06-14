import jwt, datetime, os

from src.app.settings.app_settings import app_settings

class JWT:
    @staticmethod
    def generate_token(email: str) -> str:
        """
        Generates a JWT token.
        """
        payload = {
            "sub": email,
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        return jwt.encode(payload, app_settings.secret_key, algorithm="HS256")