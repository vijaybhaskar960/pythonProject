import pytest


@pytest.fixture(params=["a",'b'])
def demo_fixture(request):
    print(request.param)


def testAnimal(demo_fixture):
    print("This is Animal Method")


def testBird():
    print("This is Bird Method")


@pytest.mark.parametrize("a, b, final",[(2,3,5),(9,9,18)])
def testAdd(a, b, final):
    assert a+b ==  final

