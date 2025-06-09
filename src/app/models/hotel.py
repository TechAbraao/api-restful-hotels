from sqlalchemy import Column, Integer, String

from src.app.settings.db_base import Base

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    city = Column(String)
    address = Column(String)
    stars = Column(Integer)
    phone = Column(String)
    email = Column(String)
    website = Column(String)

