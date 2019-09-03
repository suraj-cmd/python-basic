import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result,15)
    def test_sub(self):
        result = calc.sub(100,50)
        self.assertEqual(result,50)

if __name__ == '__main__':
    unittest.main()
