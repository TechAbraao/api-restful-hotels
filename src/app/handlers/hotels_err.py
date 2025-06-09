from flask import jsonify
from src.app.exceptions.hotels_ex import HotelNotFound, HotelsInternalError, HotelInsertionError

def register_hotel_error_handlers(bp):
    @bp.errorhandler(HotelNotFound)
    def handle_hotel_not_found(err):
        return jsonify(err.to_dict()), err.status_code

    @bp.errorhandler(HotelsInternalError)
    def handle_hotels_internal_error(err):
        return jsonify(err.to_dict()), err.status_code

    @bp.errorhandler(HotelInsertionError)
    def handle_hotels_internal_error(err):
        return jsonify(err.to_dict()), err.status_code