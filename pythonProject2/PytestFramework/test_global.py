import pytest


class TestGlobal:
    name = "Global Value"
    def test_method_1(self):
        print("This is Method_1")
        print(self.name)

    @pytest.mark.sanity
    def test_method_2(self):
        print("This is Method_2")
        pytest.name = "Local Value"
        print(pytest.name)
        pytest.name = "Local Value1"
        print(pytest.name)

    @pytest.mark.sanity
    def test_method_3(self):
        print("This is Method_3")
        print(pytest.name)