import pytest

from app.core.services.token import TokenService
from app.core.services.user import UserService
from conftests import UserFactory, minutes


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
