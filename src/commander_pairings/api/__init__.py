from fastapi import APIRouter

from .event_operations import router as event_router


router = APIRouter()
router.include_router(event_router)
