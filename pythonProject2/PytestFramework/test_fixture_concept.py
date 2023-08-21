import pytest
@pytest.fixture()
def setup_teardown():
    print("Before a test case Starting")
    yield
    print("After Every Test Case")
def test_add(setup_teardown):
    print("This is Add Method ")


def test_sub(setup_teardown):
    print("This is Sub Method")



def test_calculator(setup_teardown):
    assert 2+2 == 4