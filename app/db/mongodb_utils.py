from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import get_settings
from app.db.mongodb import db

settings = get_settings()


async def connect():
    logger.info("Connecting to MongoDB...")
    mongo_url = f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASS}@{settings.MONGO_HOST}:{settings.MONGO_PORT}/{settings.MONGO_DB}"
    db.client = AsyncIOMotorClient(mongo_url)
    logger.info("Connected to MongoDB")


async def close_connection():
    logger.info("Closing connection with MongoDB...")
    db.client.close()
    logger.info("Closed connection")
