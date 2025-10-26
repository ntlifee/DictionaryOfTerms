from src.models.image import Image
from src.utils.repository import SQLAlchemyRepository


class ImagesRepository(SQLAlchemyRepository):
    model = Image
