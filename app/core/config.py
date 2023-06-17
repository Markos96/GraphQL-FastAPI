import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Football GraphQL"
    PROJECT_VERSION: str = "1.0"
    POSTGRES_NAME: str = os.getenv("POSTGRES_NAME")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASS: str = os.getenv("POSTGRES_PASS")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"


settings = Settings()
