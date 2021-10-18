from fastapi import APIRouter
from .registerSvc import router as register_router


router = APIRouter()
router.include_router(register_router)
