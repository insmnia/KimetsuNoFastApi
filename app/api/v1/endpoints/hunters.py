from typing import List
from app.core.utils import OID
from fastapi import APIRouter, Depends, HTTPException
from app.crud.hunters import HunterCRUD
from app.models.hunter import HunterBase, HunterBaseInDB
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_200_OK
from app.db.mongodb import get_database
from motor.motor_asyncio import AsyncIOMotorClient

router = APIRouter()


@router.get('/hunters/')
async def list_hunters(
        db: AsyncIOMotorClient = Depends(get_database)
) -> List[HunterBaseInDB]:
    hunters: List[HunterBaseInDB] = await HunterCRUD.list_full_info_hunters(db)
    return hunters


@router.post('/hunters/', status_code=HTTP_201_CREATED)
async def create_hunter(
        hunter: HunterBase,
        db: AsyncIOMotorClient = Depends(get_database),
        teacher_id: OID = None,
):
    if teacher_id:
        await HunterCRUD.create_hunter_with_teacher(
            conn=db,
            hunter=hunter,
            teacher_id=teacher_id
        )
        return HTTP_201_CREATED
    await HunterCRUD.create(db, hunter)
    return HTTP_201_CREATED


@router.get('/hunters/{id}',
            response_model=HunterBase,
            status_code=HTTP_200_OK)
async def retrieve_hunter(
        id: OID,
        db: AsyncIOMotorClient = Depends(get_database)
) -> HunterBase:
    dbhunter = await HunterCRUD.retrieve(db, id)
    if not dbhunter:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"Hunter with <{id=}> not found"
        )

    return dbhunter


@router.delete('/hunters/{id}', status_code=HTTP_200_OK)
async def delete_hunter(
        id: OID,
        db: AsyncIOMotorClient = Depends(get_database)
) -> None:
    await HunterCRUD.delete(db, id)
