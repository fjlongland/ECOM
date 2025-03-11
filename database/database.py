from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from backend.config import settings 
import urllib

password = settings.db_password
encoded_password = urllib.parse.quote_plus(password)

#connection url in the form: postgresql://(username):(password)@(hostname):(database port)/(database name)
DB_URL =f"postgresql://{settings.db_username}:{encoded_password}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()