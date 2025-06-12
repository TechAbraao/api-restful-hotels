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

class RegisterInsertionError(AppException):
    def __init__(self, message="Failed to insert register user.", status_code=400):
        super().__init__(message, status_code)


class RegisterDuplicateDataError(AppException):
    def __init__(self, original_message=None, status_code=409):
        if original_message:
            if "phone" in original_message.lower():
                msg = "Phone number is already registered."
            elif "email" in original_message.lower():
                msg = "Email is already in use."
            elif "username" in original_message.lower():
                msg = "Username already exists."
            else:
                msg = "Duplicate data found in the registration request."
        else:
            msg = "Duplicate unique data error during registration."

        super().__init__(msg, status_code)
