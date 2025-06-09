from sqlalchemy import create_engine

db_url = "sqlite:///src/app/database/database.db"
engine = create_engine(db_url, echo=False)



