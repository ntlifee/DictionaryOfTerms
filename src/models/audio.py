from sqlalchemy.orm import Mapped
from src.database import Base, str_pk


class Audio(Base):
    id: Mapped[str_pk]
