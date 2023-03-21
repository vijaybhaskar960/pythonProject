import unittest

def setUpModule():
    print("setUpModule")

def tearDownModule():
    print("tearDownModule")

class TestCalculator(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("This is login Test")
    @classmethod
    def tearDown(self):
        print("This is logout Test")
    @classmethod
    def setUpClass(cls):
        print("This is setupclass Method")

    @classmethod
    def tearDownClass(cls):
        print("This is Tear down Class")

    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        self.assertEqual(4 - 2, 2)

    def test_multiplication(self):
        self.assertEqual(3 * 5, 15)

    def test_division(self):
        self.assertEqual(10 / 2, 5)

    def test_demo(self):
        print("This is demo method")


if __name__ == "__main__":
    unittest.main()