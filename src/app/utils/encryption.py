from passlib.hash import bcrypt

class Encryption:
    @staticmethod
    def encrypt_password(password: str) -> str:
        """
        Generates a secure hash for the given password using bcrypt.
        """
        try:
            return bcrypt.hash(password)
        except Exception as err:
            raise ValueError(f"Error generating password hash: {str(err)}")

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        """
        Verifies if the provided password matches the stored hash.

        Uses bcrypt to securely compare a plain text password with its hashed version.
        If they match, returns True; if they differ, returns False.
        """
        try:
            return bcrypt.verify(password, hashed)
        except Exception as err:
            raise ValueError(f"Error comparing password with hash: {str(err)}")