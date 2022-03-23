from fastapi import APIRouter

router = APIRouter()


@router.get('/hunters/')
async def get_hunters():
    return {'hunters': []}
