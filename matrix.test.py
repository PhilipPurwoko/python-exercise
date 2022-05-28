import unittest
import matrix

class Matrix(unittest.TestCase):
    def test_reverse_array(self):
        self.assertEqual(matrix.reverse_array(), [8, 1, 7, 5, 3])

    def test_penggabungan_array(self):
        self.assertEqual(matrix.penggabungan_array(), [1, 2, 3, 4, 5, 6])
    
    def test_pernjumlahan_nilai_array(self):
        self.assertEqual(matrix.menjumlahkan_nilai_array(), [5, 7, 9])
    
    def test_mengubah_array_menjadi_matrix(self):
        self.assertEqual(matrix.mengubah_array_menjadi_matrix(), [[6, 1, 0], [1, 4, 8]])

    def test_perkalian_matrix(self):
        self.assertEqual(matrix.perkalian_matrix(), [[19, 22], [43, 50]])

if (__name__ == '__main__'):
    unittest.main()