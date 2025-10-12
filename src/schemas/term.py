from typing import Optional
from pydantic import BaseModel, Field


class TermAddSchema(BaseModel):
    name: str = Field(description="Термин")
    definition: str = Field(description="Определение термина")
    image_name: Optional[str] = Field(None, description="Название изображения")
    audio_name: Optional[str] = Field(None, description="Название аудиофайла")


class TermIdSchema(BaseModel):
    id: int = Field(description="Идентификатор термина")


class TermSchema(TermAddSchema, TermIdSchema):
    class Config:
        from_attributes = True
