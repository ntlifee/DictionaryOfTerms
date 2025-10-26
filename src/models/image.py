from sqlalchemy.orm import Mapped, relationship
from src.database import Base, str_pk


class Image(Base):
    id: Mapped[str_pk]

    # Relationship с Term
    terms: Mapped[list['Term']] = relationship(back_populates="image")
