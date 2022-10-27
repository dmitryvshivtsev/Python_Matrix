from matrix_oop import Matrix
import unittest


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix()

    def test_add(self):
        self.assertTrue(1, 1)


if __name__ == "__main__":
    unittest.main()
