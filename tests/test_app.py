from httpx import AsyncClient
import pytest
from fastid.app import app

# @pytest.mark.asyncio
# async def test_read_main():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Hello World!"}

# @pytest.mark.asyncio
# async def test_read_main_wrong_message():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/")
#     assert response.status_code == 200
#     assert response.json() != {"message": "Batatinhas"}

@pytest.mark.asyncio
async def test_read_main():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "Hello World!" in response.text

@pytest.mark.asyncio
async def test_read_main_wrong_message():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "Batatinhas" not in response.text

@pytest.mark.asyncio
async def test_read_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/login")
    assert response.status_code == 200