from flask import jsonify

from src.app.exceptions.auth_exc import (
    RegisterInsertionError, RegisterDuplicateDataError
)

def register_auth_error_handlers(bp):
    @bp.errorhandler(RegisterInsertionError)
    def handle_register_insertion_error(err):
        return jsonify(err.to_dict()), err.status_code

    @bp.errorhandler(RegisterDuplicateDataError)
    def handle_register_duplicate_data_error(err):
        return jsonify(err.to_dict()), err.status_code
    return bp