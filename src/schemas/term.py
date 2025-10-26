from typing import Optional
from pydantic import BaseModel, Field


class IdSchema(BaseModel):
    id: str = Field(description="Идентификатор термина")


class TermAddSchema(BaseModel):
    name: str = Field(description="Термин")
    definition: str = Field(description="Определение термина")
    image_id: Optional[str] = Field(None, description="Идентификатор изображения")
    audio_id: Optional[str] = Field(None, description="Идентификатор аудиофайла")


class TermSchema(TermAddSchema, IdSchema):
    class Config:
        from_attributes = True
