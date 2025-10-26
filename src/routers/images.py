from fastapi import APIRouter, UploadFile
from fastapi.params import Depends, File

from src.routers.dependencies import files_services
from src.services.file import FileService

router = APIRouter()

@router.post("/images")
async def add_image(
        image: UploadFile = File(...),
        file_services: FileService = Depends(files_services)
) -> dict[str, str]:
    image_name = await file_services.save_image(image)
    return {"image_name": image_name}
