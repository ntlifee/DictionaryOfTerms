from src.schemas.term import TermAdd

from src.utils.repository import AbstractRepository


class TermsService:
    def __init__(self, term_repo: AbstractRepository):
        self.term_repo: AbstractRepository = term_repo

    async def add_term(self, term: TermAdd):
        term_dict = term.model_dump()
        term_id = await self.term_repo.add_one(term_dict)
        return term_id
