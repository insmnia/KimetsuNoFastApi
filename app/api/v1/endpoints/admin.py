from fastapi import APIRouter
from app.core.config import get_settings

router = APIRouter()
settings = get_settings()


@router.post('/admin/')
async def maintaince_mod(
        on: bool
):
    settings.MAINTAINCE_MODE = int(on)

    return {'Maintaince': on}
