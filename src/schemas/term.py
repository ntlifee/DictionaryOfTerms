from typing import Optional
from pydantic import BaseModel, Field


class TermBase(BaseModel):
    name: str = Field(description="Термин")
    definition: str = Field(description="Определение термина")
    image_name: Optional[str] = Field(None, description="Название изображения")
    audio_name: Optional[str] = Field(None, description="Название аудиофайла")


class Term(TermBase):
    id: int = Field(description="Идентификатор термина")

    class Config:
        from_attributes = True


class TermAdd(TermBase):
    pass
