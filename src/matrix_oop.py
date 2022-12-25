import random


class Matrix:

    def __init__(self, rows: int = 3, cols: int = 3):
        """ Default constructor. It creates the matrix and fills it with zeros """
        self.__rows = rows
        self.__cols = cols
        self.__matrix = []

        self.__create_matrix(rows, cols)
        for i in range(rows):
            for j in range(cols):
                self.__matrix[i][j] = 0

    def random_fill_matrix(self):
        """ This method fills the matrix with random numbers """
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__matrix[i][j] = random.randint(1, 11)

    def __create_matrix(self, rows: int, cols: int):
        """ This method creates matrix. It is 'private' method because it uses in constructor only """
        self.__rows, self.__cols = rows, cols
        [self.__matrix.append([0] * self.__cols) for _ in range(self.__rows)]

    def print_matrix(self):
        """ This method print matrix """
        for i in range(self.__rows):
            for j in range(self.__cols):
                print(str(self.__matrix[i][j]).ljust(5), end=' ')
            print()

    def eq_matrix(self, other_matrix):
        """ This method returns True if both matrices equally. Otherwise, it returns False """
        result = True
        if self.__rows and self.__cols:
            for i in range(self.__rows):
                for j in range(self.__cols):
                    if 0 != (self.__matrix[i][j] - other_matrix.__matrix[i][j]):
                        result = False
                        break
        else:
            result = False
        return result

    def sum_matrix(self, other_matrix):
        """ This method adds up the matrix and other_matrix """
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__matrix[i][j] += other_matrix.__matrix[i][j]

    def sub_matrix(self, other_matrix):
        """ This method subtracts other_matrix from the matrix """
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__matrix[i][j] -= other_matrix.__matrix[i][j]

    def mul_number(self, number: float):
        """ This method multiply the matrix by number """
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__matrix[i][j] *= number

    def transpose(self):
        """ This method transposes the matrix """
        result = Matrix(self.__rows, self.__cols)
        for i in range(self.__rows):
            for j in range(self.__cols):
                result.__matrix[i][j] = self.__matrix[j][i]
        return result

    def __minor_of_matrix(self, rows: int, cols: int):
        """ This 'private' method use for calculate minor of the matrix """
        result = Matrix(self.__rows - 1, self.__cols - 1)
        tmp_row = 0
        for i in range(self.__rows):
            if i != rows:
                tmp_col = 0
                for j in range(self.__cols):
                    if j != cols:
                        result.__matrix[tmp_row][tmp_col] = self.__matrix[i][j]
                        tmp_col += 1
                tmp_row += 1
        return result

    def determinant(self):
        """ This method use to find the determinant """
        result = 0
        if self.__rows < 3:
            result = self.__matrix[0][0] if self.__rows == 1 else self.__matrix[0][0] * self.__matrix[1][1] - \
                                                                  self.__matrix[0][1] * self.__matrix[1][0]
        else:
            for i in range(self.__cols):
                minor = self.__minor_of_matrix(0, i)
                result += pow(-1, i) * self.__matrix[0][i] * minor.determinant()
        return result

    def calc_complements(self):
        """ This method use to find the matrix of algebraic complements """
        result = Matrix(self.__rows, self.__cols)
        for i in range(self.__rows):
            for j in range(self.__cols):
                minor = self.__minor_of_matrix(i, j)
                determinant_val = minor.determinant()
                result.__matrix[i][j] = pow((-1), i + j) * determinant_val
        return result

    def inverse_matrix(self):
        """ This method use to find the inverse matrix """
        determinant_val = self.determinant()
        if determinant_val:
            tmp_matrix = self.calc_complements()
            transposed_matrix = tmp_matrix.transpose()
            transposed_matrix.mul_number(1 / self.determinant())
            return transposed_matrix
        else:
            print("error")

    # Accessors and mutators
    def get_matrix_value(self, row, col):
        return self.__matrix[row][col]

    def set_matrix_value(self, row, col, value):
        self.__matrix[row][col] = value

    def set_rows(self, row: int):
        self.__rows = row

    def set_cols(self, col: int):
        self.__cols = col

    # overload operators
    def __add__(self, other_matrix):
        return self.sum_matrix(other_matrix)

    def __sub__(self, other_matrix):
        return self.sub_matrix(other_matrix)

    def __mul__(self, number: float):
        return self.mul_number(number)

    def __eq__(self, other_matrix):
        return self.eq_matrix(other_matrix)

    def __setitem__(self, items: tuple, value: float):
        i, j = items
        self.set_matrix_value(i, j, value)

    def __getitem__(self, items: tuple):
        i, j = items
        return self.get_matrix_value(i, j)
