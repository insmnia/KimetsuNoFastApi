from typing import Any, List

from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import get_settings
from app.core.utils import OID

settings = get_settings()


class CRUDMixin:
    db_name: str = settings.MONGO_DB
    Collection: str
    CreateScheme: Any
    RetrieveScheme: Any
    RetrieveDBScheme: Any

    @classmethod
    async def create(
            cls,
            conn: AsyncIOMotorClient,
            data,
    ):
        doc = data.dict()
        await conn[cls.db_name][cls.Collection].insert_one(doc)
        return cls.RetrieveScheme(doc)

    @classmethod
    async def retrieve(
            cls,
            conn: AsyncIOMotorClient,
            _id: OID
    ):
        data = await conn[cls.db_name][cls.Collection].find_one({"_id": _id})
        return cls.RetrieveDBScheme(**data)

    @classmethod
    async def list(
            cls,
            conn: AsyncIOMotorClient
    ) -> List[Any]:
        result = []
        rows = conn[cls.db_name][cls.Collection].find({})
        async for row in rows:
            result.append(
                cls.RetrieveDBScheme(**row)
            )

        return result

    @classmethod
    async def delete(
            cls,
            conn: AsyncIOMotorClient,
            _id: OID
    ):
        await conn[cls.db_name][cls.Collection].delete_one({"_id": _id})
