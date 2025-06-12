from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from src.app.schemas.auth_sch import user_schema
from src.app.handlers.auth_err import register_auth_error_handlers
from src.app.exceptions.auth_exc import *
from src.app.services.auth_svc import AuthService
from src.app.utils.encryption import Encryption

auth_bp = Blueprint(
    'auth', __name__, url_prefix="/api/v1/auth"
)

register_auth_error_handlers(auth_bp)

@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        validated_data = user_schema.load(request.json)
        validated_data["password"] = Encryption.encrypt_password(validated_data["password"])
    except ValidationError as err:
        raise RegisterInsertionError(err.messages)

    try:
        result = AuthService.insert_user(validated_data)
    except IntegrityError as err:
        raise RegisterDuplicateDataError(str(err.orig))

    if result:
        return jsonify({
            "status": "success.",
            "message": "User added successfully.",
        }), 201
    else:
        return jsonify({
            "status": "error.",
            "message": "Undefined Error."
        })

@auth_bp.route("/login", methods=["POST"])
def login_user(): pass
