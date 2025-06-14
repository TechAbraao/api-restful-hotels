from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class AppSettings:
    host: str
    port: int
    debug: bool
    secret_key: str

    @classmethod
    def from_env(cls):
        return cls(
            host=os.getenv("FLASK_RUN_HOST", "127.0.0.1"),
            port=int(os.getenv("FLASK_RUN_PORT", 4040)),
            debug=os.getenv("FLASK_DEBUG", "False").lower() in ("true", "1", "yes"),
            secret_key=os.getenv("SECRET_KEY", "default-unsafe-secret")
        )

app_settings = AppSettings.from_env()