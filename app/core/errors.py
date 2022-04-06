from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse


async def unauthorized_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=418,
        content={
            "message": exc,
            "additional info": "Try to login before accessing the resource"
        }
    )
