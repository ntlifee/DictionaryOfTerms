from fastapi import APIRouter
from fastapi.params import Depends, Body
from fastapi import HTTPException, status

from src.routers.dependencies import terms_services
from src.schemas.term import TermAddSchema, TermSchema
from src.services.terms import TermsService

router = APIRouter()


@router.post("/terms")
async def add_term(
        term: TermAddSchema,
        term_services: TermsService = Depends(terms_services)
) -> dict[str, str]:
    term_id = await term_services.add_term(term)
    return {"term_id": term_id}


@router.get("/terms")
async def get_terms(
        term_services: TermsService = Depends(terms_services)
) -> list[TermSchema]:
    terms = await term_services.get_all()
    return terms


@router.get("/terms/{term_id}")
async def get_term(
        term_id: str,
        term_services: TermsService = Depends(terms_services)
) -> TermSchema:
    term = await term_services.get_by_id(term_id=term_id)

    if not term:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Термин с ID {term_id} не найден"
        )

    return term


@router.delete("/terms/{term_id}")
async def delete_term(
        term_id: str,
        term_services: TermsService = Depends(terms_services)
) -> dict[str, str]:
    res = await term_services.delete(item_id=term_id)
    if not res:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Термин не найден!"
        )
    return {
        "message": "Термин успешно удален!",
    }


@router.put("/terms/{term_id}")
async def update_term(
        term_id: str,
        data: TermAddSchema = Body(),
        term_services: TermsService = Depends(terms_services)
) -> dict[str, str]:
    res = await term_services.update(item_id=term_id, data=data)
    if not res:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Термин не найден!"
        )
    return {
        "message": "Термин успешно обновлен!",
    }
