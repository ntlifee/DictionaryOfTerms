import os

import aiofiles
import uuid
from fastapi import UploadFile

from src.config import settings


class FileService:
    def __init__(self):
        self.images_dir = settings.IMAGES_DIR
        self.audio_dir = settings.AUDIO_DIR

    async def save_image(self, file: UploadFile) -> str | None:
        """Сохраняет изображение и возвращает имя файла"""
        return await self._save_file(file, self.images_dir)

    async def save_audio(self, file: UploadFile) -> str | None:
        """Сохраняет аудио файл и возвращает имя файла"""
        return await self._save_file(file, self.audio_dir)

    @staticmethod
    async def _save_file(file: UploadFile, directory: str) -> str | None:
        """Общий метод для сохранения файлов"""
        if not file:
            return None
        # Генерируем уникальное имя файла
        file_extension = file.filename.rsplit(".")[-1]
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        file_path = f"{directory}/{unique_filename}"

        # Сохраняем файл
        async with aiofiles.open(file_path, 'wb') as f:
            content = await file.read()
            await f.write(content)

        return unique_filename

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
