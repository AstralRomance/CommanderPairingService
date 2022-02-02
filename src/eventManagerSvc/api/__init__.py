from fastapi import APIRouter
from .eventManagerSvc import router as manager_router


router = APIRouter()
router.include_router(manager_router)
