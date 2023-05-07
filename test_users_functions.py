import csv

import pytest


# -------------------------------------------------------------------
# Используем функциональный подход.
# Выносим логику в отдельные функции или фикстуры
# -------------------------------------------------------------------


@pytest.fixture
def users():
    with open("users.csv") as f:
        return list(csv.DictReader(f, delimiter=";"))


@pytest.fixture
def workers(users):
    return [user for user in users if user["status"] == "worker"]


def assert_worker_is_adult(worker):
    assert int(worker["age"]) >= 18


def assert_workers_are_adult(workers):
    for worker in workers:
        assert_worker_is_adult(worker)


def test_workers_are_adults_v2(workers):
    assert_workers_are_adult(workers)
