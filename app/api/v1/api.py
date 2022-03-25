from fastapi import APIRouter

# from .endpoints.teachers import router as teachers_router
from app.api.v1.endpoints.users import router as users_router
from .endpoints.hunters import router as hunters_router

router = APIRouter(prefix="/v1")
router.include_router(hunters_router)
router.include_router(users_router)
