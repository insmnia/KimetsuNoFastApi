
from factory import Factory
from faker import Faker

from app.models.user import UserBase

faker = Faker()


class UserFactory(Factory):
    class Meta:
        model = UserBase

    username = faker.name()
    password = faker.name() + 'psw'
