import pytest

@pytest.fixture(scope="module", autouse = True)
def connect_db():
    print("I need to connect employee database")
    yield
    print("I need to Disconnect employee database")


def test_first(connect_db):
    print("I am Verify the test first employee name and id")


def test_second(connect_db):
    print("I am Verify the test first employee name and id")



def test_third(connect_db):
    print("I am Verify the test first employee name and id")