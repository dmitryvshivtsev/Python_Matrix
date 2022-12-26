from context import matrix_oop
import unittest


class TestMatrix(unittest.TestCase):
    def setUp(self):
        pass

    def test_set_val(self):
        matrix_a = matrix_oop.Matrix(2, 2)
        matrix_b = matrix_oop.Matrix(2, 2)
        matrix_a[0, 0] = 5
        matrix_a[0, 1] = 5
        matrix_a[1, 0] = 5
        matrix_a[1, 1] = 5

        matrix_b[0, 0] = 5
        matrix_b[0, 1] = 5
        matrix_b[1, 0] = 5
        matrix_b[1, 1] = 5

        self.assertEqual(matrix_a[0, 1], matrix_b[0, 1])
        self.assertTrue(matrix_a == matrix_b)

    def test_sum(self):
        matrix_a = matrix_oop.Matrix(2, 2)
        matrix_b = matrix_oop.Matrix(2, 2)

        matrix_a[0, 0] = 5
        matrix_a[0, 1] = 5
        matrix_a[1, 0] = 5
        matrix_a[1, 1] = 5

        matrix_b[0, 0] = 5
        matrix_b[0, 1] = 5
        matrix_b[1, 0] = 5
        matrix_b[1, 1] = 5

        matrix_a + matrix_b

        self.assertEqual(matrix_a[0, 0], 10)
        self.assertEqual(matrix_a[1, 1], 10)

    def test_sub(self):
        matrix_a = matrix_oop.Matrix(2, 2)
        matrix_b = matrix_oop.Matrix(2, 2)

        matrix_a[0, 0] = 5
        matrix_a[0, 1] = 5
        matrix_a[1, 0] = 5
        matrix_a[1, 1] = 5

        matrix_b[0, 0] = 5
        matrix_b[0, 1] = 5
        matrix_b[1, 0] = 5
        matrix_b[1, 1] = 5

        matrix_a - matrix_b

        self.assertEqual(matrix_a[0, 0], 0)

    def test_mul(self):
        matrix_a = matrix_oop.Matrix(2, 2)

        matrix_a[0, 0] = 5
        matrix_a[0, 1] = 5
        matrix_a[1, 0] = 5
        matrix_a[1, 1] = 3

        matrix_a * 5

        self.assertEqual(matrix_a[0, 0], 25)
        self.assertEqual(matrix_a[1, 1], 15)

    def test_transpose(self):
        matrix_a = matrix_oop.Matrix(3, 3)

        matrix_a[0, 0] = 1
        matrix_a[0, 1] = 2
        matrix_a[0, 2] = 3
        matrix_a[1, 0] = 4
        matrix_a[1, 1] = 5
        matrix_a[1, 2] = 6
        matrix_a[2, 0] = 7
        matrix_a[2, 1] = 8
        matrix_a[2, 2] = 9

        matrix_b = matrix_a.transpose()

        self.assertEqual(matrix_b[0, 1], 4)
        self.assertEqual(matrix_b[1, 0], 2)
        self.assertEqual(matrix_b[1, 2], 8)
        self.assertEqual(matrix_b[2, 1], 6)

    def test_determinant(self):
        matrix_a = matrix_oop.Matrix(3, 3)

        matrix_a[0, 0] = 1
        matrix_a[0, 1] = -2
        matrix_a[0, 2] = 3
        matrix_a[1, 0] = 4
        matrix_a[1, 1] = 0
        matrix_a[1, 2] = 6
        matrix_a[2, 0] = -7
        matrix_a[2, 1] = 8
        matrix_a[2, 2] = 9

        det = matrix_a.determinant()

        self.assertEqual(det, 204)

    def test_calc_complements(self):
        matrix_a = matrix_oop.Matrix(3, 3)

        matrix_a[0, 0] = 2
        matrix_a[0, 1] = -3
        matrix_a[0, 2] = 4
        matrix_a[1, 0] = 5
        matrix_a[1, 1] = 2
        matrix_a[1, 2] = 1
        matrix_a[2, 0] = 1
        matrix_a[2, 1] = 2
        matrix_a[2, 2] = 3

        calc_complems = matrix_a.calc_complements()

        self.assertEqual(calc_complems[0, 1], -14)

    def test_inverse(self):
        self.matrix_a = matrix_oop.Matrix(3, 3)
        self.matrix_b = matrix_oop.Matrix(3, 3)

        self.matrix_a[0, 0] = 98
        self.matrix_a[0, 1] = 52
        self.matrix_a[0, 2] = 50
        self.matrix_a[1, 0] = 30
        self.matrix_a[1, 1] = 18
        self.matrix_a[1, 2] = 34
        self.matrix_a[2, 0] = 1
        self.matrix_a[2, 1] = 2
        self.matrix_a[2, 2] = 3

        self.matrix_b = self.matrix_a.inverse_matrix()

        self.assertEqual(self.matrix_b[0, 0], 0.00641025641025641)
        self.assertEqual(self.matrix_b[2, 2], -0.09340659340659341)


if __name__ == "__main__":
    unittest.main()
