from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from src.database import Base, str_pk
from src.schemas.term import TermSchema
from src.models.audio import Audio
from src.models.image import Image

class Term(Base):
    id: Mapped[str_pk]
    name: Mapped[str]
    definition: Mapped[str]
    image_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("images.id", ondelete="SET NULL"), nullable=True
    )
    audio_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("audios.id", ondelete="SET NULL"), nullable=True
    )

    # связи ORM (удобно при запросах)
    image: Mapped[Image] = relationship(back_populates="terms_with_image")
    audio: Mapped[Audio] = relationship(back_populates="terms_with_audio")

    def to_model(self) -> TermSchema:
        return TermSchema(
            id=self.id,
            name=self.name,
            definition=self.definition,
            image_id=self.image_id,
            audio_id=self.audio_id,
        )
