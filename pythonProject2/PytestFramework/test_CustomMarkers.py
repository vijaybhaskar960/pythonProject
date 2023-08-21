import pytest


@pytest.mark.smoke
def test_add():
    print("Add Method")

@pytest.mark.xfail
def test_sub():
    print("Sub Method")

@pytest.mark.xfail
def test_mul():
    print("Mul Method")