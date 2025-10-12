from sqlalchemy.orm import Mapped
from src.database import Base, str_pk


class Image(Base):
    id: Mapped[str_pk]
