from src.app.models.hotel import Hotel
from src.app.utils.decorators import with_session

from src.app.schemas.hotels import hotel_schema, hotels_schema

class HotelService:
    @staticmethod
    @with_session
    def get_hotels(db_session):
        hotels = db_session.query(Hotel).all()
        return hotels_schema.dump(hotels)

    @staticmethod
    @with_session
    def get_hotel_by_id(db_session, hotel_id):
        hotel = db_session.query(Hotel).filter(Hotel.id == hotel_id).first()
        return hotel_schema.dump(hotel)

    @staticmethod
    @with_session
    def post_hotel(db_session, hotel_data):
        new_hotel = Hotel(**hotel_data)
        db_session.add(new_hotel)
        db_session.flush()
        return hotel_schema.dump(new_hotel)
