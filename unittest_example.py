class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

if __name__ == '__main__':
    unittest.main()
