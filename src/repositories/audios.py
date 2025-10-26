from src.models.audio import Audio
from src.utils.repository import SQLAlchemyRepository


class AudiosRepository(SQLAlchemyRepository):
    model = Audio
