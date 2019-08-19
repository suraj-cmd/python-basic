import unittest 
  
class TestStringMethods(unittest.TestCase): 
      
    def setUp(self): 
        pass
  
    # Returns True if the string contains 4 a. 
    def test_strings_a(self): 
        self.assertEqual( 'a'*4, 'aaaa') 
  
  
if __name__ == '__main__': 
    unittest.main() 
