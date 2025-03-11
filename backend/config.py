from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    db_password: str
    db_username: str
    db_port: int
    db_name: str
    db_hostname: str

    class config:
        env_file = ".env"

settings = Settings()
