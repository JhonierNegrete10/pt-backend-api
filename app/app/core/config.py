import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", "secrect.env"),
        env_ignore_empty=True,
        extra="ignore",
    )

    # load_env = load_dotenv("./.env")
    # # to load private secrect api key
    # load_env = load_dotenv("./secrect.env")
    # if not load_env:
    #     print("ERROR: DONT LOAD ENV :: ", __name__)

    OPEN_WEATHER_API_KEY: str = os.getenv("OPEN_WEATHER_API_KEY")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")

    PROJECT_NAME: str = "backend"
    PROJECT_VERSION: str = "0.1"

    MYSQL_DB: str = os.getenv("MYSQL_DB")
    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_SERVER: str = os.getenv("MYSQL_SERVER")
    MYSQL_HOST: str = os.getenv("MYSQL_HOST")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT")

    DATABASE_URL: str = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"

    # DATABASE_URL = "mysql+pymysql://root:examplepassword@mysql:3306/weather_db"

    # print(f"__name__  :  {__name__}")
    # print(f"__DATABASE_URL__  :  {DATABASE_URL}")


settings = Settings()
