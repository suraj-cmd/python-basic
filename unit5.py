import unittest
class TestCase(unittest.TestCase):
    def Exampletest(self):
        a = 'none'
        b = 'none'
        self.assertEqual(a, b)
if __name__ == '__main__':
    unittest.main(verbose=2)
