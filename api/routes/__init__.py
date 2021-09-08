from fastapi import APIRouter

from .infractions import router as infractions_router
from .logs import router as logs_router

router = APIRouter()

router.include_router(infractions_router)
router.include_router(logs_router)
