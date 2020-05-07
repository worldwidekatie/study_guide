import unittest
from math1 import Math1

class Math1Tests(unittest.TestCase):
    
    def test_addition(self):
        math1 = Math1()
        self.assertEqual(math1.addition(), 30)
    
    def test_subtraction(self):
        math1 = Math1()
        self.assertEqual(math1.subtraction(), -10)
    

if __name__ == "__main__":
    unittest.main()