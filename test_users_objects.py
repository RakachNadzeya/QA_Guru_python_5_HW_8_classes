import csv

import pytest

from models.providers import UserProvider, CsvUserProvider, DatabaseUserProvider, ApiUserProvider
from models.users import User, UserStatus, Worker


# -------------------------------------------------------------------
# Используем объектный подход работы с данными
# -------------------------------------------------------------------


@pytest.fixture(params=[CsvUserProvider(), DatabaseUserProvider(), ApiUserProvider()])
def provider(request) -> UserProvider:
    return request.param


@pytest.fixture
def users(provider) -> list[User]:
    user_models = provider.get_users()
    return user_models


@pytest.fixture
def workers(users) -> list[Worker]:
    return [Worker.from_user(user) for user in users if user.status == UserStatus.Worker]


def assert_workers_are_adult(workers):
    for worker in workers:
        assert worker.is_adult()


def test_workers_are_adults_v2(workers):
    assert_workers_are_adult(workers)
