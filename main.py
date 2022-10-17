from typing import List, Tuple

MatrixType = List[List[float]]


class IsNotSquareMatrixError(ValueError):
    def __init__(self, message: str = "Matrix must be square"):
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

    def size(self) -> Tuple[int, int]:
        return self._size

    def determinant(self) -> float:
        if self._size[0] != self._size[1]:
            raise IsNotSquareMatrixError()

        return self._determinant(self._matrix)

    def minor(self, r: int, c: int) -> float:
        if self._size[0] != self._size[1]:
            raise IsNotSquareMatrixError()

        return self._minor(r, c, self._matrix)

    def cofactor(self, r: str, c: str) -> float:
        if self._size[0] != self._size[1]:
            raise IsNotSquareMatrixError()

        return self._cofactor(r, c, self._matrix)
