
import unittest


def addition(num1, num2):
    return num1 + num2

def multiplication(num1, num2):
    return num1 * num2


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(100, 200), 300)

    def test_multiplication(self):
        self.assertEqual(multiplication(100, 200), 20000)




if __name__ == '__main__':
    unittest.main()
