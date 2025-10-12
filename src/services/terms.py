from src.schemas.term import TermAddSchema

from src.utils.repository import AbstractRepository


class TermsService:
    def __init__(self, term_repo: AbstractRepository):
        self.term_repo: AbstractRepository = term_repo

    async def add_term(self, term: TermAddSchema) -> int:
        term_dict = term.model_dump()
        term_id = await self.term_repo.add_one(data=term_dict)
        return term_id

    async def get_all(self) -> list:
        terms = await self.term_repo.find_all()
        return terms

    async def delete(self, item_id: int) -> bool:
        res = await self.term_repo.delete(item_id=item_id)
        return res

    async def update(self, item_id: int, data: TermAddSchema):
        term_dict = data.model_dump()
        res = await self.term_repo.update(item_id=item_id, data=term_dict)
        return res
