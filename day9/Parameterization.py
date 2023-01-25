import pytest


class Test:

    @pytest.mark.parametrize("geometry",['test1','test2','test3'])
    def test_method1(self,geometry):
        print("Geometry is called is:{}".format(geometry))

