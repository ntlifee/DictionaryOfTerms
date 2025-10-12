from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "terms"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "password"
    SERVICE_HOST: str = "0.0.0.0"
    SERVICE_PORT: int = 3000
    IMAGES_DIR: str = "static/images"
    AUDIO_DIR: str = "static/audio"
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        env_file_encoding="utf-8"
    )


settings = Settings()


def get_db_url():
    return (f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@"
            f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")
