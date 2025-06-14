from src.app.utils.decorators import with_session
from src.app.models.auth_mdl import Users
from src.app.schemas.auth_sch import login_schema

class AuthService:
    @staticmethod
    @with_session
    def insert_user(db_session, user_data: dict) -> bool:
        """ Will register the user in the database. """
        if user_data:
            new_user = Users(**user_data)
            db_session.add(new_user)
            return True
        return False

    @staticmethod
    @with_session
    def search_email(db_session, user_email: str) -> tuple[bool, Users | None]:
        """ It will search the e-mail according to the parameters. """
        finding_email = db_session.query(Users).filter_by(email=user_email).first()
        if finding_email:
            validate_email = login_schema.dump(finding_email)
            return True, validate_email["email"]
        return False, None

    @staticmethod
    @with_session
    def search_password_hash_by_email(db_session, user_email) -> str | None:
        """ Searches for the user's password hash by email. """
        finding_hash = db_session.query(Users).filter_by(email=user_email).first()
        if finding_hash:
            validate_data = login_schema.dump(finding_hash)
            return validate_data["password"]
        return None