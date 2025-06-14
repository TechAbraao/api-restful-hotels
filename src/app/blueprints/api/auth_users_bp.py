from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from src.app.schemas.auth_sch import register_user_schema, login_user_schema
from src.app.handlers.auth_err import register_auth_users_error_handlers
from src.app.exceptions.auth_exc import *
from src.app.services.auth_svc import AuthService
from src.app.utils.encryption import Encryption
from src.app.utils.jwt import JWT

auth_users_bp = Blueprint('auth', __name__, url_prefix="/api/v1/auth")

register_auth_users_error_handlers(auth_users_bp)

@auth_users_bp.route("/register", methods=["POST"])
def register_user():
    try:
        validated_data = register_user_schema.load(request.json)
        validated_data["password"] = Encryption.encrypt_password(validated_data["password"])
    except ValidationError as err:
        raise RegisterDataValidationError(err.messages)

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
        raise RegisterInternalError(
            "Undefined Error."
        )

@auth_users_bp.route("/login", methods=["POST"])
def login_user():
    try:
        validated_data = login_user_schema.load(request.json)
        email_validated = validated_data["email"]
        password_validated = validated_data["password"]
    except ValidationError as err:
        raise LoginDataValidationError(err.messages)

    email_found, email_value = AuthService.search_email(user_email=email_validated)
    if not email_found or email_value is None:
        raise EmailNonExistentError(
            "E-mail not found."
        )

    hash_found = AuthService.search_password_hash_by_email(email_value)
    if hash_found is None:
        raise PasswordVerificationError(
            "The hash found is None."
        )

    verify_pass_and_hash = Encryption.verify_password(password_validated, hash_found)
    if not verify_pass_and_hash:
        raise PasswordVerificationError(
            "Hash and password are inconsistent."
        )

    token = JWT.generate_token(str(email_value))

    return jsonify({
        "status": "success.",
        "message": "User logged in successfully.",
        "token": token
    })
