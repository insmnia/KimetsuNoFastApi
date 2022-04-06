from fastapi import APIRouter
from starlette.status import HTTP_200_OK

from app.core.config import get_settings

router = APIRouter()
settings = get_settings()


@router.post('/admin/')
async def maintaince_mod(
        on: bool
):
    settings.MAINTAINCE_MODE = int(on)

    return {'Maintaince': on}


@router.get('/healthcheck/')
async def healthcheck():
    return HTTP_200_OK
