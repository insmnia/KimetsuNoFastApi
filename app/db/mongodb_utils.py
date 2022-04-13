from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import get_settings
from app.db.mongodb import db

settings = get_settings()


async def connect():
    logger.info("Connecting to MongoDB...")
    mongo_url = f"mongodb://" \
                f"{settings.MONGO_USER}:" \
                f"{settings.MONGO_PASS}@" \
                f"{settings.MONGO_HOST}:" \
                f"{settings.MONGO_PORT}/" \
                f"{settings.MONGO_DATABASE}"
    db.client = AsyncIOMotorClient(mongo_url)
    logger.info("Connected to MongoDB")


async def close_connection():
    logger.info("Closing connection with MongoDB...")
    db.client.close()
    logger.info("Closed connection")
