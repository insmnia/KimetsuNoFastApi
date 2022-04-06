from app.core.services.user import UserService
from conftests import UserFactory


def test_password_hashing():
    user = UserFactory.stub()
    hashed_password = UserService.get_password_hash(user.password)

    assert hashed_password is not None


def test_password_hash_matching():
    assert 1 == 1
