from fastapi import APIRouter
from .registerSvc import router as register_router
from .playerSvc import router as player_router
from .eventManagerSvc import router as event_manager_router


router = APIRouter()
router.include_router(register_router)
router.include_router(player_router)
router.include_router(event_manager_router)
