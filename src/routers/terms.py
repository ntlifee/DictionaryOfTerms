from fastapi import APIRouter
from fastapi.params import Depends

from src.routers.dependencies import terms_services
from src.schemas.term import TermAdd
from src.services.terms import TermsService

router = APIRouter()


@router.post("/term")
async def add_term(
        term: TermAdd,
        term_services: TermsService = Depends(terms_services)
):
    term_id = await term_services.add_term(term)
    return {"term_id": term_id}
