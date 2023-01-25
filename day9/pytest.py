import pytest


class Test:

    @pytest.fixture(autouse=True)
    def my_fixture(self):
        print("Fixture will called")

    def test_m1(self):
        print('This is Class A Method')

    def test_add(self):
        print("This is Add Method")
