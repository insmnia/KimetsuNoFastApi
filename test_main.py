import pytest

from app.core.services.token import TokenService
from app.core.services.user import UserService
from conftests import UserFactory, minutes, override_get_database
from app.db.mongodb import get_database
from app.main import app
from httpx import AsyncClient
from app.db.mongodb import get_database


@pytest.mark.asyncio
async def test_list_hunter(override_get_database):
    app.dependency_overrides[get_database] = override_get_database
    async with AsyncClient(app=app, base_url="") as ac:
        response = await ac.get('/api/v1/hunters/')

    assert response.status_code == 200


def test_password_hashing():
    user = UserFactory.stub()
    hashed_password = UserService.get_password_hash(user.password)

    assert hashed_password is not None


def test_token_generation(minutes):
    user = UserFactory.stub()
    assert TokenService.create_access_token(
        data={"sub": user.username},
        expires_delta=minutes
    ) is not None


@pytest.mark.asyncio
async def test_token_validation(minutes):
    user = UserFactory.stub()
    token = await TokenService.create_access_token(
        data={"sub": user.username},
        expires_delta=minutes
    )
    token_data = await TokenService.get_token_data(token)
    assert token_data.username == user.username
