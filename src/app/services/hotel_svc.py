from src.app.models.hotel import Hotel
from src.app.utils.decorators import with_session

class HotelService:
    @staticmethod
    @with_session
    def get_hotels(db_session):
        return db_session.query(Hotel).all()

    @staticmethod
    @with_session
    def get_hotel_by_id(db_session, hotel_id):
        return db_session.query(Hotel).filter(Hotel.id == hotel_id).first()

    @staticmethod
    @with_session
    def post_hotel(db_session, hotel_data):
        new_hotel = Hotel(**hotel_data)
        db_session.add(new_hotel)
        db_session.flush()
        return {
            "id": new_hotel.id,
            "name": new_hotel.name,
            "city": new_hotel.city,
            "address": new_hotel.address,
            "stars": new_hotel.stars,
            "phone": new_hotel.phone,
            "email": new_hotel.email,
            "website": new_hotel.website
        }