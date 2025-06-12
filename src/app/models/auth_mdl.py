from sqlalchemy import Column, Integer, String, Date

from src.app.settings.db_base import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    full_name = Column(String)
    phone = Column(String, unique=True)
    birth_date = Column(Date)
    role = Column(String)