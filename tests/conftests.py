from datetime import timedelta

from factory import Factory
from faker import Faker
from app.models.user import UserBase
from pytest import fixture

faker = Faker()


class UserFactory(Factory):
    class Meta:
        model = UserBase

    username = faker.name()
    password = faker.name() + 'psw'


@fixture(autouse=True)
def minutes():
    return timedelta(minutes=30)
