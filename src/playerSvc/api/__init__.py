from fastapi import APIRouter
from .playerSvc import router as players_router


router = APIRouter()
router.include_router(players_router)
