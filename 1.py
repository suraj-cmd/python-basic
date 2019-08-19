import unittest
 
class Test(unittest.testcase):

    def setup(self):
        pass

    def test(self):
       self.assertequal( 'a'*4, 'aaaa')

if __name__ == '__main__':
    unittest.main()
