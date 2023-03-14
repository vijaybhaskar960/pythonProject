import pytest

def test_add():
    print("This is Add Method ")


def test_sub():
    print("This is Sub Method")



def test_calculator(setup):
    assert 2+2 == 4