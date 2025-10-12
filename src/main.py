import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from src.config import settings
from src.routers.router import router


def create_app() -> FastAPI:
    """
   Создание и конфигурация FastAPI приложения.

   Returns:
       Сконфигурированное приложение FastAPI
   """
    app = FastAPI(
        title="Стартовая сборка FastAPI",
        description="Электронный словарь терминов",
        version="1.0.0",
    )

    # Настройка CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    # Монтирование статических файлов
    app.mount(
        '/static',
        StaticFiles(directory='static'),
        name='static'
    )

    app.include_router(router)

    return app


def main():
    # Создание экземпляра приложения
    app = create_app()
    uvicorn.run(app, host=settings.SERVICE_HOST, port=int(settings.SERVICE_PORT))


if __name__ == "__main__":
    main()
