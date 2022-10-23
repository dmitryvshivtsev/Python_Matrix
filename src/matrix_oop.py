import random


class Matrix:
    __rows: int = 1
    __cols: int = 1
    __matrix: list = []

    def __init__(self, rows: int = 3, cols: int = 3):
        self.__rows = rows
        self.__cols = cols
        self.create_matrix(rows, cols)
        for i in range(rows):
            for j in range(cols):
                self.__matrix[i][j] = 0

    def random_fill_matrix(self):
        self.create_matrix(self.__rows, self.__cols)
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__matrix[i][j] = random.randint(1, 10)

    def create_matrix(self, rows: int, cols: int):
        self.__rows = rows
        self.__cols = cols
        for i in range(rows):
            self.__matrix.append([0] * cols)
            for j in range(cols):
                self.__matrix[i][j] = 0

    def print_matrix(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                print(str(self.__matrix[i][j]).ljust(3), end=' ')
            print()

    def sum_matrix(self, other_matrix):
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__matrix[i][j] += other_matrix.__matrix

    def sub_matrix(self, other_matrix):
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__matrix[i][j] -= other_matrix.__matrix[i][j]

    def mul_number(self, number):
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__matrix[i][j] *= number

    def transpose(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__matrix[i][j] = self.__matrix[j][i]


# A = Matrix(5, 5)
# A.random_fill_matrix()
# A.print_matrix()
# print()
# # A.Transpose()
# A.print_matrix()
