import unittest
import multi
class ExampleCase(unittest.TestCase):
    
    def test_description(self):
        result = multi.add(50,50)
        self.assertEqual(result,10)
    
    def test_description(self):
        result = multi.multi(5,2)
        self.assertEqual(result,10)
       
if __name__ == '__main__':
    unittest.main(verbosity=2)
