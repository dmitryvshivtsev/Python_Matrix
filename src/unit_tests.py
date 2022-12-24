import matrix_oop
import unittest


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix_a = matrix_oop.Matrix(2, 2)
        self.matrix_b = matrix_oop.Matrix(2, 2)

    def test_set_val(self):
        self.matrix_a.set_matrix_value(0, 0, 5)
        self.matrix_a.set_matrix_value(0, 1, 5)
        self.matrix_a.set_matrix_value(1, 0, 5)
        self.matrix_a.set_matrix_value(1, 1, 5)

        self.matrix_b.set_matrix_value(0, 0, 5)
        self.matrix_b.set_matrix_value(0, 1, 5)
        self.matrix_b.set_matrix_value(1, 0, 5)
        self.matrix_b.set_matrix_value(1, 1, 5)

        self.assertEqual(self.matrix_a.get_matrix_value(0, 1), self.matrix_b.get_matrix_value(0, 1))
        self.assertTrue(self.matrix_a == self.matrix_b)

    def test_sum(self):
        self.matrix_a.set_matrix_value(0, 0, 5)
        self.matrix_a.set_matrix_value(0, 1, 5)
        self.matrix_a.set_matrix_value(1, 0, 5)
        self.matrix_a.set_matrix_value(1, 1, 5)

        self.matrix_b.set_matrix_value(0, 0, 5)
        self.matrix_b.set_matrix_value(0, 1, 5)
        self.matrix_b.set_matrix_value(1, 0, 5)
        self.matrix_b.set_matrix_value(1, 1, 5)

        self.matrix_a + self.matrix_b

        self.assertEqual(self.matrix_a.get_matrix_value(0, 0), 10)
        self.assertEqual(self.matrix_a.get_matrix_value(0, 1), 10)

    def test_sub(self):
        self.matrix_a.set_matrix_value(0, 0, 5)
        self.matrix_a.set_matrix_value(0, 1, 5)
        self.matrix_a.set_matrix_value(1, 0, 5)
        self.matrix_a.set_matrix_value(1, 1, 5)

        self.matrix_b.set_matrix_value(0, 0, 5)
        self.matrix_b.set_matrix_value(0, 1, 5)
        self.matrix_b.set_matrix_value(1, 0, 5)
        self.matrix_b.set_matrix_value(1, 1, 5)

        self.matrix_a - self.matrix_b

        self.assertEqual(self.matrix_a.get_matrix_value(0, 0), 0)


    def test_inverse(self):
        self.matrix_a = matrix_oop.Matrix(3, 3)
        self.matrix_b = matrix_oop.Matrix(3, 3)

        self.matrix_a.set_matrix_value(0, 0, 98)
        self.matrix_a.set_matrix_value(0, 1, 52)
        self.matrix_a.set_matrix_value(0, 2, 50)
        self.matrix_a.set_matrix_value(1, 0, 30)
        self.matrix_a.set_matrix_value(1, 1, 18)
        self.matrix_a.set_matrix_value(1, 2, 34)
        self.matrix_a.set_matrix_value(2, 0, 1)
        self.matrix_a.set_matrix_value(2, 1, 2)
        self.matrix_a.set_matrix_value(2, 2, 3)

        self.matrix_b = self.matrix_a.inverse_matrix()

        self.assertEqual(self.matrix_b.get_matrix_value(0, 0), 0.00641025641025641)
        self.assertEqual(self.matrix_b.get_matrix_value(2, 2), -0.09340659340659341)


if __name__ == "__main__":
    unittest.main()
