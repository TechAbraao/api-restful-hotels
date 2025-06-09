from flask import Blueprint, jsonify, request

from src.app.exceptions.hotels_ex import HotelNotFound, HotelsInternalError, HotelInsertionError
from src.app.schemas.hotels import hotel_schema, hotels_schema
from src.app.handlers.hotels_err import register_hotel_error_handlers
from src.app.services.hotel_svc import HotelService

hotels_bp = Blueprint('hotels', __name__, url_prefix="/api/hotels")

register_hotel_error_handlers(hotels_bp)

@hotels_bp.route("/", methods=["GET"])
def get_hotels():
    data = HotelService.get_hotels()

    result = hotels_schema.dump(data)
    return jsonify({
        "status": "success",
        "count": len(data),
        "message": "List of all hotels.",
        "data": result
    }), 200


@hotels_bp.route("/<int:id>", methods=["GET"])
def get_hostels_by_id(id: int):
    data = HotelService.get_hotel_by_id(id)

    if not data:
        raise HotelNotFound(f"Hotel with ID {id} not found.")

    result = hotel_schema.dump(data)
    return jsonify({
        "status": "success",
        "message": f"Details for Hotel ID {id}.",
        "data": result
    }), 200


@hotels_bp.route("/", methods=["POST"])
def post_hotel():
    data = request.json
    if not data:
        raise HotelInsertionError("Failed to insert hotel.")

    new_hotel = HotelService.post_hotel(data)

    result = hotel_schema.dump(new_hotel)
    return jsonify({
        "status": "success",
        "message": "Hotel created successfully",
        "data": result
    }), 201


@hotels_bp.route("/<int:id>", methods=["DELETE"])
def delete_hotel_by_id(id: int): pass

@hotels_bp.route("/err", methods=["GET"])
def hotels_model_err():
    raise HotelsInternalError("Something went wrong in hotels logic.")
