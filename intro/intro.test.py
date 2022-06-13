import unittest
import intro

class TestBeginnerExercise(unittest.TestCase):
    def test_penjumlahan(self):
        self.assertEqual(intro.penjumlahan(), 40)

    def test_perkalian(self):
        self.assertEqual(intro.perkalian(), 200)

    def test_perpangkatan(self):
        self.assertEqual(intro.perpangkatan(), 248832)

    def test_deret_bilangan_ganjil(self):
        self.assertEqual(intro.deret_bilangan_ganjil(), [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

    def test_deret_bilangan_genap(self):
        self.assertEqual(intro.deret_bilangan_genap(), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_deret_bilangan_prima(self):
        self.assertEqual(intro.deret_bilangan_prima(), [1, 3, 4, 5, 6, 7, 8, 9, 10, 11])

if (__name__ == '__main__'):
    unittest.main()