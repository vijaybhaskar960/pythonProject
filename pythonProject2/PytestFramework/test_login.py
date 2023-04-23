import pytest


@pytest.mark.linux   # Skip the Specific test case
def test_login():
    print("Login successful")


def test_logoff():
    print("Logoff successful")

@pytest.mark.linux
def testCalculator():
    assert 2 + 2 == 4
