from datetime import timedelta, datetime

from jose import jwt, JWTError

from app.core.config import get_settings
from app.core.http_exception import credential_exception
from app.models.token import TokenData

settings = get_settings()


class TokenService:

    @staticmethod
    async def create_access_token(
            data: dict,
            expires_delta: timedelta = None
    ) -> dict:
        to_encode = data.copy()
        time_expires: datetime = datetime.utcnow()
        if expires_delta:
            time_expires += expires_delta
        else:
            time_expires += timedelta(minutes=30)

        to_encode.update({"exp": time_expires})
        token = jwt.encode(
            claims=to_encode,
            key=settings.SECRET_KEY,
            algorithm=settings.ALGORITHM
        )
        return token

    @staticmethod
    async def get_token_data(token):
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
        return token_data
