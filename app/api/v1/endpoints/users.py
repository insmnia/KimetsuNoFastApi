from datetime import timedelta

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import get_settings
from app.core.http_exception import credential_exception, unauthorized_exception
from app.core.services.token import TokenService
from app.core.services.user import UserService
from app.db.mongodb import get_database
from app.models.token import Token, TokenData
from app.models.user import User, UserInDB

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='api/v1/token')
router = APIRouter()
settings = get_settings()


async def get_current_user(
        conn: AsyncIOMotorClient = Depends(get_database),
        token: str = Depends(oauth2_scheme)
) -> User:
    try:
        payload = jwt.decode(
            token=token,
            key=settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get('sub')
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception

    user = await UserService.get_user(conn, token_data.username)
    if user is None:
        raise credential_exception
    return User(
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


@router.get('/users/me/', response_model=User)
async def get_user_me(
        current_user: User = Depends(get_current_user)
) -> User:
    return current_user


# FIXME
@router.post('/testuser')
async def test_user(
        conn: AsyncIOMotorClient = Depends(get_database)
):
    await conn['kimetsu']['users'].delete_many({})
    await conn['kimetsu']['users'].insert_one(
        {"username": "admin", "hashed_password": await UserService.get_password_hash("admin")})
