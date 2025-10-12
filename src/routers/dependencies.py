from src.repositories.terms import TermsRepository
from src.services.file import FileService
from src.services.terms import TermsService


def terms_services() -> TermsService:
    return TermsService(TermsRepository())

def files_services() -> FileService:
    return FileService()
