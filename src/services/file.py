import os

import aiofiles
import uuid
from fastapi import UploadFile

from src.config import settings
from src.repositories.audios import AudiosRepository
from src.repositories.images import ImagesRepository


class FileService:
    def __init__(self):
        self.images_dir = settings.IMAGES_DIR
        self.audio_dir = settings.AUDIO_DIR
        self.images_repo = ImagesRepository()
        self.audio_repo = AudiosRepository()

    async def save_image(self, file: UploadFile) -> str | None:
        """Сохраняет изображение и возвращает имя файла"""
        file_name = await self._save_file(file, self.images_dir)
        result = await self.images_repo.add_one(dict(id=file_name))
        return result

    async def save_audio(self, file: UploadFile) -> str | None:
        """Сохраняет аудио файл и возвращает имя файла"""
        file_name = await self._save_file(file, self.audio_dir)
        result = await self.audio_repo.add_one(dict(id=file_name))
        return result

    @staticmethod
    async def _save_file(file: UploadFile, directory: str) -> str | None:
        """Общий метод для сохранения файлов"""
        if not file:
            return None
        # Генерируем уникальное имя файла
        file_extension = file.filename.rsplit(".")[-1]
        file_name = str(uuid.uuid4())
        file_path = f"{directory}/{file_name}.{file_extension}"

        # Сохраняем файл
        async with aiofiles.open(file_path, 'wb') as f:
            content = await file.read()
            await f.write(content)

        return file_name

    async def delete_image(self, filename: str) -> dict:
        file_path = f"{self.images_dir}/{filename}"
        return await self._delete_file(file_path=file_path)

    async def delete_audio(self, filename: str) -> dict:
        file_path = f"{self.audio_dir}/{filename}"
        return await self._delete_file(file_path=file_path)

    @staticmethod
    async def _delete_file(file_path: str) -> dict:
        """Удаляет файл"""
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                return {
                    "status": True,
                    "message": "Файл удален!"
                }
            else:
                return {
                    "status": False,
                    "message": f"Файл {file_path} не существует!"
                }
        except Exception as e:
            return {
                "status": False,
                "message": f"Ошибка при удалении файла {file_path}: {e}!"
            }
