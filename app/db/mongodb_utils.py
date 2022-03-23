import logging
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGODB_URL
from app.db.mongodb import db


async def connect():
    logging.info("Connecting to MongoDB...")
    db.client = AsyncIOMotorClient(MONGODB_URL)
    logging.info("Connected to MongoDB")


async def close_connection():
    logging.info("Closing connection with MongoDB...")
    db.client.close()
    logging.info("Closed connection")
