from typing import List
from app.core.config import get_settings, hunters_collection_name
from motor.motor_asyncio import AsyncIOMotorClient
from app.models.hunter import Hunter, HunterInDB
from app.core.utils import OID

settings = get_settings()


class HunterCRUD:
    @staticmethod
    async def create(
            conn: AsyncIOMotorClient,
            hunter: Hunter
    ) -> Hunter:
        doc_hunter = hunter.dict()
        await conn[settings.MONGO_DB][hunters_collection_name].insert_one(doc_hunter)
        return Hunter(**doc_hunter)

    @staticmethod
    async def retrieve(
            conn: AsyncIOMotorClient,
            id: OID
    ) -> Hunter:
        hunter = await conn[settings.MONGO_DB][hunters_collection_name].find_one({"_id": id})
        return Hunter(**hunter)

    @staticmethod
    async def list(
            conn: AsyncIOMotorClient
    ) -> List[HunterInDB]:
        hunters: List[HunterInDB] = []
        rows = conn[settings.MONGO_DB][hunters_collection_name].find({})

        async for row in rows:
            hunters.append(
                HunterInDB(**row)
            )
        return hunters

    @staticmethod
    async def delete(
            conn: AsyncIOMotorClient,
            id: OID
    ):
        await conn[settings.MONGO_DB][hunters_collection_name].delete_one({"_id": id})
