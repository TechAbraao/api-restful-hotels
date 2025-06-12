from src.app.utils.decorators import with_session
from src.app.models.auth_mdl import Users

class AuthService:
    @staticmethod
    @with_session
    def insert_user(db_session, user_data):
        if user_data:
            new_user = Users(**user_data)
            db_session.add(new_user)
            return True
        return False
