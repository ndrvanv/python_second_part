
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        return "\n".join([' '.join(map(str, row)) for row in self.data])

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data
        return False

    def __add__(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        raise MatrixOperationException("Матрицы не могут быть сложены")


class MatrixOperationException:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'Ошибка операции с матрицами: {self.message}'

try:
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 2], [3, 4]]
    print(matrix1)

    matrix2 = Matrix(2, 2)
    matrix2.data = [[5, 6], [7, 8]]
    print(matrix2)

    matrix3 = Matrix(2, 2)
    matrix3.data = [[1, 2], [3, 4]]
    print(matrix3)

    print(matrix1 == matrix2)  # False
    print(matrix1 == matrix3)  # True

    matrix_sum = matrix1 + matrix2
    print(matrix_sum)

    matrix_invalid = Matrix(2, 3)
    matrix_invalid.data = [[1, 2, 3], [4, 5, 6]]
    matrix_sum_invalid = matrix1 + matrix_invalid  # Raises MatrixOperationException

except MatrixOperationException as e:
    print(e)
