from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext

from app.core.config import MONGO_DB as db_name, users_collection_name
from app.models.user import UserInDB


class UserService:
    context: CryptContext = CryptContext(schemes=['bcrypt'], deprecated='auto')

    @classmethod
    async def verify_password(cls, plain_pass, hashed_pass) -> bool:
        return cls.context.verify(plain_pass, hashed_pass)

    @classmethod
    async def get_password_hash(cls, password):
        return cls.context.hash(password)

    @staticmethod
    async def get_user(
            conn: AsyncIOMotorClient,
            username: str
    ) -> UserInDB:
        user = await conn[db_name][users_collection_name].find_one({"username": username})
        if user:
            return UserInDB(**user)

    @classmethod
    async def authenticate_user(
            cls,
            conn: AsyncIOMotorClient,
            username: str,
            password: str
    ) -> UserInDB:
        db_user = await cls.get_user(conn, username)
        print(password, db_user)
        if not db_user or await cls.verify_password(password, db_user.hashed_password):
            return False
        return db_user
