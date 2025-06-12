from passlib.hash import bcrypt

class Encryption:
    @staticmethod
    def encrypt_password(password):
        encry_pass = bcrypt.hash(password)
        return encry_pass
