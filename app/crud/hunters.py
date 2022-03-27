from typing import List

from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import hunters_collection_name, teachers_collection_name
from app.models.hunter import HunterBase, HunterBaseInDB, HunterFull
from app.models.teacher import TeacherBaseInDB
from core.utils import OID
from .mixins import CRUDMixin


class HunterCRUD(CRUDMixin):
    Collection = hunters_collection_name
    CreateScheme = HunterBase
    RetrieveScheme = HunterBase
    RetrieveDBScheme = HunterBaseInDB
    FullRetrieveScheme = HunterFull

    @classmethod
    async def list_full_info_hunters(
            cls,
            conn: AsyncIOMotorClient
    ) -> List[HunterFull]:
        hunters: List[HunterFull] = []
        rows = conn[cls.db_name][cls.Collection].find({})

        async for row in rows:
            teacher = None
            if row.get('teacher') is not None:
                t = row.pop('teacher')
                teacher = await conn[cls.db_name][teachers_collection_name].find_one(
                    {"_id": t.id}
                )

            hunters.append(
                HunterFull(
                    teacher=TeacherBaseInDB(**teacher) if teacher else None,
                    **row
                )
            )
        return hunters

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
