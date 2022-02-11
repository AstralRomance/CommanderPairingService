from fastapi import APIRouter
from .analyticSvc import router as decks_router


router = APIRouter()
router.include_router(decks_router)
