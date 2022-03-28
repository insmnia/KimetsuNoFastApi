from datetime import timedelta
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND

from app.core.config import get_settings
from app.core.http_exception import (
    credential_exception,
    unauthorized_exception
)
from app.core.services.token import TokenService
from app.core.services.user import UserService
from app.db.mongodb import get_database
from app.models.token import Token
from app.models.user import UserBase, UserInDB, UserCreate
from app.core.utils import OID
from app.crud.user import UserCRUD

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='api/v1/token')
router = APIRouter()
settings = get_settings()


async def get_current_user(
        conn: AsyncIOMotorClient = Depends(get_database),
        token: str = Depends(oauth2_scheme)
) -> UserBase:
    token_data = await TokenService.get_token_data(token)
    user = await UserService.get_user(conn, token_data.username)
    if user is None:
        raise credential_exception
    return UserBase(
        **user.dict()
    )


@router.post('/token', response_model=Token)
async def login_for_access_token(
        conn: AsyncIOMotorClient = Depends(get_database),
        form_data: OAuth2PasswordRequestForm = Depends()
) -> Token:
    user: UserInDB = await UserService.authenticate_user(
        conn=conn,
        username=form_data.username,
        password=form_data.password
    )
    if not user:
        raise unauthorized_exception
    access_token_expires = timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)
    access_token = await TokenService.create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get('/users/me/', response_model=UserBase)
async def get_user_me(
        current_user: UserBase = Depends(get_current_user)
) -> UserBase:
    return current_user


@router.get('/users/')
async def list_users(
        db: AsyncIOMotorClient = Depends(get_database)
) -> List[UserInDB]:
    users: List[UserInDB] = await UserCRUD.list(db)
    return users


@router.post('/users/',
             response_model=UserCreate,
             status_code=HTTP_201_CREATED
             )
async def create_user(
        user: UserCreate,
        db: AsyncIOMotorClient = Depends(get_database)
) -> UserCreate:
    await UserCRUD.create(db, user)
    return


@router.get('/users/{id}', response_model=UserBase, status_code=HTTP_200_OK)
async def retrieve_user(
        id: OID,
        db: AsyncIOMotorClient = Depends(get_database)
) -> UserBase:
    dbuser = await UserCRUD.retrieve(db, id)
    if not dbuser:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"Hunter with <{id=}> not found"
        )

    return dbuser
