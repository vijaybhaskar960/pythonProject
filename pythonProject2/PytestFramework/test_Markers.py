import pytest


@pytest.mark.smoke
def test_m1():
    print("M1 Method")

@pytest.mark.regression
def test_m2():
    print("M2 Method")

@pytest.mark.regression
def test_m3():
    print("M3 Method")


@pytest.mark.smoke
def test_m4():
    print("M4 Method")