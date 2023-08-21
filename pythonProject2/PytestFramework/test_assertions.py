def test_sample():
    a = 5
    b = 5
    assert a == b, "a not equal to b"


def test_sample1():
    a = 4
    b = 3
    assert a > b, "This msg won't be displayed"


def test_sample2():
    a = 'Vaishu'
    b = 'Vijay'

    assert a.__eq__(b), "Vaishu not equal to Vijay"
