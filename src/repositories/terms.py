from src.models.term import Term
from src.utils.repository import SQLAlchemyRepository


class TermsRepository(SQLAlchemyRepository):
    model = Term
