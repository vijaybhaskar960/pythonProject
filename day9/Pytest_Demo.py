import pytest


@pytest.fixture()
def setup():
    print("Before test method")


def test_method(setup):
    print("This is method")


def test_method1():
    print("This is method1")
