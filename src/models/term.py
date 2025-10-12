from sqlalchemy.orm import Mapped
from src.database import Base, int_pk, str_null_true
from src.schemas.term import TermSchema


class Term(Base):
    id: Mapped[int_pk]
    name: Mapped[str]
    definition: Mapped[str]
    image_name: Mapped[str_null_true]
    audio_name: Mapped[str_null_true]

    def to_model(self) -> TermSchema:
        return TermSchema(
            id=self.id,
            name=self.name,
            definition=self.definition,
            image_name=self.image_name,
            audio_name=self.audio_name,
        )
