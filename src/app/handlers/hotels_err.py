from flask import jsonify

from src.app.exceptions.hotels_exc import (
    HotelNotFound, HotelsInternalError, HotelInsertionError,
    HotelIndexZeroError, IndexNotIntegerError, HotelDuplicateDataError
)

def register_hotel_error_handlers(bp):
    @bp.errorhandler(HotelNotFound)
    def handle_hotel_not_found(err):
        return jsonify(err.to_dict()), err.status_code

    @bp.errorhandler(HotelsInternalError)
    def handle_hotels_internal_error(err):
        return jsonify(err.to_dict()), err.status_code

    @bp.errorhandler(HotelInsertionError)
    def handle_hotel_insertion_error(err):
        return jsonify(err.to_dict()), err.status_code

    @bp.errorhandler(HotelIndexZeroError)
    def handle_hotel_index_zero(err):
        return jsonify(err.to_dict()), err.status_code

    @bp.errorhandler(IndexNotIntegerError)
    def handle_hotel_index_not_integer(err):
        return jsonify(err.to_dict()), err.status_code

    @bp.errorhandler(HotelDuplicateDataError)
    def handle_hotel_duplicate_data_error(err):
        return jsonify(err.to_dict()), err.status_code

    return bp