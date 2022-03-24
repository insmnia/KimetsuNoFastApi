from datetime import timedelta

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import SECRET_KEY, ALGORITHM, TOKEN_EXPIRE_MINUTES
from app.core.http_exception import credential_exception, unauthorized_exception
from app.core.services.token import TokenService
from app.core.services.user import UserService
from app.db.mongodb import get_database
from app.models.token import Token, TokenData
from app.models.user import User, UserInDB

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
router = APIRouter()


async def get_current_user(
        conn: AsyncIOMotorClient = Depends(get_database),
        token: str = Depends(oauth2_scheme)
):
    try:
        payload = jwt.decode(
            token=token,
            key=SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        username: str = payload.get('sub')
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception

    user = UserService.get_user(conn, token_data.username)
    if user is None:
        raise credential_exception
    return user


@router.post('/token', response_model=Token)
async def login_for_access_token(
        conn: AsyncIOMotorClient = Depends(get_database),
        form_data: OAuth2PasswordRequestForm = Depends()
) -> dict:
    user: UserInDB = await UserService.authenticate_user(
        conn=conn,
        username=form_data.username,
        password=form_data.password
    )
    print(user)
    if not user:
        raise unauthorized_exception
    access_token_expires = timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    access_token = TokenService.create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )

    return {
        "access_key": access_token,
        "token_type": "bearer"
    }


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
    print('Created test user')
    print(await UserService.get_password_hash("admin"))
    await conn['kimetsu']['users'].insert_one(
        {"username": "admin2", "hashed_password": await UserService.get_password_hash("admin")})
