class AppException(Exception):
    def __init__(self, message="Application error", status_code=500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

    def to_dict(self):
        return {
            "status": "error",
            "message": self.message
        }

class HotelNotFound(AppException):
    def __init__(self, message="Hotel not found.", status_code=404):
        super().__init__(message, status_code)

class HotelsInternalError(AppException):
    def __init__(self, message="Internal error in hotels module.", status_code=500):
        super().__init__(message, status_code)

class HotelInsertionError(AppException):
    def __init__(self, message="Failed to insert hotel.", status_code=400):
        super().__init__(message, status_code)