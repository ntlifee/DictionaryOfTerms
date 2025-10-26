from fastapi import APIRouter
from src.routers.terms import router as term_routers
from src.routers.audio import router as audio_router
from src.routers.images import router as images_router

router = APIRouter()

router.include_router(term_routers, tags=['Terms'])
router.include_router(audio_router, tags=['Audios'])
router.include_router(images_router, tags=['Images'])
