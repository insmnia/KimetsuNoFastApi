from typing import List

from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_200_OK

from app.core.utils import OID
from app.crud.teachers import TeacherCRUD
from app.db.mongodb import get_database
from app.models.teacher import TeacherBase, TeacherBaseInDB

router = APIRouter()

@router.get('/teachers/', response_model=List[TeacherBaseInDB])
async def list_teachers(
        db: AsyncIOMotorClient = Depends(get_database)
) -> List[TeacherBaseInDB]:
    teachers: List[TeacherBaseInDB] = await TeacherCRUD.list(db)
    return teachers


@router.post('/teachers/', response_model=TeacherBase, status_code=HTTP_201_CREATED)
async def create_teacher(
        teacher: TeacherBase,
        db: AsyncIOMotorClient = Depends(get_database)
) -> TeacherBase:
    dbteacher = await TeacherCRUD.create(db, teacher)
    return dbteacher


@router.get('/teachers/{id}', response_model=TeacherBase, status_code=HTTP_200_OK)
async def retrieve_teacher(
        id: OID,
        db: AsyncIOMotorClient = Depends(get_database)
) -> TeacherBase:
    dbteacher = await TeacherCRUD.retrieve(db, id)
    if not dbteacher:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"Hunter with <{id=}> not found"
        )

    return dbteacher


@router.delete('/teachers/{id}', status_code=HTTP_200_OK)
async def delete_teacher(
        id: OID,
        db: AsyncIOMotorClient = Depends(get_database)
) -> None:
    await TeacherCRUD.delete(db, id)
