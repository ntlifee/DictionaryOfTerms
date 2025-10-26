import logging

from functools import wraps
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from fastapi import HTTPException


def handle_db_errors(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except IntegrityError as e:
            logging.error(f"Повторяющийся ввод или нарушение ограничений в {func.__name__}: {e}")
            raise HTTPException(400, "Повторяющийся ввод или нарушение ограничений")
        except SQLAlchemyError as e:
            logging.error(f"Ошибка базы данных в {func.__name__}: {e}")
            raise HTTPException(500, "Сбой операции с базой данных")
        except Exception as e:
            logging.error(f"Неожиданная ошибка в {func.__name__}: {e}")
            raise HTTPException(500, "Внутренняя ошибка сервера")

    return wrapper
