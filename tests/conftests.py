from factory import Factory
from faker import Faker
from app.models.user import User
from app.core.services.user import UserService
from pytest import fixture

faker = Faker()


class UserFactory(Factory):
    class Meta:
        model = User

    username = faker.name()
    password = faker.name() + 'psw'


@fixture(autouse=True)
def hashed_pass_from_abc():
    return UserService.get_password_hash("abc")
