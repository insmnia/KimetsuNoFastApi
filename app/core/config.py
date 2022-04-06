from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_HOST: str = 'localhost'
    MONGO_PORT: int = 27017
    MONGO_USER: str = 'admin'
    MONGO_PASS: str = 'admin'
    MONGO_DATABASE: str = 'kimetsu'
    #
    SECRET_KEY: str = 'supersecret'
    ALGORITHM: str = 'HS256'
    TOKEN_EXPIRE_MINUTES: int = 30
    MAINTAINCE_MODE: int = 0

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings() -> Settings:
    return Settings()


hunters_collection_name = 'hunters'
teachers_collection_name = 'teachers'
users_collection_name = 'users'
