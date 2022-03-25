from motor.motor_asyncio import AsyncIOMotorClient
from app.models.user import User
from app.core.config import get_settings, users_collection_name

settings = get_settings()


def create_user(
        conn: AsyncIOMotorClient,
        user: User
):
    doc_user = user.dict()
    await conn[settings.MONGO_DB][users_collection_name].insert_one(doc_user)
