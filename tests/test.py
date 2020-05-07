import unittest
from ..my_studyguide.math1 import Math1

class Math1Tests(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(Math1.addition, 30)

if __name__ == "__main__":
    unittest.main()