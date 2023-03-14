import pytest


@pytest.mark.skip   # Skip the Specific test case
def test_login():
    print("Login successful")


def test_logoff():
    print("Logoff successful")


def testCalculator():
    assert 2 + 2 == 4
