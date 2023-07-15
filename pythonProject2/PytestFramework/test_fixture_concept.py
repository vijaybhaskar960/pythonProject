import pytest
@pytest.fixture()
def setup():
    print("Before a test case Starting")
    yield
    print("After Every Test Case")
def test_add(setup):
    print("This is Add Method ")


def test_sub(setup):
    print("This is Sub Method")



def test_calculator(setup):
    assert 2+2 == 4