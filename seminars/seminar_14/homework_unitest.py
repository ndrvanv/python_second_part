import unittest

def multyply_numbers(a, b):
    return a * b

class TestMultyPlication(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multyply_numbers(2, 3), 6)

    def test_negative_numbers(self):
        self.assertEqual(multyply_numbers(-2, 3), 6)

    def zero_test(self):
        self.assertEqual(multyply_numbers(5, 0), 0)

if __name__ == "__main__":
    unittest.main()