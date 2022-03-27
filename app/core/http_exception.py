from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

credential_exception = HTTPException(
    status_code=HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={
        "WWW-Authenticate": "Bearer"
    }
)

unauthorized_exception = HTTPException(
    status_code=HTTP_401_UNAUTHORIZED,
    detail="Incorrect username or password",
    headers={
        "WWW-Authenticate": "Bearer"
    }
)
