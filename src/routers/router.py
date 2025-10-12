from fastapi import APIRouter
from src.routers.terms import router as term_routers

router = APIRouter()

router.include_router(term_routers, tags=['TermsApi'])
