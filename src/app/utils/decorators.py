from functools import wraps
from src.app.settings.db_session import session

def with_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        db_session = session()
        try:
            result = func(db_session, *args, **kwargs)
            db_session.commit()
            return result
        except Exception:
            db_session.rollback()
            raise
        finally:
            db_session.close()
    return wrapper