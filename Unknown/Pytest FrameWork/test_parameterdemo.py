import pytest

@pytest.fixture(params=['a','b'])
def demo(request):
    print(request.param)


def testLogin(demo):
    print("Login successful")