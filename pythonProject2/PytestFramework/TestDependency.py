import pytest

class TestDepends:

    @pytest.mark.dependency()
    def test_method1(self):
        print("This is test_method1")
        assert 1+4 == 6

    @pytest.mark.dependency(depends= ["TestDepends::test_method1"])
    def test_method2(self):
        print("This is test_method2")

    def test_method3(self):
        print("This is test_method3")
        assert 2+4 == 6

class TestNew:

    def test_method3(self):
        print("This is test_method4")
