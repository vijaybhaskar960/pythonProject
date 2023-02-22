import pytest


@pytest.yield_fixture()
def setup():
    print("Once before every method")
    yield
    print("Once after Every method")


def testmethod(setup):
    print("This is testmethod")


def testmethod1(setup):
    print("This is testmethod1")



