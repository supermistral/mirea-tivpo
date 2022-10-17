from __future__ import annotations
from typing import Any, List, Tuple, Union

MatrixType = List[List[float]]


class IsNotSquareMatrixError(ValueError):
    def __init__(self, message: str = "Matrix must be square"):
        super().__init__(message)


class MatrixSizeMismatchError(ArithmeticError):
    def __init__(self, message: str = "The sizes of the matrix doesn't allow the operation"):
        super().__init__(message)


class Matrix:
    def __init__(self, matrix: MatrixType):
        self._matrix = matrix
        self._size = self._size_by_matrix(matrix)

    def _size_by_matrix(self, matrix: MatrixType) -> Tuple[int, int]:
        rows = len(matrix)
        return rows, len(matrix[0]) if rows > 0 else 0

    def _determinant(self, matrix: MatrixType) -> float:
        size = self._size_by_matrix(matrix)

        if size[0] == 1:
            return matrix[0][0]
        if size[0] == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0
        for i in range(size[1]):
            det += matrix[0][i] * self._cofactor(1, i + 1, matrix)
        
        return det

    def _minor(self, r: int, c: int, matrix: MatrixType) -> float:
        new_matrix: MatrixType = []

        for i in range(self._size[0]):
            if i + 1 != r:
                new_matrix.append([])
                for j in range(self._size[1]):
                    if j + 1 != c:
                        new_matrix[-1].append(matrix[i][j])

        return self._determinant(new_matrix)

    def _cofactor(self, r: int, c: int, matrix: MatrixType) -> float:
        factor = 1 if (r + c) % 2 == 0 else -1
        return factor * self._minor(r, c, matrix)

    def is_square(self) -> bool:
        return self._size[0] == self._size[1]

    def _check_for_square(self) -> None:
        if not self.is_square():
            raise IsNotSquareMatrixError()

    def size(self) -> Tuple[int, int]:
        return self._size

    def determinant(self) -> float:
        self._check_for_square()
        return self._determinant(self._matrix)

    def minor(self, r: int, c: int) -> float:
        self._check_for_square()
        return self._minor(r, c, self._matrix)

    def cofactor(self, r: str, c: str) -> float:
        self._check_for_square()
        return self._cofactor(r, c, self._matrix)

    def get_matrix(self) -> MatrixType:
        return self._matrix

    def __mul__(self, other: Any) -> Union[Matrix, float, None]:
        if isinstance(other, (int, float)):
            matrix = [[0 for _ in range(self._size[1])] for _ in range(self._size[0])]
            for i in range(self._size[0]):
                for j in range(self._size[1]):
                    matrix[i][j] = self._matrix[i][j] * other
            return Matrix(matrix)
        if isinstance(other, Matrix):
            other_size = other.size()

            if self._size[1] != other_size[0]:
                raise MatrixSizeMismatchError()

            other_matrix = other.get_matrix()
            matrix = [[0 for _ in range(other_size[1])] for _ in range(self._size[0])]
            for i in range(self._size[0]):
                for j in range(other_size[1]):
                    elem = sum([self._matrix[i][k] * other_matrix[k][j] for k in range(self._size[1])])
                    matrix[i][j] = elem
            return Matrix(matrix)

    def __rmul__(self, other: Any) -> Union[Matrix, float, None]:
        return self + other
