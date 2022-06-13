import unittest
import aritmatika

class Matrix(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(aritmatika.mean(), 168.2)
    
    def test_factorial(self):
        self.assertEqual(aritmatika.factorial(), 720)
    
    def test_handshake(self):
        self.assertEqual(aritmatika.handshake(), 780)

if (__name__ == '__main__'):
    unittest.main()