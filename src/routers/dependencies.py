from src.repositories.terms import TermsRepository
from src.services.terms import TermsService


def terms_services() -> TermsService:
    return TermsService(TermsRepository())
