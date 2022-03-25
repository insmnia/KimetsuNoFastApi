from typing import List

from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_200_OK

from app.core.utils import OID
from app.crud.teachers import TeacherCRUD
from app.db.mongodb import get_database
from app.models.teacher import Teacher, TeacherInDB

router = APIRouter()


@router.get('/teachers/',response_model=List[TeacherInDB])
async def list_hunters(
        db: AsyncIOMotorClient = Depends(get_database)
) -> List[TeacherInDB]:
    teachers: List[TeacherInDB] = await TeacherCRUD.list(db)
    return teachers


@router.post('/teachers/', response_model=Teacher, status_code=HTTP_201_CREATED)
async def create_hunter(
        teacher: Teacher,
        db: AsyncIOMotorClient = Depends(get_database)
) -> Teacher:
    dbteacher = await TeacherCRUD.create(db, teacher)
    return dbteacher


@router.get('/teachers/{id}', response_model=Teacher, status_code=HTTP_200_OK)
async def retrieve_hunter(
        id: OID,
        db: AsyncIOMotorClient = Depends(get_database)
) -> Teacher:
    dbteacher = await TeacherCRUD.retrieve(db, id)
    if not dbteacher:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"Hunter with <{id=}> not found"
        )

    return dbteacher


@router.put('/teachers/{id}', response_model=Teacher, status_code=HTTP_200_OK)
async def update_hunter(
        teacher: Teacher,
        id: OID,
        db: AsyncIOMotorClient = Depends(get_database),
) -> Teacher:
    pass


@router.delete('/teachers/{id}', status_code=HTTP_200_OK)
async def delete_hunter(
        id: OID,
        db: AsyncIOMotorClient = Depends(get_database)
) -> None:
    await TeacherCRUD.delete(db, id)
