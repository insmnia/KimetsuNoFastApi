from fastapi import APIRouter
from .endpoints.hunters import router as hunters_router
from .endpoints.teachers import router as teachers_router

router = APIRouter()
router.include_router(hunters_router)
router.include_router(teachers_router)