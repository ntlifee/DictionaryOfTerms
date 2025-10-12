from abc import ABC, abstractmethod
from sqlalchemy import insert, select, delete, update

from src.database import async_session_maker


class AbstractRepository(ABC):
    model = None

    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplemented

    @abstractmethod
    async def find_all(self) -> list:
        raise NotImplemented

    @abstractmethod
    async def delete(self, item_id: int) -> bool:
        raise NotImplemented

    @abstractmethod
    async def update(self, item_id, data: dict):
        raise NotImplemented


class SQLAlchemyRepository(AbstractRepository):
    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_all(self) -> list:
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = [row[0].to_model() for row in res.all()]
            return res

    async def delete(self, item_id: int) -> bool:
        async with async_session_maker() as session:
            stmt = delete(self.model).where(self.model.id == item_id)
            res = await session.execute(stmt)
            await session.commit()
            return res.rowcount > 0

    async def update(self, item_id, data: dict):
        async with async_session_maker() as session:
            stmt = update(self.model).where(self.model.id == item_id).values(**data).returning(self.model)
            res = await session.execute(stmt)
            updated_item = res.scalar_one_or_none()
            await session.commit()
            return updated_item
