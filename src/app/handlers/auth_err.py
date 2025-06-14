from flask import jsonify

from src.app.exceptions.auth_exc import (
    RegisterDataValidationError, RegisterDuplicateDataError, RegisterInternalError, LoginDataValidationError,
    EmailNonExistentError, PasswordVerificationError
)

def register_auth_error_handlers(bp):
    @bp.errorhandler(RegisterDataValidationError)
    def handle_register_insertion_error(err):
        return jsonify(err.to_dict()), err.status_code

    @bp.errorhandler(RegisterDuplicateDataError)
    def handle_register_duplicate_data_error(err):
        return jsonify(err.to_dict()), err.status_code

    @bp.errorhandler(RegisterInternalError)
    def handle_register_internal_error(err):
        return jsonify(err.to_dict()), err.status_code

    @bp.errorhandler(LoginDataValidationError)
    def handle_login_data_validation_error(err):
        return jsonify(err.to_dict()), err.status_code

    @bp.errorhandler(EmailNonExistentError)
    def handle_email_nonexistent_error(err):
        return jsonify(err.to_dict()), err.status_code

    @bp.errorhandler(PasswordVerificationError)
    def handle_password_verification_error(err):
        return jsonify(err.to_dict()), err.status_code

    return bp