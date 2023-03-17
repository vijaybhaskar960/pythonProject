import unittest

class TestCalculator(unittest.TestCase):

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