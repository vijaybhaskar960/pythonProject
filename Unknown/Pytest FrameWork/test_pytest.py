import pytest


@pytest.mark.login
def test_add():
    name = "selenium"
    assert name.upper() == "SELENIUM"
    print("This is add method")

def test_sub():
    surname = 'Tegalapalli'
    assert surname == "Tegalapalli"

@pytest.mark.login
def test_m1():
    name = "Amulya"
    assert name == 'Amulya'
