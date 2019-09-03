import unittest
import calc

class TestCalc(unittest.Testcase):

    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result,15)
   # def test_sub(self):
    #    result = calc.sub(200,100)
     #   self.assertEqual(result,100)

if __name__ == '__main__':
    unittest.main()
