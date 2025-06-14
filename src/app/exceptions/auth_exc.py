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

class RegisterDataValidationError(AppException):
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

class RegisterInternalError(AppException):
    def __init__(self, message=None, status_code=500):
        super().__init__(message, status_code)

class LoginDataValidationError(AppException):
    def __init__(self, original_message=None, status_code=400):
        msg = "Error logging in"
        if isinstance(original_message, dict):
            if "email" in original_message:
                msg = original_message["email"][0]
            elif "password" in original_message:
                msg = original_message["password"][0]

        super().__init__(msg, status_code)

class EmailNonExistentError(AppException):
    def __init__(self, message="E-mail not found.", status_code=404):
        super().__init__(message, status_code)

class PasswordVerificationError(AppException):
    def __init__(self, message="Invalid credentials.", status_code=400):
        super().__init__(message, status_code)