from typing import List
from app.core.config import MONGO_DB as db_name, hunters_collection_name
from motor.motor_asyncio import AsyncIOMotorClient
from app.models.hunter import Hunter, HunterInDB
from app.core.utils import OID


class HunterCRUD:
    @staticmethod
    async def create(
            conn: AsyncIOMotorClient,
            hunter: Hunter
    ) -> Hunter:
        doc_hunter = hunter.dict()
        await conn[db_name][hunters_collection_name].insert_one(doc_hunter)
        return Hunter(**doc_hunter)

    @staticmethod
    async def retrieve(
            conn: AsyncIOMotorClient,
            id: OID
    ) -> Hunter:
        hunter = await conn[db_name][hunters_collection_name].find_one({"_id": id})
        return Hunter(**hunter)

    @staticmethod
    async def list(
            conn: AsyncIOMotorClient
    ) -> List[HunterInDB]:
        hunters: List[HunterInDB] = []
        rows = conn[db_name][hunters_collection_name].find({})

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
        await conn[db_name][hunters_collection_name].delete_one({"_id": id})
