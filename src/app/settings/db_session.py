from sqlalchemy.orm import sessionmaker
from src.app.settings.db_engine import engine

session = sessionmaker(bind=engine)