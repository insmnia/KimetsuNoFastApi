from motor.motor_asyncio import AsyncIOMotorClient
from app.models.user import User
from app.core.config import MONGO_DB as db_name, users_collection_name


def create_user(
        conn: AsyncIOMotorClient,
        user: User
):
    doc_user = user.dict()
    await conn[db_name][users_collection_name].insert_one(doc_user)
