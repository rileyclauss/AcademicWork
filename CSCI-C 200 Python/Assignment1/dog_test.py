import dog

import unittest

class MyTests(unittest.TestCase):

    def test_S(self):
        self.assertEqual(dog.S(0),0)
        self.assertEqual(dog.S(1),1)
        self.assertEqual(dog.S(2),4)
        self.assertEqual(dog.S(3),9)

if __name__=="__main__":
    unittest.main()

