import sys
import os

try:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

    from src.app.settings.db_base import Base
    from src.app.settings.db_engine import engine
    from src.app.models.hotel import Hotel

    Base.metadata.create_all(bind=engine)
    print(" * Database created successfully.")
except Exception as e:
    print(f" * Error occurred while creating the database: {e}")
