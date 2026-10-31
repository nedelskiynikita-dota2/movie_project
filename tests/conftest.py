import asyncio

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.main import app
from src.models import Base
from src.database import get_session


@pytest.fixture
def client(tmp_path):
    database_url = f"sqlite+aiosqlite:///{tmp_path}/test.db"

    engine = create_async_engine(database_url)
    TestingSessionLocal = async_sessionmaker(
        bind=engine,
        expire_on_commit=False
    )

    async def create_tables():
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)

    asyncio.run(create_tables())

    async def override_get_session():
        async with TestingSessionLocal() as session:
            yield session

    app.dependency_overrides[get_session] = override_get_session

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    asyncio.run(engine.dispose())
