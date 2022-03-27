from typing import List

from app.core.config import hunters_collection_name, teachers_collection_name
from app.models.hunter import HunterBase, HunterBaseInDB, HunterFull
from core.utils import OID
from .mixins import CRUDMixin
from motor.motor_asyncio import AsyncIOMotorClient


class HunterCRUD(CRUDMixin):
    Collection = hunters_collection_name
    CreateScheme = HunterBase
    RetrieveScheme = HunterBase
    RetrieveDBScheme = HunterBaseInDB
    FullRetrieveScheme = HunterFull

    @classmethod
    async def get_full_info_hunters(
            cls,
            conn: AsyncIOMotorClient
    ) -> List[HunterFull]:
        hunters = await conn[cls.db_name][cls.Collection].find({})
        print(hunters)
        return []

    @classmethod
    async def create_hunter_with_teacher(
            cls,
            conn: AsyncIOMotorClient,
            hunter: HunterBase,
            teacher_id: OID,
    ):
        data = hunter.dict()
        data['teacher'] = {
            "$ref": teachers_collection_name,
            "$id": teacher_id
        }
        await conn[cls.db_name][cls.Collection].insert_one(data)

