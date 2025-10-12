from typing import Optional
from pydantic import BaseModel, Field


class IdSchema(BaseModel):
    id: str = Field(description="Идентификатор термина")


class TermAddSchema(BaseModel):
    name: str = Field(description="Термин")
    definition: str = Field(description="Определение термина")
    image_name: Optional[str] = Field(None, description="Название изображения")
    audio_name: Optional[str] = Field(None, description="Название аудиофайла")


class TermSchema(TermAddSchema, IdSchema):
    class Config:
        from_attributes = True
