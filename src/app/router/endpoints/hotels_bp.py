from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from src.app.exceptions.hotels_exc import *
from src.app.handlers.hotels_err import register_hotel_error_handlers
from src.app.services.hotel_svc import HotelService

hotels_bp = Blueprint('hotels', __name__, url_prefix="/api/hotels")

register_hotel_error_handlers(hotels_bp)

@hotels_bp.route("/", methods=["GET"])
def get_hotels():
    page = request.args.get("page", type=int)
    per_page = request.args.get("per_page", type=int)

    if page is not None and per_page is not None:
        data = HotelService.get_paginated_hotels(page, per_page)
        return jsonify({
            "status": "success",
            "total": data["total"],
            "total_pages": data["pages"],
            "page": data["page"],
            "message": "List of all hotels.",
            "data": data["data"]
        }), 200
    else:
        data = HotelService.get_all_hotels()
        return jsonify({
            "status": "success",
            "total": len(data["data"]),
            "total_pages": 1,
            "page": 1,
            "message": "List of all hotels.",
            "data": data["data"]
        }), 200

@hotels_bp.route("/<string:id>", methods=["GET"])
def get_hostel_by_id(id: int):
    try:
        id = int(id)
    except ValueError:
        raise IndexNotIntegerError()

    if id <= 0:
        raise HotelIndexZeroError()

    data = HotelService.get_hotel_by_id(id)

    if not data:
        raise HotelNotFound(f"Hotel with ID {id} not found.")

    return jsonify({
        "status": "success",
        "message": f"Details for Hotel ID {id}.",
        "data": data
    }), 200

@hotels_bp.route("/", methods=["POST"])
def post_hotel():
    data = request.json
    if not data:
        raise HotelInsertionError("Failed to insert hotel.")

    try:
        data = HotelService.post_hotel(data)
    except IntegrityError as err:
        raise HotelDuplicateDataError(str(err.orig))

    return jsonify({
        "status": "success",
        "message": "Hotel created successfully",
        "data": data
    }), 201


@hotels_bp.route("/<int:id>", methods=["DELETE"])
def delete_hotel_by_id(id: int): pass

@hotels_bp.route("/err", methods=["GET"])
def hotels_model_err():
    raise HotelsInternalError("Something went wrong in hotels logic.")
