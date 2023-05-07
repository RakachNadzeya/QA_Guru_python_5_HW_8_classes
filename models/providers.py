import csv

from models.users import User


class UserProvider:

    def get_users(self) -> list[User]:
        raise NotImplementedError("Реализуйте эту функцию в конкретном провайдере")


class CsvUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        with open("users.csv") as f:
            users_dicts = list(csv.DictReader(f, delimiter=";"))
        users_models = []
        for user in users_dicts:
            users_models.append(User.from_csv(user))
        return users_models


class DatabaseUserProvider(UserProvider):
    pass


class ApiUserProvider(UserProvider):
    pass
