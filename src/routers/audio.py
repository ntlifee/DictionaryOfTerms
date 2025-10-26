from fastapi import APIRouter, UploadFile
from fastapi.params import Depends, File

from src.routers.dependencies import files_services
from src.services.file import FileService

router = APIRouter()

@router.post("/audios")
async def add_audio(
        audio: UploadFile = File(...),
        file_services: FileService = Depends(files_services)
) -> dict[str, str]:
    audio_name = await file_services.save_audio(audio)
    return {"audio_name": audio_name}
