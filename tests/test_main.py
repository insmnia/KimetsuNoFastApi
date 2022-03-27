from conftests import UserFactory, hashed_pass_from_abc
from app.core.services.user import UserService


def test_password_hashing():
    user = UserFactory.stub()
    hashed_password = UserService.get_password_hash(user.password)

    assert hashed_password is not None


def test_password_hash_matching():
    assert hashed_pass_from_abc == UserService.get_password_hash('abc')
