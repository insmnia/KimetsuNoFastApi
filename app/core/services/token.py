from datetime import timedelta, datetime

from jose import jwt

from app.core.config import SECRET_KEY, ALGORITHM


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
            key=SECRET_KEY,
            algorithm=ALGORITHM
        )
        return token
