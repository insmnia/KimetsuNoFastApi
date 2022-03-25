from fastapi import APIRouter

router = APIRouter()

@router.post('/admin/')
async def maintaince_mod(
        on: bool
):
    with open('maintaince.txt','w') as f:
        f.write(str(int(on)))

    return {'Maintaince':on}